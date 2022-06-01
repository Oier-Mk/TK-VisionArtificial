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
from PedestrianDetector.image import detectImage
from PedestrianDetector.main import pedestrianModel
from FaceBlur.main import faceBlur, faceModel

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
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("home.html",{"request":request})

# PEDESTRIAN DETECTOR    

@app.get("/PedestrianDetector/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
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
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("PedestrianDetector/returnImage.html",{"request":request, "nDetections": nDetections, "path": path})

# FACE BLUR

@app.get("/FaceBlur/", response_class=HTMLResponse)
async def uploadFile(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("FaceBlur/uploadImage.html",{"request":request})

@app.post("/FaceBlur/select/", response_class=HTMLResponse)
async def uploadFile(request: Request, file: UploadFile = File(...)):
    templates = Jinja2Templates(directory="templates")
    path = "static" + os.path.sep + "FaceBlur" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
    with open( path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "FaceBlur" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
    name =  f'{file.filename}'
    return templates.TemplateResponse("FaceBlur/selectRange.html",{"request":request, "path":path, "name":name})


@app.post("/FaceBlur/response/", response_class=HTMLResponse)
async def uploadFile(request: Request, x: int = Form(...), y: int = Form(...), x2: int = Form(...), y2: int = Form(...), x3: int = Form(...), y3: int = Form(...), x4: int = Form(...), y4: int = Form(...),x5: int = Form(...), y5: int = Form(...), imgName: str = Form(...)): 
    path =  relative + os.path.sep + "static" + os.path.sep + "FaceBlur" + os.path.sep + "pictures" + os.path.sep + f'{imgName}'
    #nDetections, img = faceBlur(path, faceModel,[(x,y),(x2,y2),(x3,y3),(x4,y4),(x5,y5)])
    nDetections=0
    r = [(x,y),(x2,y2),(x3,y3),(x4,y4),(x5,y5)]
    img=cv2.imread(path)
    for h in range(len(r)):
        cv2.circle(img, (r[h][0],r[h][1]), radius=5, color=(0, 0, 255), thickness=-1)
    path =  relative + os.path.sep + "static" + os.path.sep + "FaceBlur" + os.path.sep + "results" + os.path.sep + f'{imgName}'
    cv2.imwrite(path,img)
    path = "FaceBlur/results/"+ f'{imgName}'    
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("FaceBlur/returnImage.html",{"request":request, "nDetections": nDetections, "path": path})










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
