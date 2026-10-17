import asyncio
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes.preprocessing_routes import router as preprocessing_router
from app.routes.prediction_routes import router as prediction_router

from app.core.config import settings


async def _wake(url: str) -> None:
    """Despierta un servicio dormido (planes gratis con arranque en frío) sin esperar su respuesta."""
    try:
        async with httpx.AsyncClient(timeout=180) as client:
            await client.get(f"{url}/docs")
    except httpx.HTTPError:
        pass


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Al abrirse el gateway se despiertan los otros dos servicios en paralelo,
    # para que no se encadenen tres arranques en frío al subir la primera imagen.
    tasks = [asyncio.create_task(_wake(url)) for url in (settings.PREPROCESSING_URL, settings.LATEX_RECOGNITION_URL)]
    yield
    for task in tasks:
        task.cancel()


app = FastAPI(lifespan=lifespan)

# Configurar FastAPI para servir archivos estáticos desde la carpeta /static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

#registrar rutas
app.include_router(preprocessing_router)
app.include_router(prediction_router)

# Ruta para la página de bienvenida
@app.get("/")
async def read_root():
    return FileResponse("app/static/index.html")
