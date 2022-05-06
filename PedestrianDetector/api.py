from fastapi import FastAPI, File, UploadFile
import shutil
import os
import io
from starlette.responses import StreamingResponse
from image import detectImage
from main import modeloYolo

app = FastAPI()

@app.get("/")
async def helloWorld():
    return {"Hello, world!"}


@app.post("/uploadFile/")
async def uploadFile(file: UploadFile = File(...)) :
    path = "pictures" +os.path.sep + f'{file.filename}'
    with open( path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    nDetections, image = detectImage(path, modeloYolo)
    print("$$$$ "+str(nDetections))
    return StreamingResponse(io.BytesIO(image.tobytes()), media_type="image/png")
