# Limitaciones, desviaciones y condiciones pendientes de verificación

**Referencia:** protocolo congelado el 8 de octubre de 2026. Las observaciones corresponden a la ronda 1 de ChatGPT Search.

## Confirmado en el registro aportado
- 15 de 15 consultas tienen una observación marcada `complete`, de las cuales 12 son genéricas y 3 son de marca.
- Solo `DISC-01` tiene inicio y fin documentados (`2026-10-08T14:20:49-06:00` y `2026-10-08T14:22:19-06:00`). Las otras 14 carecen de estos campos.
- Las primeras cuatro filas registran modo «Instant» sin versión exacta del modelo; las otras 11 dejan el campo de versión vacío.
- Los primeros cuatro registros indican personalización `unknown`; los restantes no registran ese dato.
- En una revisión posterior se aportaron `responses.zip` y `screenshots.zip`: se localizaron las 15 respuestas y capturas asociadas. La revisión de citas se documenta en `citation-audit.md`.
- El registro disponible no documenta semilla de aleatorización, ni permite confirmar el orden aleatorizado, las condiciones de nueva conversación por consulta o la comparabilidad horaria. **No se afirma que no se hayan aplicado**: su cumplimiento no pudo verificarse con los archivos examinados.

## Alcance
- El indicador primario del protocolo es la mención espontánea en consultas genéricas. Las métricas de recomendación y citación son complementarias.
- El protocolo completo prevé 135 ejecuciones; solo 15 corresponden a esta entrega.
- La comparación con cinco competidores y el SOV del panel **no se presentan** porque no se entregó codificación equivalente por competidor.
- La selección de preguntas es intencional y los resultados no son representativos del comportamiento general de ChatGPT Search en México.
- Las repeticiones futuras por consulta no deben tratarse como observaciones independientes. No se infiere causalidad ni efecto en ventas.

## Pendiente antes de publicar como evidencia completa
1. Completar una auditoría exhaustiva de las 15 respuestas y todas las capturas si se requiere certificación integral; se realizó revisión focalizada de citaciones.
2. Registrar en documento separado las desviaciones efectivas que puedan verificarse, sin alterar el protocolo original.
3. Revisar privacidad, derechos de terceros y posible información de sesión en cualquier captura pública.
4. Si se publican extractos, vincularlos por `query_id` y documentar cualquier edición o anonimización.

## Actualización — Entrega 02 (12 de octubre de 2026)

Esta sección amplía el alcance a ChatGPT Search, Gemini y
Perplexity. Las secciones anteriores se conservan como
registro histórico de la Entrega 01.

### Cobertura

- Ronda 1: 45 observaciones registradas.
- Cada motor: 12 consultas genéricas y 3 de marca.
- Rondas 2 y 3: pendientes.
- El total previsto por el protocolo sigue siendo 135.

### Comparabilidad entre motores

Se utilizaron las mismas 15 consultas, pero no se ha
verificado la equivalencia de todas las condiciones de
ejecución entre plataformas.

Las diferencias de interfaz, recuperación de fuentes,
configuración y personalización pueden afectar las respuestas.
No se atribuyen causalmente los resultados a un motor.

### Codificación y revisión

Los indicadores de mención, recomendación y cita no son
mutuamente excluyentes.

Durante la revisión de los datos consolidados se corrigieron
dos clasificaciones de recomendación correspondientes a
Perplexity. El dataset público refleja las clasificaciones
revisadas.

Esta revisión no equivale a una validación independiente
y exhaustiva de las 45 respuestas.

### Evidencia y trazabilidad

El inventario de trabajo identifica 45 archivos de respuestas
y 177 capturas PNG. No se ha completado una auditoría
exhaustiva de correspondencia, integridad y privacidad.

La discrepancia entre las huellas históricas y actuales de
`observations.csv`, así como la falta de verificación reciente
de los ZIP históricos, se documentan en `EVIDENCE-MANIFEST.md`.

### Interpretación

Los resultados son descriptivos y se limitan a las consultas
y ejecuciones registradas.

No constituyen una muestra representativa, ni permiten
inferir significancia estadística, causalidad, estabilidad
temporal, ventas o participación de mercado.

La presencia de una cita al dominio oficial no demuestra
por sí sola que una afirmación esté respaldada.

## Actualización — Corte preliminar R1 + R2 (14 de octubre de 2026)

Esta sección amplía el estado del experimento sin sustituir
las limitaciones documentadas en las entregas anteriores.

### Cobertura y estado

- R1: 45 observaciones completas.
- R2: 45 observaciones completas.
- Total registrado: 90 observaciones.
- Motores: ChatGPT Search, Gemini y Perplexity.
- Consultas: 15 por motor y ronda; 12 genéricas y 3 de marca.
- R3: pendiente, con 45 observaciones previstas.
- Total previsto al completar el protocolo: 135 observaciones.

Este corte es preliminar y no representa el cierre del estudio.

### Integridad de datos

Los archivos normalizados de R1 y R2 contienen 23 campos
y fueron reconciliados con el registro maestro actual,
sin diferencias en los valores comparados después de
normalizar las representaciones booleanas.

Los archivos públicos de resultados utilizan 11 columnas.
El CSV de R2 fue generado a partir del archivo normalizado
y del catálogo de consultas, conservando la estructura de R1.

Se verificaron 45 combinaciones únicas de motor y consulta
por ronda, sin diferencias entre los cuatro campos de R2
contrastados con su fuente normalizada.

Estas comprobaciones no sustituyen una auditoría independiente
de las decisiones de codificación.

### Evidencia local

Se localizaron 90 archivos de respuestas, uno por observación.

La comprobación automática identificó imágenes asociadas
a las 45 observaciones de R1 y las 45 de R2.

En los directorios locales examinados se contabilizaron
177 imágenes candidatas de R1 y 151 de R2.

La asociación se verificó mediante rutas, directorios
y convenciones de nombres. No constituye una revisión
visual exhaustiva del contenido, legibilidad o privacidad
de cada captura.

Estas cantidades describen evidencia local y no implican
que todas las imágenes estén publicadas en GitHub.

### Comparabilidad e interpretación

Las dos rondas utilizan las mismas combinaciones de motor
y consulta. Sin embargo, no se ha demostrado equivalencia
completa de las condiciones de ejecución ni independencia
estadística entre repeticiones.

Las diferencias entre rondas deben describirse como cambios
observados en este conjunto de ejecuciones, sin atribuirles
causalidad ni estabilidad temporal.

La tasa de mención espontánea en consultas genéricas
permanece como indicador principal. Recomendación y cita
son indicadores complementarios.

No se infiere significancia estadística, representatividad,
participación de mercado, ventas ni tráfico.

### Pendientes

- Ejecutar y auditar R3.
- Revisar de forma exhaustiva las decisiones de codificación.
- Completar la revisión visual y de privacidad antes de
  publicar nuevas capturas.
- Preparar índices y manifiestos verificables de R2.
- Mantener documentadas las discrepancias históricas
  de integridad y procedencia que aún no estén resueltas.
