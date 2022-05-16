from fastapi import FastAPI, File, UploadFile, Request
import shutil
import os
import io
import cv2
from starlette.responses import StreamingResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from image import detectImage
from main import modeloYolo

relative = os.getcwd()

app = FastAPI()
app.mount("/static" , StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/uploadFile/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("uploadFile.html",{"request":request})

@app.post("/upload/", response_class=HTMLResponse)
async def uploadFile(request: Request, file: UploadFile = File(...)) :
    path = "static" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
    with open( path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    nDetections, img = detectImage(path, modeloYolo)
    path =  relative + os.path.sep + "static" + os.path.sep + "results" + os.path.sep + f'{file.filename}'
    cv2.imwrite(path,img)
    path = "/static/results/"+ f'{file.filename}'
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("returnImage.html",{"request":request, "nDetections": nDetections, "path":path})

@app.get("/uploadFileJSON/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("uploadFileJSON.html",{"request":request})

@app.post("/uploadJSON/", response_class=JSONResponse)
async def uploadFile(request: Request, file: UploadFile = File(...)) :
    path = "static" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
    with open( path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    nDetections, img = detectImage(path, modeloYolo)
    path =  relative + os.path.sep + "static" + os.path.sep + "results" + os.path.sep + f'{file.filename}'
    cv2.imwrite(path,img)
    path = "/static/results/"+ f'{file.filename}'
    return { "nDetections" : nDetections, "path" : path }
