# Coppel México — GEO Audit Lab

**Estudio:** GEO-COPPEL-001
**Mercado:** México
**Motores:** ChatGPT Search, Gemini y Perplexity
**Estado:** rondas 1 y 2 completadas (90 observaciones); ronda 3 pendiente.

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

La ronda 2 se completó posteriormente. La ronda 3 permanece pendiente.

## Corte preliminar — R1 + R2 (14 de octubre de 2026)

Se completaron dos rondas con las mismas 15 consultas
en ChatGPT Search, Gemini y Perplexity.

| Ronda | Observaciones | Estado |
|---|---:|---|
| R1 | 45 | Completa |
| R2 | 45 | Completa |
| R3 | 45 previstas | Pendiente |
| **Total registrado** | **90** | **Corte preliminar** |

El protocolo completo contempla 135 observaciones.

### Datos de la segunda ronda

- [Resultados consolidados de R2](results-all-engines-r2.csv)
- [Resultados consolidados de R1](results-all-engines-r1.csv)
- [Limitaciones y desviaciones actualizadas](limitations-and-deviations.md)

Ambos archivos de resultados contienen 45 registros,
15 consultas por motor y 11 columnas equivalentes.

Las 90 observaciones fueron reconciliadas con el
registro maestro actual del laboratorio.

### Alcance de la comparación

Este corte permite describir los cambios observados
entre dos ejecuciones de las mismas consultas.

La tasa de mención espontánea en consultas genéricas
continúa siendo el indicador principal.

Las diferencias entre rondas no demuestran estabilidad
temporal, significancia estadística ni causalidad.

La revisión independiente y exhaustiva de la codificación
permanece pendiente.

### Evidencia y próximos pasos

En el laboratorio local se localizaron 90 archivos de
respuesta y asociaciones automáticas con capturas para
las 90 observaciones.

La evidencia visual de R2 requiere revisión de privacidad,
índice verificable y preparación para publicación.

La tercera ronda todavía no se ha ejecutado.

La Entrega 03 corresponde a un análisis preliminar de
R1 + R2 y no al cierre definitivo del experimento.

## Independencia

Este proyecto no cuenta con aval de Coppel ni de los
proveedores de motores generativos.
