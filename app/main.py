import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
template = Jinja2Templates(directory=str(BASE_DIR / "template"))
print(BASE_DIR/"template")
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home_view(request: Request):
    return template.TemplateResponse("home.html", {"request":request, "abc":12})

@app.post("/")
def home_detail_view():
    return {"Hello":"World"}
