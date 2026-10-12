# Coppel México — GEO Audit Lab

**Estudio:** GEO-COPPEL-001
**Mercado:** México
**Motores:** ChatGPT Search, Gemini y Perplexity
**Estado:** ronda 1 documentada; rondas 2 y 3 pendientes.

Investigación independiente y exploratoria sobre la visibilidad
de Coppel en respuestas generativas.

## Resultados de la ronda 1

Se registraron 45 observaciones: 15 consultas por motor,
con 12 consultas genéricas y 3 explícitas de marca por motor.

| Motor | Mención espontánea | Recomendación | Cita oficial |
|---|---:|---:|---:|
| ChatGPT Search | 10/12 (83.3 %) | 9/12 (75.0 %) | 4/12 (33.3 %) |
| Gemini | 8/12 (66.7 %) | 8/12 (66.7 %) | 5/12 (41.7 %) |
| Perplexity | 8/12 (66.7 %) | 8/12 (66.7 %) | 7/12 (58.3 %) |

Los porcentajes corresponden exclusivamente a consultas genéricas.

En las tres consultas explícitas de marca, cada motor registró
3 menciones, 0 recomendaciones y 3 citas.

Los indicadores no son mutuamente excluyentes.

## Datos y metodología

- [Dataset consolidado de la ronda 1](results-all-engines-r1.csv)
- [Resultados, procedencia y limitaciones](results-all-engines-r1.md)
- [Resultados históricos de ChatGPT — Entrega 01](results-chatgpt-r1.csv)
- [Protocolo original v1.0](protocol-v1.0.md)
- [Consultas originales](queries-v1.0.csv)
- [Diccionario de codificación](codebook.md)
- [Limitaciones y desviaciones](limitations-and-deviations.md)
- [Auditoría focalizada de citas](citation-audit.md)

## Interpretación

Los resultados describen las respuestas registradas durante
la primera ronda. No constituyen una muestra representativa
del comportamiento general de los motores en México.

Las diferencias observadas no demuestran significancia
estadística, causalidad ni estabilidad temporal.

La presencia de una cita al dominio oficial no garantiza
por sí sola que una afirmación esté respaldada.

Los indicadores no equivalen a participación de mercado,
ventas, tráfico o preferencia de consumidores.

## Auditoría de citas de la Entrega 01

La revisión focalizada confirmó la clasificación
`CRED-02: cited=true`, distinguiendo una fuente visible
del enlace comercial «Ver en Coppel».

La revisión está documentada en `citation-audit.md`,
con evidencia seleccionada en `evidence/`.

## Evidencia visual — Entrega 02.1

Se prepararon 107 capturas correspondientes a la ronda 1:

- Gemini: 59 capturas de 15 consultas.
- Perplexity: 48 capturas de 15 consultas.

Las imágenes cuentan con un índice que identifica el motor,
la consulta, la secuencia, la ruta y el hash SHA-256.

- [Consultar evidencia visual e índice](evidence/round-1/README.md)
- [Índice CSV de las 107 capturas](evidence/round-1/EVIDENCE-INDEX.csv)

El investigador realizó una revisión visual de legibilidad
y privacidad. Esta revisión no fue independiente.

Las capturas de ChatGPT no forman parte de la Entrega 02.1.
La revisión exhaustiva de la codificación de todas las
respuestas permanece pendiente.

Las rondas 2 y 3 no se han ejecutado.

## Independencia

Este proyecto no cuenta con aval de Coppel ni de los
proveedores de motores generativos.
