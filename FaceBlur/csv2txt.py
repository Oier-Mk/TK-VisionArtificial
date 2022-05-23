import os

def convert(width, height, xmin, xmax, ymin, ymax):
    width = int(width)
    height = int(height)
    xmin = int(xmin)
    ymin = int(ymin)
    xmax = int(xmax)
    ymax = int(ymax)

    puntoX = abs(xmin-xmax)/2 + xmin
    puntoY = abs(ymin-ymax)/2 + ymin
    ancho = abs(xmin-xmax)
    alto = abs(ymin-ymax)

    propX = puntoX/width
    propY = puntoY/height
    propAncho = ancho/width
    propAlto = alto/height

    return ("0 {:.6f} {:.6f} {:.6f} {:.6f}\n".format(propX, propY, propAncho, propAlto))

def write2txt(name, dst, string):
    path = os.path.sep + dst+os.path.sep + name.split(".")[0] + '.txt'
    with open(path, 'w') as f:
        f.write(string)

import csv

import time

start = time.time()

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/dataSet/annotations.csv"
dst = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/dataSet/images"

numbers = ""

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    picture =  ""
    string = ""
    for row in csv_reader:
        if i == 0:
            i += 1
        else:
            if picture != row[0]:
                write2txt(picture,dst,string)
                string = ""
                picture = row[0]
                numbers += picture.split(".")[0]+"\n"
            string += convert(row[1], row[2], row[3], row[4], row[5], row[6]) 
            i += 1
    # Last picture
    write2txt(picture,dst,string)
    string = ""
    picture = row[0]
    string += convert(row[1], row[2], row[3], row[4], row[5], row[6]) 
    print(f'Processed {i} lines.')

end = time.time()

print("Runtime = " + str((end-start)*60) + "ms")

with open("/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/dataSet/numbers.txt", 'w') as f:
    f.write(numbers)