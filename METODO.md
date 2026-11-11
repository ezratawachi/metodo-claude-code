# Nuestro método de trabajo — versión 2

Sale de una tienda online real (del 26 de octubre al 9 de noviembre de 2026, 17 fases y ~390 commits; entregada a la clienta y con pedidos reales).
Sale de **un solo proyecto**: el próximo es la prueba de verdad. Hay que mantenerlo chico y que cada proyecto lo ajuste.

Tiene 3 capas:
- **A. Cómo trabajar con el usuario.** Son sus reglas de conversación en `~/.claude/CLAUDE.md` y pasan solas a cualquier proyecto (ver el punto 4). Para otra persona hay una plantilla en `reglas/CLAUDE.md`.
- **B. El núcleo.** Sirve para cualquier proyecto (punto 1).
- **C. Lo propio de cada proyecto.** Su `CLAUDE.md`, su contexto y sus comandos.

Además hay secciones por tipo de proyecto. Hoy existe solo **"Si es una web"** (punto 2). Las de otros tipos se escriben cuando hagamos uno de verdad.

---

## 1. El núcleo (cualquier proyecto)

### Al empezar
1. **Contexto.** Antes de diseñar, escribir `docs/contexto.md`: para quién es, qué necesita, cómo funciona hoy, marca y tono, y lo que no se puede decir.
   Que salga de fuentes reales (por ejemplo, el Instagram del negocio), con lo que falte anotado como "**Falta**".
2. **Elegir el stack.** Nada de "el de moda":
   - Primero escribir **qué necesita el proyecto**: costo (¿gratis? ¿permite uso comercial?), qué tiene que hacer, quién lo usa y quién lo mantiene, y los límites de los planes gratis (pausas, topes).
   - Después research con fuentes y comparar 2–3 opciones con precios reales.
   - La elegida va a `docs/decisiones.md` con su porqué.
   - Lo mismo cada vez que entra una pieza nueva (correo, pagos…).
3. **Plan.** `PLAN.md` con todas las fases, de inicio a entrega. Lo no definido va como tarea de "definir X" dentro de su fase, así siempre hay un siguiente paso. El plan es un mapa, no un contrato: fases y tareas se suman, mueven o parten en el camino, y las lejanas pueden tener tareas gruesas que se parten al llegar.
4. **`CLAUDE.md` del proyecto.** Solo datos fijos, comandos y reglas propias. Máximo 5 KB. Las decisiones no van aquí.
5. **Avisos automáticos.** Los dos hooks (ver "Las piezas") desde el primer día.

### Cada sesión
- El usuario dice **"seguimos con el plan"**. Claude lee "Dónde quedamos" y hace **solo la próxima tarea**: una sesión, una tarea.
- Si una tarea es grande, se parte (4a, 4b) y se dice cuál toca en esta sesión.
- Toda decisión de diseño pasa primero por un research con fuentes y una recomendación. El usuario aprueba diciendo "sí" y "no ahora".

### Al cerrar una tarea
1. Marcarla en `PLAN.md` en **una línea**, con la fecha.
2. Poner el detalle (qué se hizo, con qué y cómo se probó) **arriba de todo** del archivo de su fase en `docs/historial/`.
3. Corregir los documentos que hayan cambiado: decisiones y, en una web, el mapa y la guía de problemas.
4. Dejar "Dónde quedamos" en 2–3 líneas.
5. Juntar con `main`, subir y publicar con el OK del usuario. **La tarea no está lista hasta que está en `main`.**

### Al cerrar una fase
- Sus líneas pasan de `PLAN.md` a `docs/plan-hecho.md`.
- Se revisa el `CLAUDE.md` del proyecto con los pasos del skill `claude-md-improver` (plugin oficial `claude-md-management`).

### Las piezas

| Pieza | Para qué | Desde |
|---|---|---|
| `PLAN.md` | **Solo lo pendiente.** Arriba "Dónde quedamos" (máx. 4 líneas). Después las fases con tareas numeradas, "Al publicar" y "Para después" (solo lo que el usuario mandó ahí) | El día 1 |
| `docs/decisiones.md` | Tabla: fecha, decisión, por qué. Si una cambia, se corrige su fila | El día 1 |
| `docs/historial/` | Cómo se hizo cada cosa, un archivo por fase, más un índice | El día 1 (al principio basta un solo archivo) |
| `docs/contexto.md` | El punto 1 de "Al empezar" | El día 1 |
| `docs/research-*.md` | Un research con fuentes por cada decisión grande | Cuando haya una decisión |
| `docs/skills-y-librerias.md` | Lo que ya se buscó (con find-skills y en la web), para no buscarlo dos veces | El día 1 |
| `docs/plan-hecho.md` | Las fases cerradas | Al cerrar la primera fase |
| **Aviso de orden** (hook `Stop`) | Al final de cada respuesta avisa si `PLAN.md` pasa de 10 KB, `CLAUDE.md` de 5 KB, una tarea hecha ocupa más de una línea, una fase ya no tiene nada pendiente o "Dónde quedamos" pasa de 4 líneas | El día 1 |
| **Aviso de inicio** (hook `SessionStart`) | Le pasa a Claude "Dónde quedamos" y avisa si hay ramas, copias o commits fuera de `main` | El día 1 |

