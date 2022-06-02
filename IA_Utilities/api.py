from fastapi import FastAPI, File, UploadFile, Request, Form
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
from pathlib import Path
from pydantic import BaseModel


relative = os.getcwd()

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

# HOME

@app.get("/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    return templates.TemplateResponse("home.html",{"request":request})

# PEDESTRIAN DETECTOR    

from PedestrianDetector.image import detectImage
from PedestrianDetector.main import pedestrianModel

@app.get("/PedestrianDetector/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    return templates.TemplateResponse("PedestrianDetector/uploadImage.html",{"request":request})

@app.post("/PedestrianDetector/response/", response_class=HTMLResponse)
async def uploadFile(request: Request, file: UploadFile = File(...)):
    path = "static" + os.path.sep + "PedestrianDetector" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
    with open( path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    nDetections, img = detectImage(path, pedestrianModel)
    path =  relative + os.path.sep + "static" + os.path.sep + "PedestrianDetector" + os.path.sep + "results" + os.path.sep + f'{file.filename}'
    cv2.imwrite(path,img)
    path = "PedestrianDetector/results/"+ f'{file.filename}'    
    return templates.TemplateResponse("PedestrianDetector/returnImage.html",{"request":request, "nDetections": nDetections, "path": path})

# FACE BLUR

from FaceBlur.main import faceBlur, faceModel

@app.get("/FaceBlur/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    return templates.TemplateResponse("FaceBlur/uploadImage.html",{"request":request})

@app.post("/FaceBlur/select/", response_class=HTMLResponse)
async def uploadFile(request: Request, file: UploadFile = File(...)):
    path = "static" + os.path.sep + "FaceBlur" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
    with open( path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "FaceBlur" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
    name =  f'{file.filename}'
    return templates.TemplateResponse("FaceBlur/selectRange.html",{"request":request, "path":path, "name":name})

@app.post("/FaceBlur/response/", response_class=HTMLResponse)
async def uploadFile(request: Request, x: int = Form(...), y: int = Form(...), x2: int = Form(...), y2: int = Form(...), imgName: str = Form(...)): #TODO paso de parametros incorrecto
    path =  relative + os.path.sep + "static" + os.path.sep + "FaceBlur" + os.path.sep + "pictures" + os.path.sep + f'{imgName}'
    nDetections, img = faceBlur(path, faceModel,[x,y,x2,y2])
    path =  relative + os.path.sep + "static" + os.path.sep + "FaceBlur" + os.path.sep + "results" + os.path.sep + f'{imgName}'
    cv2.imwrite(path,img)
    path = "FaceBlur/results/"+ f'{imgName}'    
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("FaceBlur/returnImage.html",{"request":request, "nDetections": nDetections, "path": path})

# IMAGE TRANSFORMATOR

from ImageTransformator.BoxImage import boxImage
from ImageTransformator.CleanNoise import cleanNoise
from ImageTransformator.DeleteLines import deleteLines
from ImageTransformator.Rotator import rotator
from ImageTransformator.Reader import reader

@app.get("/ImageTransformator/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    return templates.TemplateResponse("ImageTransformator/uploadImage.html",{"request":request})

@app.post("/ImageTransformator/response/", response_class=HTMLResponse)
async def uploadFile(request: Request, file: UploadFile = File(...), function: int = Form(...)):
    if function == 1:
        function = "BoxImage"
        path = "static" + os.path.sep + "ImageTransformator" + os.path.sep + "pictures" + os.path.sep + function + os.path.sep + f'{file.filename}'
        with open( path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        img = boxImage(path)
        path =  relative + os.path.sep + "static" + os.path.sep + "ImageTransformator" + os.path.sep + "results" + os.path.sep + function + os.path.sep + f'{file.filename}'
        cv2.imwrite(path,img)
        path = "ImageTransformator/results/"+ function +"/"+ f'{file.filename}'  
    if function == 2:
        function = "CleanNoise"
        path = "static" + os.path.sep + "ImageTransformator" + os.path.sep + "pictures" + os.path.sep + function + os.path.sep + f'{file.filename}'
        with open( path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        img = cleanNoise(path)
        path =  relative + os.path.sep + "static" + os.path.sep + "ImageTransformator" + os.path.sep + "results" + os.path.sep + function + os.path.sep + f'{file.filename}'
        cv2.imwrite(path,img)
        path = "ImageTransformator/results/"+ function +"/"+ f'{file.filename}' 
    if function == 3:
        function = "DeleteLines"
        path = "static" + os.path.sep + "ImageTransformator" + os.path.sep + "pictures" + os.path.sep + function + os.path.sep + f'{file.filename}'
        with open( path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        img = deleteLines(path)
        path =  relative + os.path.sep + "static" + os.path.sep + "ImageTransformator" + os.path.sep + "results" + os.path.sep + function + os.path.sep + f'{file.filename}'
        cv2.imwrite(path,img)
        path = "ImageTransformator/results/"+ function +"/"+ f'{file.filename}'  
    if function == 4:
        function = "Rotator"
        path = "static" + os.path.sep + "ImageTransformator" + os.path.sep + "pictures" + os.path.sep + function + os.path.sep + f'{file.filename}'
        with open( path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        img = rotator(path)
        path =  relative + os.path.sep + "static" + os.path.sep + "ImageTransformator" + os.path.sep + "results" + os.path.sep + function + os.path.sep + f'{file.filename}'
        cv2.imwrite(path,img)
        path = "ImageTransformator/results/"+ function +"/"+ f'{file.filename}' 
    if function == 5:
        function = "Reader"
        path = "static" + os.path.sep + "ImageTransformator" + os.path.sep + "pictures" + os.path.sep + function + os.path.sep + f'{file.filename}'
        with open( path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        text = reader(path)
        path = "static" + os.path.sep + "ImageTransformator" + os.path.sep + "results" + os.path.sep + function + os.path.sep + file.filename.split('.')[0] + '.txt'
        with open(path, 'w') as f:
            f.write(text)
        return templates.TemplateResponse("ImageTransformator/returnText.html",{"request":request, "text": text})
    return templates.TemplateResponse("ImageTransformator/returnImage.html",{"request":request, "path": path})







'''! --------------------------------------------------------------------------------------------------------- '''

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
    path =  relative + os.path.sep + "static" + os.path.sep + "PedestrianDetector" + os.path.sep + "results" + os.path.sep + f'{file.filename}'
    cv2.imwrite(path,img)
    path = "/static/results/"+ f'{file.filename}'
    return { "nDetections" : nDetections, "path" : path }
