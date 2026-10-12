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