Los dos avisos generales son `hooks/aviso-orden.py` y `hooks/aviso-inicio.py` de este repo. Viven en el plugin (una sola copia para todos los proyectos) y no dicen nada en carpetas sin un `PLAN.md` con "Dónde quedamos".

### Antes y después de entregar
- **Antes:** todo lo creado al probar es de prueba y se borra junto.
- **Después:** todo es real y no se borra nada sin el OK del usuario. Se anota en la memoria del proyecto el día que se entrega.
- **Fase de seguridad obligatoria antes de entregar**, si el proyecto maneja datos de personas o dinero: un `SEGURIDAD.md` con su propia lista. Va al final, cuando el código ya no cambia.

---

## 2. Si es una web

### Receta probada (punto de partida, no copia)
**Astro + Cloudflare Workers + base D1.** En esa tienda se eligió porque:
- es gratis y permite uso comercial (Vercel gratis lo prohíbe);
- tiene un servidor propio, que hacía falta para que los pagos no se pudieran falsificar;
- no se apaga solo por poco uso, como pasa con Supabase o Netlify gratis;
- dejó hacer un panel propio para la dueña sin pagar Shopify.

Piezas que se sumaron con el mismo criterio:
- **Resend** para los correos: gratis, 3.000 al mes y 100 al día.
- **Cloudflare Access** para cerrar el panel.
- **Turnstile** contra robots.
- **Email Workers** para leer los correos de pago.

**En cada web nueva, revisar la receta con la lista del paso "Elegir el stack".** Si el proyecto necesita otra cosa, se cambia.

### Piezas que suma una web

| Pieza | Para qué | Desde |
|---|---|---|
| `docs/mapa.md` | Una fila por pantalla: lo que se ve, lo que se mueve o se toca y qué archivos la hacen. **Se lee antes de proponer o cambiar algo** | Cuando haya pantallas |
| Comentario arriba de cada archivo | Qué hace el archivo. El aviso de orden revisa que esté y que el mapa lo nombre | Desde el primer archivo |
| `npm run revisar` | Red de seguridad antes de publicar: tipos, build y que las páginas abran (y que las privadas den 403) | Cuando haya código |
| `docs/problemas.md` | Qué hacer cuando algo falla en vivo: cómo darse cuenta, dónde mirar y cómo arreglarlo | Al publicar |
| `.claude/launch.json` | El servidor local, para probar en el navegador integrado | Desde el primer código |

### Fases propias de una web
- **Identidad visual** al principio: 2–3 direcciones de prueba, elegir una (a veces gana una mezcla).
- **R, revisión visual:** una pasada a todo con ojo de diseño antes de entregar.
- **S, seguridad:** la del núcleo, con los skills security-review y security-and-hardening.
- **Publicar:** dominio, Google (solo las páginas públicas) y una lista de "Al publicar".

---

## 3. Lo que ya existe afuera (research del 2026-11-09)
- **GitHub Spec Kit:** una "constitución" (las reglas del proyecto), después spec, plan y tareas. Es lo más parecido a lo nuestro.
- **BMAD Method:** un "equipo" de ~21 agentes. Es pesado y se basa en agentes, que este método no usa: no sirve.
- **Agent OS:** estándares de código que se repiten entre proyectos.
- **El patrón "archivo de progreso":** cada sesión lee el estado y lo actualiza al terminar. Es nuestro "Dónde quedamos".
- **Plugins de Claude Code:** juntan skills y hooks en un solo paquete que se instala desde una carpeta o un repo propio. Dos detalles:
  - Un `CLAUDE.md` dentro del plugin no se carga solo.
  - Cada skill instalado ocupa contexto en todas las sesiones. Con el plan Pro conviene uno solo y corto.

**Lo que tenemos y ellos no:** las reglas de conversación de la capa A, las decisiones con su porqué y los avisos automáticos que mantienen el orden.

## 4. Lecciones que ya están en la capa A
Desde el 2026-11-09, en `~/.claude/CLAUDE.md`:
- hablar en pasos y no en días;
- nada a "para después" si el usuario no lo dijo;
- research antes de recomendar;
- el orden MCP o skill → navegador integrado → el usuario;
- gastar menos uso;
- antes y después de entregar;
- find-skills antes de hacer algo a mano.
