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


# @app.post("/upload/", response_class=HTMLResponse)
# async def uploadFile(request: Request, file: UploadFile = File(...)) :
#     path = "static" + os.path.sep + "pictures" + os.path.sep + f'{file.filename}'
#     with open( path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     nDetections, img = detectImage(path, modeloYolo)
#     path =  relative + os.path.sep + "static" + os.path.sep + "results" + os.path.sep + f'{file.filename}'
#     cv2.imwrite(path,img)
#     path = "/static/results/"+ f'{file.filename}'
#     #json_compatible_item_data = jsonable_encoder(ReturnObject(path))
#     #return JSONResponse(content=json_compatible_item_data)
#     templates = Jinja2Templates(directory="templates")
#     return templates.TemplateResponse("returnImage.html",{"request":request, "nDetections": nDetections, "path":path})

#class ReturnObject(BaseModel):
    #image: str
    #nDetections: int
    # def __init__(self,nDetections,image):
    #     self.nDetections = nDetections
    #     self.image = image
    #def __init__(self,nDetections):
        #self.nDetections = nDetections