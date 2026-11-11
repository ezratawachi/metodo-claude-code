#!/usr/bin/env python3
# Aviso de inicio (hook SessionStart): le pasa a Claude "Dónde quedamos" de PLAN.md y avisa si hay trabajo
# fuera de la rama principal: ramas con commits que ella no tiene, otras copias (worktrees) o commits sin subir.
# Solo actúa en proyectos del método (un PLAN.md con "## Dónde quedamos"); en cualquier otra carpeta se calla.
# No usa internet (no hace git fetch): mira lo que ya está en esta compu.
import json, os, re, select, subprocess, sys

PARTIR = 'Antes de confirmar la próxima tarea con el usuario, revisa si se parte (2.1a, 2.1b) y propón cuáles van en esta sesión.'


def git(raiz, *args):
    try:
        r = subprocess.run(['git', '-C', raiz, *args], capture_output=True, text=True, timeout=5)
    except (OSError, subprocess.TimeoutExpired):
        return ''
    return r.stdout.strip() if r.returncode == 0 else ''


def donde_quedamos(raiz):
    try:
        with open(os.path.join(raiz, 'PLAN.md'), encoding='utf-8') as f:
            plan = f.read()
    except OSError:
        return None
    m = re.search(r'^## Dónde quedamos\n(.*?)(?=^## |\Z)', plan, re.M | re.S)
    if not m:
        return None
    return re.sub(r'<!--.*?-->\n?', '', m.group(1), flags=re.S).strip()


def fuera_de_principal(raiz):
    ramas = [r for r in git(raiz, 'for-each-ref', '--format=%(refname:short)', 'refs/heads', 'refs/remotes').split('\n') if r]
    principal = 'main' if 'main' in ramas else 'master' if 'master' in ramas else None
    if not principal:
        return []  # sin git o sin rama principal: nada que comparar
    remota = 'origin/' + principal
    avisos = []
    for rama in ramas:
        if rama in (principal, 'origin', 'origin/HEAD'):
            continue
        n = git(raiz, 'rev-list', '--count', f'{principal}..{rama}')
        if rama == remota:
            atras = git(raiz, 'rev-list', '--count', f'{remota}..{principal}')
            if atras and atras != '0':
                avisos.append(f'{principal} tiene {atras} commit(s) sin subir a GitHub.')
            if n and n != '0':
                avisos.append(f'{remota} tiene {n} commit(s) que {principal} no tiene.')
        elif n and n != '0':
            avisos.append(f'La rama {rama} tiene {n} commit(s) que no están en {principal}.')
    copias = [l[9:] for l in git(raiz, 'worktree', 'list', '--porcelain').split('\n') if l.startswith('worktree ')]
    for c in copias:
        if os.path.realpath(c) != os.path.realpath(raiz):
            avisos.append(f'Hay otra copia (worktree) en {c}.')
    return avisos


def main():
    try:
        listo = select.select([sys.stdin], [], [], 1)[0]
        entrada = json.load(sys.stdin) if listo else {}
    except ValueError:
        entrada = {}
    raiz = os.environ.get('CLAUDE_PROJECT_DIR') or entrada.get('cwd') or os.getcwd()
    d = donde_quedamos(raiz)
    if d is None:
        return 0  # no es un proyecto del método
    partes = ['Dónde quedamos (PLAN.md):\n' + d + '\n\n' + PARTIR] if d else []
    a = fuera_de_principal(raiz)
    if a:
        partes.append('Trabajo fuera de la rama principal (avisar al usuario antes de empezar):\n' + '\n'.join('- ' + x for x in a))
    if partes:
        print('\n\n'.join(partes))
    return 0


if __name__ == '__main__':
    sys.exit(main())
