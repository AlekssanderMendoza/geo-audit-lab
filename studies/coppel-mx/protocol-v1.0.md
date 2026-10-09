# GEO Audit Lab — Coppel México
## Protocolo preregistrado v1.0 (2026-10-08)
Estado: diseño cerrado; no se han recolectado respuestas.

### Pregunta
¿Cuál es la tasa observada de mención espontánea de Coppel frente a cinco competidores en 12 consultas comerciales genéricas predefinidas del retail mexicano, ejecutadas en ChatGPT Search, Gemini y Perplexity?

### Decisiones
- DEC-001: indicador primario tasa de mención espontánea; 15 consultas.
- DEC-002: 12 genéricas (primarias), 3 con marca (secundarias); consultas congeladas en queries-v1.0.csv.
- DEC-003: codificación manual con validación automatizada; sentimiento exploratorio.
- DEC-004: 3 días, una ejecución por consulta y motor por día; sesión habitual documentada; conservar respuesta íntegra, captura y metadatos.

### Diseño
3 motores × 15 consultas × 3 días = 135 ejecuciones previstas; 108 genéricas y 27 de marca. La unidad de observación es una respuesta; repeticiones por consulta no se tratan como independientes. Canal web es principal; API/Python es estudio separado. Competidores fijos: Elektra, Liverpool, Walmart, Mercado Libre y Amazon; registrar otras marcas espontáneas.

### Indicadores
MR = respuestas genéricas válidas que mencionan explícitamente Coppel / respuestas genéricas válidas. Reportar por motor, categoría y global descriptivo con ponderación indicada. CR = respuestas válidas con cita de respaldo a dominio oficial coppel.com / respuestas válidas. RR = respuestas válidas que proponen Coppel como alternativa adecuada / respuestas válidas. SOV = respuestas con mención de Coppel / suma de respuestas con mención de cada marca del panel (máximo 1 por marca y respuesta). Desglosar consultas genéricas y de marca.

### Codificación
No contar marca presente solo en prompt, URL, título de fuente o panel lateral como mención en texto. Cita solo cuando se presente como fuente o respaldo, no enlaces comerciales/navegacionales. Recomendación requiere propuesta explícita como opción adecuada; mención descriptiva no basta. Sentimiento positivo/neutral/negativo/mixto; exploratorio. Campos no evaluables son null, no false. Guardar fuentes y enlaces en tabla secundaria.

### Ejecución
Registrar configuración de cuenta, personalización conocida, idioma, país, navegador, motor, modalidad de búsqueda, versión de modelo si visible, hora de inicio y fin con zona horaria, estado, respuesta íntegra, captura y URLs. Nueva conversación por ejecución. Ejecutar una ronda diaria por tres días, con orden aleatorizado mediante semilla fija registrada y horarios comparables. Documentar desviaciones y fallos; no sustituir consultas tras ver respuestas.

### Validación
Un registro por ejecución programada, sin IDs duplicados; integridad de evidencias; revisión manual de ambigüedades; dominios normalizados; registrar ausentes. Umbral operativo de 95% de respuestas válidas: si no se cumple, investigar y reportar; no ocultar fallos. Los resultados no son representativos de todas las consultas de México ni demuestran causalidad. No se han observado resultados todavía.

### Transparencia y publicación
Estudio independiente sin aval de Coppel. Conservar respuestas completas en repositorio privado de trabajo; publicar metodología, datos derivados y extractos permitidos, no necesariamente textos íntegros de terceros. Publicar desviaciones y resultados negativos.
