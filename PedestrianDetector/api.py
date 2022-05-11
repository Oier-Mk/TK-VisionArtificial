from fastapi import FastAPI, File, UploadFile, Request
import shutil
import os
import io
import cv2
from starlette.responses import StreamingResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from image import detectImage
from main import modeloYolo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def helloWorld():
    return {"Hello, world!"}

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
    scale_percent = 30 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    path = os.path.sep + "static" + os.path.sep + "results" + os.path.sep + f'{file.filename}'
    cv2.imwrite(path,resized)
    print("$$$$ "+str(nDetections))
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("returnImage.html",{"request":request, "nDetections": nDetections, "image":path})


@app.get("/items/")
async def read_item(UploadFile: str = 0):
    return UploadFile