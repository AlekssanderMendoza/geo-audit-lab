# Ronda 1 — Evidencia visual

## Alcance

Este directorio contiene 177 capturas de pantalla correspondientes a la primera ronda de observación del GEO Audit Lab de Coppel México.

- ChatGPT Search: 70 capturas correspondientes a 15 consultas.
- Gemini: 59 capturas correspondientes a 15 consultas.
- Perplexity: 48 capturas correspondientes a 15 consultas.

Estas capturas documentan las respuestas registradas durante el estudio. No constituyen observaciones adicionales: la Ronda 1 comprende 45 observaciones (15 consultas por 3 motores).

## Organización

- `chatgpt/`: capturas obtenidas de ChatGPT Search.
- `gemini/`: capturas obtenidas de Gemini.
- `perplexity/`: capturas obtenidas de Perplexity.
- `EVIDENCE-INDEX.csv`: índice de archivos con motor, ronda, identificador de consulta, secuencia, nombre, ruta dentro del repositorio y hash SHA-256.

## Trazabilidad

Cada captura se identifica mediante el motor, la ronda, el identificador de consulta y la secuencia registrados en `EVIDENCE-INDEX.csv`.

Las 70 capturas de ChatGPT Search proceden de los directorios originales de la sesión del 8 de octubre de 2026. Se copiaron al repositorio local sin modificar su contenido y se normalizaron los nombres de las copias, conservando intactos los originales.

En cuatro capturas de la consulta `DISC-01`, la secuencia se asignó según el orden cronológico de sus nombres originales de macOS. Este orden no debe interpretarse necesariamente como el orden de lectura de la respuesta.

Los valores SHA-256 permiten verificar la integridad de los archivos indexados.

## Controles de calidad

- Las 107 capturas originales de Gemini y Perplexity superaron las comprobaciones documentadas de existencia, correspondencia e integridad.
- Las 70 capturas de ChatGPT Search se compararon con sus archivos originales mediante SHA-256, sin discrepancias.
- Los 177 registros del índice R1 superaron la comprobación local de existencia, nombre, SHA-256 y unicidad de secuencia.
- El investigador confirmó visualmente que las cuatro capturas de ChatGPT Search correspondientes a `DISC-01` eran correctas y aptas para publicación.
- Las 70 capturas de ChatGPT Search fueron revisadas y aprobadas visualmente por el investigador; esta revisión no constituye una auditoría independiente.

## Limitaciones

- La revisión visual y los controles documentados no constituyen una validación independiente.
- Las capturas son evidencia observacional, no una demostración de reproducibilidad de las respuestas generativas.
- La integridad SHA-256 no demuestra la corrección de los indicadores GEO codificados manualmente.
- Este directorio documenta únicamente R1. R2 cuenta con evidencia en su propio directorio y R3 permanece pendiente.
- El estudio es exploratorio y no permite establecer conclusiones causales ni representativas del mercado.

## Publicación de evidencias

Este directorio amplía el paquete de evidencias de R1 originalmente asociado con la Entrega 02.1 del GEO Audit Lab de Coppel México.

Las 70 capturas de ChatGPT Search y sus registros de índice se han incorporado al repositorio local. Su revisión visual fue completada por el investigador, pero su publicación en GitHub continúa pendiente.

Las evidencias se organizan para facilitar la inspección y verificación independiente de los archivos registrados. Su publicación no implica una validación independiente de las decisiones de codificación del estudio.
