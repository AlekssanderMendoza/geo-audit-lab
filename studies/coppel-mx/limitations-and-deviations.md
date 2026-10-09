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
