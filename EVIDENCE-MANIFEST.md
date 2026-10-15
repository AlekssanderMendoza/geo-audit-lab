# Manifiesto de evidencia

En el corte histórico documentado originalmente, el paquete público contenía documentación metodológica, resultados derivados y una captura seleccionada de CRED-02. En ese momento, los archivos completos de respuestas y el archivo de 70 capturas no se distribuían por prudencia editorial y de privacidad. El estado posterior de las evidencias de R1 se documenta en las actualizaciones fechadas al final de este manifiesto.

## Archivos originales inmutables

- `protocol-v1.0.md`: SHA-256 `69fe77997bbe30401fd15ea1045d3443b948f19970c7404e15870fb3ef64e1d8`
- `queries-v1.0.csv`: SHA-256 `a93a04151efaeede102eca86c5d1ebd5d5612575d2769b01daef57d4a91203e4`
- `observations.csv`: SHA-256 `f3a41713ea32206fb5ec1c7c1058c1b19cdfc5f462f1fff8dd06bd5db8f26a99`
- `responses.zip`: SHA-256 `81252bba55f0dedd17368df71f2ad8fbdb5048ab22aa3a5b70ad194ae024b10e`
- `screenshots.zip`: SHA-256 `6c9c90306a93b14032bfb4ca2d131bf0028ef74067f219d7c05f5c9cc82dff59`


## Actualización — Entrega 02 (12 de octubre de 2026)

Esta actualización incorpora la primera ronda consolidada de
ChatGPT Search, Gemini y Perplexity: 45 observaciones de las
135 previstas en el protocolo.

### Verificaciones SHA-256

- Protocolo v1.0: `69fe77997bbe30401fd15ea1045d3443b948f19970c7404e15870fb3ef64e1d8`
- Consultas v1.0: `a93a04151efaeede102eca86c5d1ebd5d5612575d2769b01daef57d4a91203e4`
- `data/raw/observations.csv` local actual: `2fb7834b82c62acc405e04b9972f20d18a545c134114573569ed66f0b7afa3e7`
- `data/processed/observations_round1_normalized.csv` local: `bbc97a28091ee8adb5b9c02db119c1124e4c8cb20a4db68379ec5eec04b1df02`
- `studies/coppel-mx/results-all-engines-r1.csv` público: `797a55e6b76277775c7e6bf2025bbaf92e41a2343def0c2048e9297644807759`

Las copias locales y del repositorio del protocolo y las
consultas coinciden byte por byte.

### Discrepancia histórica pendiente

El manifiesto de la Entrega 01 registra para
`observations.csv` la huella `f3a41713ea32206fb5ec1c7c1058c1b19cdfc5f462f1fff8dd06bd5db8f26a99`.

La única copia con ese nombre localizada dentro de
`~/Documents/GEO-Audit-Lab` tiene una huella diferente.
No se ha determinado la causa de esta discrepancia.

Los archivos `responses.zip` y `screenshots.zip` no se
localizaron dentro de ese directorio durante la comprobación.
Sus huellas históricas se conservan arriba, pero no pudieron
verificarse nuevamente.

### Alcance de la evidencia

El inventario de trabajo registra 45 archivos de respuestas
y 177 capturas PNG distribuidas entre los tres motores.
Este inventario no constituye una auditoría exhaustiva
de integridad, privacidad ni correspondencia de cada captura.

El dataset público consolidado es un archivo derivado.
No incluye respuestas completas, capturas ni metadatos
detallados de sesión.

Las rondas 2 y 3 permanecen pendientes.

---

## Actualización — Corte preliminar R1 + R2 (14 de octubre de 2026)

Esta sección actualiza el estado público del laboratorio sin sustituir
las verificaciones ni las declaraciones históricas anteriores.

### Observaciones

| Ronda | Observaciones | Estado |
|---|---:|---|
| R1 | 45 | Completada |
| R2 | 45 | Completada |
| R3 | 45 previstas | Pendiente |
| **Total registrado** | **90 de 135 previstas** | **Corte preliminar** |

Los resultados públicos consolidados están disponibles en:

- `studies/coppel-mx/results-all-engines-r1.csv`
- `studies/coppel-mx/results-all-engines-r2.csv`

Cada archivo contiene 45 observaciones y 11 columnas.

