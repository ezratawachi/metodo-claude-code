#!/usr/bin/env python3
# Aviso de orden (hook Stop): al final de cada respuesta revisa que PLAN.md y CLAUDE.md sigan ordenados.
# Si algo se pasa, se lo dice a Claude para que lo arregle en el momento. Sin problemas no dice nada.
# Solo actúa en proyectos del método (un PLAN.md con "## Dónde quedamos"); en cualquier otra carpeta se calla.
import json, os, re, select, sys

MAX_PLAN = 10_000   # bytes
MAX_CLAUDE = 5_000  # bytes
MAX_HECHA = 300     # caracteres de una tarea [x] en el plan
MAX_DONDE = 4       # líneas de "Dónde quedamos"
DONDE = re.compile(r'^## Dónde quedamos\n(.*?)(?=^## |\Z)', re.M | re.S)


def leer(raiz, nombre):
    try:
        with open(os.path.join(raiz, nombre), encoding='utf-8') as f:
            return f.read()
    except OSError:
        return None


def sin_comentarios(texto):
    # Las plantillas traen ayudas entre <!-- -->: no cuentan como contenido.
    return re.sub(r'<!--.*?-->\n?', '', texto, flags=re.S)


def problemas(raiz):
    plan = leer(raiz, 'PLAN.md')
    if plan is None or not DONDE.search(plan):
        return []  # no es un proyecto del método
    claude = leer(raiz, 'CLAUDE.md')
    hay = []
    if len(plan.encode()) > MAX_PLAN:
        hay.append(f'PLAN.md pesa {len(plan.encode())} bytes (máximo {MAX_PLAN}): pasar lo hecho a docs/plan-hecho.md o el detalle a docs/historial/fase-NN.md.')
    if claude is not None and len(claude.encode()) > MAX_CLAUDE:
        hay.append(f'CLAUDE.md pesa {len(claude.encode())} bytes (máximo {MAX_CLAUDE}): dejar solo reglas, datos fijos y comandos.')

    lineas = plan.split('\n')
    for i, l in enumerate(lineas, 1):
        if l.startswith('- [x]'):
            if len(l) > MAX_HECHA:
                hay.append(f'PLAN.md:{i} tarea hecha de {len(l)} caracteres (máximo {MAX_HECHA}): una línea corta y el detalle en docs/historial/fase-NN.md.')
            if i < len(lineas) and lineas[i].startswith('  -'):
                hay.append(f'PLAN.md:{i} tarea hecha con sub-puntos: pasarlos a docs/historial/fase-NN.md.')

    limpio = sin_comentarios(plan)
    # Una fase sin nada pendiente ya no va en el plan.
    for titulo, cuerpo in re.findall(r'^## (Fase [^\n]*)\n(.*?)(?=^## |\Z)', limpio, re.M | re.S):
        if '- [x]' in cuerpo and '- [ ]' not in cuerpo:
            hay.append(f'PLAN.md: "{titulo}" ya no tiene nada pendiente: pasarla a docs/plan-hecho.md.')

    donde = DONDE.search(limpio)
    if donde and len([l for l in donde.group(1).split('\n') if l.strip()]) > MAX_DONDE:
        hay.append(f'PLAN.md: "Dónde quedamos" pasa de {MAX_DONDE} líneas: dejar solo qué se cerró y qué sigue.')
    return hay


def main():
    # El hook manda un JSON por la entrada. Corrido a mano no llega nada: sin esto se quedaría esperando para siempre.
    try:
        listo = select.select([sys.stdin], [], [], 1)[0]
        entrada = json.load(sys.stdin) if listo else {}
    except ValueError:
        entrada = {}
    raiz = os.environ.get('CLAUDE_PROJECT_DIR') or entrada.get('cwd') or os.getcwd()
    hay = problemas(raiz)
    if not hay:
        return 0
    texto = 'Aviso de orden:\n- ' + '\n- '.join(hay)
    if entrada.get('stop_hook_active'):
        # Claude ya tuvo su vuelta para arreglarlo: no volver a frenarlo (sin bucles), solo avisarle al usuario.
        print(json.dumps({'systemMessage': texto}))
        return 0
    print(texto + '\nArréglalo ahora siguiendo "Cómo se trabaja" en CLAUDE.md (sin perder información), o explícale al usuario por qué no.', file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
