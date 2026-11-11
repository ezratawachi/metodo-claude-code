# (Nombre del proyecto)

(Una línea: qué es, para quién y quién lo hace.)
<!-- Máximo 5 KB. Solo datos fijos, comandos y reglas propias. Las decisiones van en docs/decisiones.md. -->

## Cómo se trabaja
- **Plan:** `PLAN.md` tiene solo lo pendiente. Si el usuario dice "seguimos con el plan", leer "Dónde quedamos" y hacer solo la próxima tarea. Antes de empezarla, ver si se parte: cuando hay una decisión del usuario en medio (ej.: "armar 3 direcciones" y después "elegir una") o partes que se cierran solas (un research, una pantalla). Si a la mitad crece, parar y partirla ahí. Las sub-tareas aprobadas reemplazan la línea original en `PLAN.md` y cada una se cierra como una tarea normal.
- **Al cerrar una tarea:** marcarla en `PLAN.md` en una línea con la fecha; anotar el detalle (qué se hizo, con qué, cómo se probó) arriba de todo en `docs/historial/fase-NN.md` y en el índice `docs/historial.md`; corregir los documentos que cambiaron; dejar "Dónde quedamos" en 2–3 líneas; juntar con `main`, subir y publicar con el OK del usuario. La tarea no está lista hasta que está en `main`.
- **Al cerrar una fase:** sus líneas pasan a `docs/plan-hecho.md` y se revisa este archivo con los pasos del skill `claude-md-improver` (plugin oficial `claude-md-management`).
- **Cada dato en un solo lugar:** decisiones en `docs/decisiones.md` (si una cambia, se corrige su fila); cómo se hizo cada cosa en `docs/historial/`; para quién es y el tono en `docs/contexto.md`; comandos y datos fijos aquí.
- **Avisos automáticos:** el hook `Stop` avisa si un archivo se pasa de tamaño o "Dónde quedamos" se alarga: arreglarlo en el momento. El hook `SessionStart` pasa "Dónde quedamos" y las ramas, copias o commits fuera de `main`: si avisa algo, decírselo al usuario antes de empezar.
- **Skills:** al empezar cada fase, buscar skills y librerías antes de hacer algo a mano (lo ya visto: `docs/skills-y-librerias.md`).
<!-- Reglas propias del proyecto (lo que no se puede decir, entregas, seguridad…) van como viñetas aquí. -->

## Datos fijos
<!-- Stack, repo de GitHub, dominio, direcciones en vivo y de prueba, cuentas. Solo lo que no cambia seguido. -->
- (stack)
- GitHub: (repo)

## Comandos
<!-- Los corre Claude, no el usuario. Uno por línea, con para qué sirve. -->
- `(comando)`: (para qué)
