---
name: empezar
description: Arranca un proyecto nuevo con el método. Pregunta lo básico, copia las plantillas (PLAN.md, CLAUDE.md, docs/), escribe el contexto desde fuentes reales y elige el stack con research. Usar cuando el usuario diga "empezar", "empecemos un proyecto", "proyecto nuevo", "arranquemos con el método" o abra una carpeta vacía para algo nuevo. No usar si la carpeta ya tiene un PLAN.md con "Dónde quedamos": ahí se sigue con el plan.
---

# Empezar un proyecto

Deja una carpeta lista para trabajar con el método: plantillas copiadas, contexto escrito, stack elegido y un plan con la primera fase. Todo en una sesión, con las paradas marcadas abajo.

Las plantillas están en `../../plantillas/` y el método completo en `../../METODO.md` (las dos rutas se cuentan desde la carpeta de este skill). No leas `METODO.md` entero: solo la parte "Si es una web" si el proyecto es una web.

## Antes de tocar nada

Mira la carpeta. Si ya hay un `PLAN.md` con "Dónde quedamos", para y dile al usuario que este proyecto ya empezó. Si hay otros archivos, dile cuáles viste y pregunta si se sigue aquí: no pises nada.

## Paso 1 — Lo básico

Pregunta de a una, con un ejemplo concreto y 2–3 opciones cuando ayude. Lo que el usuario ya dijo no se vuelve a preguntar.

1. Nombre del proyecto.
2. Para quién es y qué necesita, en una o dos frases suyas.
3. De dónde sale el contexto real: redes, una web vieja, documentos, una charla con la persona.
4. Si es una web o es otra cosa.

Repite las respuestas en una lista corta y espera el "sí" antes de seguir.

## Paso 2 — Copiar las plantillas

Copia el contenido de `../../plantillas/` a la raíz del proyecto, con la misma estructura (`PLAN.md`, `CLAUDE.md`, `docs/`). Pon el nombre del proyecto donde dice "(nombre del proyecto)" o "(Nombre del proyecto)". Los demás paréntesis se llenan en los pasos que siguen; los comentarios `<!-- -->` se quedan, porque explican cómo se usa cada archivo.

Si la carpeta no es un repo de git, pregunta si lo creas: los avisos automáticos miran las ramas y sin git no pueden.

## Paso 3 — Contexto

Llena `docs/contexto.md` leyendo las fuentes del paso 1. Va antes del stack y del diseño porque todo lo demás sale de aquí.

- Solo lo que diga la fuente. Las frases textuales van entre comillas.
- Lo que no se sabe va en "**Falta**", con a quién preguntarle. No se inventa nada para llenar un título.
- Arriba, la fuente y la fecha de la revisión.

Muéstrale al usuario un resumen corto y la lista de "Falta", y espera su OK.

## Paso 4 — Stack

Nada de "el de moda": se elige por lo que el proyecto necesita.

1. **Qué necesita el proyecto.** Escríbelo primero: costo (¿gratis?, ¿permite uso comercial?), qué tiene que hacer, quién lo usa, quién lo mantiene y qué límites de planes gratis molestarían (pausas, topes). Confírmalo con el usuario.
2. **Buscar antes de armar.** Busca skills con find-skills y librerías en la web, y anota lo visto en `docs/skills-y-librerias.md`. Antes de instalar un skill, pregunta.
3. **Research.** Compara 2–3 opciones con precios reales de las páginas oficiales y la fecha en que se miraron. Guárdalo en `docs/research-stack.md` con los enlaces. Si es una web, la receta de "Si es una web" es un punto de partida a comparar, no una copia.
4. **Recomendación.** Una opción, con su razón en dos líneas. El usuario aprueba con "sí apruebas" o "no ahora".
5. **Anotar.** La elegida va a la fila de `docs/decisiones.md` con su porqué y lo descartado, y a "Datos fijos" de `CLAUDE.md`.

Si el usuario dice "no ahora", el research queda guardado y elegir el stack pasa a ser la tarea 1.1 del plan.

## Paso 5 — Plan y cierre

- `PLAN.md`: propón la Fase 1 con pocas tareas numeradas y espera el OK. Solo las fases que se ven claras; "Para después" queda vacío, porque ahí solo entra lo que el usuario manda.
- "Dónde quedamos": qué se cerró en esta sesión, con fecha, y cuál es la próxima tarea.
- `CLAUDE.md`: la línea de qué es y para quién, y las reglas propias que salgan del contexto (por ejemplo, lo que no se puede decir). Si no hay comandos todavía, la sección queda con su comentario.
- GitHub: pregunta si se crea un repo. Si sí, va a "Datos fijos" de `CLAUDE.md`; si no, esa línea dice "GitHub: todavía no".
- `docs/historial.md` y `docs/historial/fase-1.md`: el nombre de la fase.
- Líneas de ejemplo que quedaron sin llenar (como `(comando)` en `CLAUDE.md` o `## 1.1 — (qué se hizo)` en el historial): se borran. El comentario de al lado ya explica el formato.
- Los dos avisos (orden e inicio) vienen con el plugin y empiezan a hablar solos cuando existe el `PLAN.md`: no se copia nada al proyecto.
- Si hay git, propón el primer commit y espera el OK.

Cierra con un resumen de unas 4 líneas: lo que quedó hecho, lo que falta y lo que decide el usuario.
