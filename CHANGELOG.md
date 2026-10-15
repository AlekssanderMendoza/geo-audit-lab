# Historial de versiones

## Paquete público v1.0 — preparación
- Copia sin alteraciones del protocolo y preguntas originales.
- Exportación derivada de las 15 observaciones de ChatGPT Search, ronda 1.
- Diccionario de indicadores y documento de limitaciones.
- No se publican capturas ni respuestas íntegras en esta versión.

## v1.1 — Auditoría de evidencia
- Se revisaron las respuestas y capturas aportadas después del primer paquete.
- Se documentó la decisión de conservar la citación de CRED-02 como válida y se incorporó una captura puntual.
- Se actualizó el estado de disponibilidad de evidencias en las limitaciones, sin alterar protocolo, consultas ni resultados.

## v1.2 — Entrega 02 (12 de octubre de 2026)
- Se incorpora el dataset consolidado de la ronda 1: 45 observaciones, 15 por motor, de ChatGPT Search, Gemini y Perplexity.
- Se publican resultados descriptivos separados para las 12 consultas genéricas y las 3 consultas explícitas de marca de cada motor.
- Se documentan dos correcciones de clasificación de recomendación de Perplexity efectuadas durante la revisión de los datos.
- Se actualizan los README, el diccionario de codificación, las limitaciones metodológicas y el manifiesto de evidencia.
- Se conserva la discrepancia pendiente entre las huellas SHA-256 históricas y actuales de `observations.csv`.
- Los ZIP históricos de respuestas y capturas no pudieron verificarse nuevamente en el directorio del laboratorio.
- El protocolo v1.0, las 15 consultas originales y el dataset histórico de ChatGPT Search permanecen sin modificaciones.
- Las rondas 2 y 3 continúan pendientes; no se afirma representatividad, causalidad ni significancia estadística.

## Actualizaciones posteriores a v1.2 — 14 de octubre de 2026

### Evidencia visual de R1 — Entrega 02.1

- Se publicaron inicialmente 107 capturas: 59 de Gemini y 48 de Perplexity.
- Se incorporaron un README y un índice CSV con huellas SHA-256.
- En ese corte, las 70 capturas de ChatGPT Search R1 permanecían pendientes de incorporación.
- Actualización del 14 de octubre: las 70 capturas se incorporaron e indexaron localmente, se verificaron mediante SHA-256 y fueron aprobadas visualmente por el investigador.
- La publicación de esas 70 capturas en GitHub continúa pendiente de confirmación.

### Corte preliminar R1 + R2

- Se completó R2 con 45 observaciones adicionales.
- El estudio alcanzó 90 de las 135 observaciones previstas.
- Se publicó `results-all-engines-r2.csv` con 45 registros.
- Se mantuvo R3 como pendiente.
- Se estableció que la Entrega 03 presentará resultados preliminares, no conclusiones definitivas.

### Evidencia visual de R2

- Se publicaron 151 capturas: 54 de ChatGPT Search, 51 de Gemini y 46 de Perplexity.
- Se incorporaron un README y un índice CSV de evidencias.
- Se verificó mediante SHA-256 la correspondencia de los 151 archivos publicados con sus originales locales.
- La revisión visual realizada no constituye una auditoría independiente y exhaustiva.

### Actualización de navegación y documentación

- Se reorganizó la portada del repositorio y el índice técnico de Coppel.
- Se incorporaron enlaces a los resultados y evidencias de ambas rondas.
- Se actualizó el manifiesto general sin alterar sus hashes ni registros históricos.
- Se conservaron las limitaciones metodológicas y las discrepancias de integridad pendientes.
- No se modificaron el protocolo v1.0, las consultas originales ni los datasets.

### Preparación local de evidencias ChatGPT Search R1

- Se incorporaron localmente 70 capturas de ChatGPT Search correspondientes a R1.
- El inventario local de R1 pasó de 107 a 177 capturas: 70 de ChatGPT Search, 59 de Gemini y 48 de Perplexity.
- Se amplió `studies/coppel-mx/evidence/round-1/EVIDENCE-INDEX.csv` a 177 registros.
- Se verificaron la existencia, los nombres, las huellas SHA-256 y la unicidad de las secuencias del índice R1, sin errores detectados.
- Las 70 copias de ChatGPT Search conservaron su contenido original, comprobado mediante SHA-256.
- Las cuatro capturas de `DISC-01` recibieron secuencias basadas en las marcas temporales de sus nombres originales; estas no garantizan el orden de lectura de la respuesta.
- Se confirmó visualmente la correspondencia de las cuatro capturas de `DISC-01`.
- Al preparar esta incorporación local, permanecían pendientes de revisión visual las otras 66 capturas de ChatGPT Search R1.
- Posteriormente, el investigador revisó y aprobó visualmente esas 66 capturas, completando la revisión de las 70 capturas de ChatGPT Search R1.
- La revisión visual no constituye una auditoría independiente; la publicación en GitHub continúa pendiente.
- En el corte publicado anterior, el repositorio contenía 258 capturas. El inventario local preparado de R1 y R2 suma 328; la publicación de las 70 capturas adicionales de ChatGPT Search R1 sigue pendiente de confirmación.
- Se actualizaron las referencias documentales sin modificar el protocolo, las consultas ni los datasets.
