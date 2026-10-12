# Manifiesto de evidencia

El paquete público contiene documentación metodológica, resultados derivados y una captura seleccionada de CRED-02. Los archivos completos de respuestas y el archivo de 70 capturas no se distribuyen en esta versión por prudencia editorial y de privacidad.

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
- `studies/coppel-mx/results-all-engines-r1.csv` público: `389fc3333d8135c366d54e5830445275122e931df33bdd51eab2c41c08552dab`

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
