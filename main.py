from fastapi import FastAPI#, Request, APIRouter
#from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
#from fastapi.templating import Jinja2Templates
from router.user import user

app = FastAPI()

app.include_router(user)

# Configurar el directorio de plantillas
#templates = Jinja2Templates(directory="templates")

# Configurar el directorio de archivos estáticos (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Definir una ruta para servir el HTML
#@app.get("/", response_class=HTMLResponse)
#async def read_root(request: Request):
#    return templates.TemplateResponse("index.html", {"request": request})
