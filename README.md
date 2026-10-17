# LaTexIA

Sistema de reconocimiento y conversión de ecuaciones a LaTeX, organizado como microservicios en un solo repositorio.

| Carpeta | Servicio |
|---|---|
| `LaTexIA-Gateway/` | Gateway de la API |
| `preprocessing-service/` | Preprocesamiento de imágenes |
| `ocr-service/` | OCR |
| `latex-recognition-service/` | Reconocimiento de LaTeX |
| `frontend-ui/` | Interfaz web |

Cada carpeta conserva el historial de commits de su repositorio original (organización LaTexIA, 2025-03).

## Despliegue

Los tres servicios corren en Render (plan gratis, definidos en `render.yaml`):

| Servicio | URL |
|---|---|
| Gateway con la interfaz | https://latexia-gateway.onrender.com |
| Preprocesamiento | https://latexia-preprocessing.onrender.com |
| Reconocimiento | https://latexia-recognition.onrender.com |

Con el plan gratis los servicios se duermen tras ~15 minutos sin tráfico y el primer arranque tarda cerca de un minuto; el gateway despierta a los otros dos en paralelo al abrirse la página.
