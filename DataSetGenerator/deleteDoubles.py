import glob
import os

#path = r"C:\Users\eneko\GitHub\TK-VisionArtificial\KaggleCoches\train\*.txt"
path = "/Users/mentxaka/Downloads/dataset/images/test/*.txt"

files = glob.glob(path)

for file in files:
    with open(file, 'r') as f: data = f.readlines()

    newText = ""
    for line in data:
        if line[0] == "0": 
            newText += line
    
    if newText != "":
        with open(".".join((file.split("."))[:-1]) + ".txt", 'w') as file: file.write(newText)


    if newText == "":
        os.remove(file)
        try:
            os.remove(".".join((file.split("."))[:-1]) + ".jpg")
        except:
            try:
                os.remove(".".join((file.split("."))[:-1]) + ".jpeg")
            except:
                os.remove(".".join((file.split("."))[:-1]) + ".png")
    