import os       

directory = r"FaceDataset\YOLOannotations"
directory2 = r"FaceDataset\dataset"

print(directory)
print(directory2)
counter = 0

for filename in os.listdir(directory):
    filename = filename.split(".")[0] + ".jpg"
    print(directory2+os.path.sep+filename)
    if(not os.path.isfile(directory2+os.path.sep+filename)):
        counter += 1
        print(filename)
    
print(counter)  


def deleteImg(name):
    os.remove("FaceDataset\dataset\\"+name+".jpg" )