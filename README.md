# metodo

Una forma de trabajar con Claude Code por fases. Sale de una tienda online real, hecha de principio a fin con Claude Code y entregada con pedidos reales.

Es un plugin de Claude Code. Trae:

- **El skill `empezar`:** arranca un proyecto nuevo. Pregunta lo básico, copia las plantillas (`PLAN.md`, `CLAUDE.md`, `docs/`), escribe el contexto desde fuentes reales y elige el stack con research.
- **Dos avisos automáticos:** al abrir una sesión, Claude recibe "Dónde quedamos" del plan y un aviso si hay ramas, copias o commits fuera de `main`. Al terminar, avisa si el plan creció de más o si una fase ya está cerrada.

Los avisos solo hablan en carpetas que tienen un `PLAN.md` con "Dónde quedamos". En el resto no hacen nada.

El método completo está en [`METODO.md`](METODO.md).

## Instalar

Se instala una sola vez por computador. Necesitas Claude Code y `python3`.

```bash
claude plugin marketplace add ezratawachi/metodo-claude-code
```

```bash
claude plugin install metodo@metodo
```

Los cambios se ven al abrir una sesión nueva.

## Usar

1. Crea una carpeta vacía y abre Claude Code ahí.
2. Escribe `/metodo:empezar` (en el menú basta con `/empezar` para encontrarlo).
3. En cada sesión siguiente, escribe `seguimos con el plan`.

## Tus reglas de conversación (opcional)

[`reglas/CLAUDE.md`](reglas/CLAUDE.md) es una plantilla de cómo quieres que Claude te hable y trabaje contigo. Cópiala a `~/.claude/CLAUDE.md` y cámbiala a tu gusto. Si ya tienes ese archivo, junta los dos.

## Actualizar

```bash
claude plugin marketplace update metodo && claude plugin update metodo@metodo
```

## Licencia

MIT. Ver [`LICENSE`](LICENSE).
