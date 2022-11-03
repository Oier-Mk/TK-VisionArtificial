import glob

path = r"C:\Users\eneko\GitHub\TK-VisionArtificial\KaggleCoches\train\*.txt"

files = glob.glob(path)

for file in files:
    with open(file, 'r') as f: data = f.readlines()

    newText = ""
    for line in data:
        newText += "1" + line[1:]

    with open(file.split(".")[0] + ".txt", 'w') as file: file.write(newText)
