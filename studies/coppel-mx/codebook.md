# Diccionario de codificación — GEO-COPPEL-001

Fuente: protocolo-v1.0, apartado Codificación e Indicadores.

- **coppel_mentioned:** `true` cuando Coppel aparece explícitamente en el texto de la respuesta. No cuentan apariciones solo en el prompt, URL, título de fuente o panel lateral.
- **coppel_recommended:** `true` cuando se propone explícitamente Coppel como alternativa adecuada; una mención descriptiva no basta.
- **coppel_cited:** `true` cuando coppel.com figura como fuente o respaldo de una afirmación; no cuentan enlaces comerciales o de navegación.
- **false:** el indicador fue evaluado y no se observó; **vacío / null:** no evaluable o no registrado, según el campo.
- Los tres indicadores **no son mutuamente excluyentes**.
- **generic:** consulta que no nombra Coppel; se utiliza para la tasa primaria de mención espontánea. **brand:** consulta que nombra explícitamente Coppel; se reporta aparte.
- Cada fila representa una respuesta registrada de ChatGPT Search en la ronda 1.
- **No** confundir la ausencia de una recomendación con una valoración negativa de la marca.
- Los resultados reflejan codificación manual documentada en `observations.csv`; este paquete no incluye una auditoría independiente de todas las respuestas originales.
