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

#getting the actual directory path
relative = os.getcwd()

app = FastAPI()
app.mount("/static" , StaticFiles(directory="static"), name="static")

#default get of the API
@app.get("/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("index.html",{"request":request})

#HTML form for uploading an image (TEMPLATES)
@app.get("/uploadFile/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("uploadFile.html",{"request":request})

#gets the image from /uploadFile/ and uses Yolo model, then it returns in a HTML template format
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

#HTML form for uploading an image (JSON) 
@app.get("/uploadFileJSON/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("uploadFileJSON.html",{"request":request})

#gets de image from /uploadFileJSON/ and uses a Yolo model, then it returns in a JSON format 
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