### Evidencia visual publicada

| Ronda | ChatGPT Search | Gemini | Perplexity | Total |
|---|---:|---:|---:|---:|
| R1 | 0 | 59 | 48 | 107 |
| R2 | 54 | 51 | 46 | 151 |
| **Total** | **54** | **110** | **94** | **258** |

Las capturas publicadas están organizadas en:

- `studies/coppel-mx/evidence/round-1/`
- `studies/coppel-mx/evidence/round-2/`

Cada ronda dispone de un archivo `EVIDENCE-INDEX.csv` y un README
que documentan el conjunto publicado.

En el corte histórico de esta sección, las 70 capturas de ChatGPT Search R1 identificadas en el laboratorio local permanecían pendientes de incorporación al repositorio público. Su incorporación local posterior y el estado de publicación se documentan en las actualizaciones fechadas al final de este manifiesto.

Existen además cuatro capturas seleccionadas directamente en
`studies/coppel-mx/evidence/`. Su clasificación por ronda y
procedencia específica requiere revisión documental.

### Verificaciones y límites

Las 151 capturas publicadas de R2 fueron contrastadas mediante
SHA-256 con sus correspondientes archivos originales locales
durante la preparación de la publicación.

Los índices por ronda permiten consultar las huellas registradas
para las capturas publicadas. La existencia de un hash no demuestra
por sí sola la autenticidad de la respuesta, la corrección de la
codificación ni la ausencia de información privada.

La revisión visual realizada no constituye una auditoría
independiente y exhaustiva.

### Discrepancias históricas

La discrepancia previamente documentada entre las huellas SHA-256
de `observations.csv` continúa sin explicación confirmada.

Las huellas históricas de `responses.zip` y `screenshots.zip`
se conservan en las secciones anteriores; su verificación
posterior no quedó acreditada en esa revisión.

Ninguno de esos registros históricos se sustituye por los
índices de evidencias publicados posteriormente.

### Estado editorial

Este corte corresponde a R1 + R2 y no al cierre del experimento.
La comparación descriptiva prevista para la Entrega 03 y la
tercera ronda permanecen pendientes.

---

## Actualización local — Incorporación de ChatGPT Search R1 (14 de octubre de 2026)

Esta sección documenta una ampliación local de las evidencias de R1.
No sustituye los inventarios históricos ni acredita su publicación en GitHub.

### Inventario local preparado

| Ronda | ChatGPT Search | Gemini | Perplexity | Total |
|---|---:|---:|---:|---:|
| R1 | 70 | 59 | 48 | 177 |
| R2 | 54 | 51 | 46 | 151 |
| **Total** | **124** | **110** | **94** | **328** |

Las 70 capturas adicionales de ChatGPT Search R1 se encuentran en
`studies/coppel-mx/evidence/round-1/chatgpt/`.

El índice `studies/coppel-mx/evidence/round-1/EVIDENCE-INDEX.csv`
contiene 177 registros, con rutas y huellas SHA-256 verificadas
contra los archivos locales.

### Procedencia y controles

- Las 70 capturas se copiaron desde los directorios originales de R1.
- Las copias conservaron su contenido, comprobado mediante SHA-256.
- Se normalizaron los nombres de las copias sin modificar los originales.
- Cuatro capturas de `DISC-01` recibieron secuencias basadas en el orden
  cronológico de sus nombres originales de macOS.
- La auditoría del índice R1 terminó con cero errores de existencia,
  nombre, integridad SHA-256 o duplicación de secuencias.
- El investigador confirmó visualmente las cuatro capturas de `DISC-01`.
- Posteriormente, revisó y aprobó visualmente las otras 66 capturas de ChatGPT Search R1.
- Las 70 capturas quedaron aprobadas visualmente por el investigador; esta revisión no constituye una auditoría independiente.

### Pendientes de publicación

- Completar la verificación final de los archivos y la documentación del repositorio.
- Publicar en GitHub las 70 capturas de ChatGPT Search R1 y el índice actualizado.
- Verificar la publicación mediante el commit y el repositorio remoto.

Las 328 capturas representan el inventario local preparado para R1 y R2,
no el total acreditado como publicado en GitHub en este corte.

Las discrepancias históricas de `observations.csv` y las verificaciones
pendientes de los archivos ZIP originales permanecen sin resolver.
