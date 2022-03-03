from bs4 import BeautifulSoup
import glob
import os

#path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/KaggleCoches/images/Cars0.png"
path = "/Users/mentxaka/Documents/Y - Trabajo/TK - Vision Artificial/KaggleCoches/images/*"

files = glob.glob(path)
files.sort()

for path in files:
    if path.split('.')[-1] == "xml":
        
        # Reading the data inside the xml
        # file to a variable under the name
        # data
        with open(path, 'r') as file:
            data = file.read()

        # Passing the stored data inside
        # the beautifulsoup parser, storing
        # the returned object
        Bs_data = BeautifulSoup(data, "xml")

        # Finding all instances of tag
        # `unique`
        width = int(Bs_data.find('width').text)
        height = int(Bs_data.find('height').text)
        xmin = int(Bs_data.find('xmin').text)
        ymin = int(Bs_data.find('ymin').text)
        xmax = int(Bs_data.find('xmax').text)
        ymax = int(Bs_data.find('ymax').text)

        # width = 6
        # height = 6
        # xmin = 2
        # ymin = 2
        # xmax = 4
        # ymax = 4

        puntoX = abs(xmin-xmax)/2
        puntoY = abs(ymin-ymax)/2
        ancho = abs(xmin-xmax)
        alto = abs(ymin-ymax)

        propX = puntoX/width
        propY = ancho/height
        propAncho = puntoX/width
        propAlto = alto/height

        #print("0 " + str(propX) + " " + str(propY) + " " + str(propAncho) + " " + str(propAlto))
        string = ("0 {:.6f} {:.6f} {:.6f} {:.6f} ".format(propX, propY, propAncho, propAlto))
        print(string)

        path = path.split(".")[0]+'.txt'
        #print("$$ "+string+" ## "+path)

        with open(path, 'w') as f:
            f.write(string)
