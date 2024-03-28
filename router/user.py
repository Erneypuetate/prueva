from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

user=APIRouter()

templates = Jinja2Templates(directory="templates")

#user.mount("/static", StaticFiles(directory="static"), name="static")

@user.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})