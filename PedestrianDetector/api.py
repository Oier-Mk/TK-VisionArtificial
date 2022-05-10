from fastapi import FastAPI, File, UploadFile, Request
import shutil
import os
import io
from starlette.responses import StreamingResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from image import detectImage
from main import modeloYolo

app = FastAPI()

@app.get("/")
async def helloWorld():
    return {"Hello, world!"}

@app.get("/uploadFile/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("uploadFile.html",{"request":request})



@app.post("/upload/", response_class=HTMLResponse)
async def uploadFile(request: Request, file: UploadFile = File(...)) :
    path = "pictures" +os.path.sep + f'{file.filename}'
    with open( path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    nDetections, image = detectImage(path, modeloYolo)
    print("$$$$ "+str(nDetections))
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("returnImage.html",{"request":request, "nDetections": nDetections, "image":image})


@app.get("/items/")
async def read_item(UploadFile: str = 0):
    return UploadFile