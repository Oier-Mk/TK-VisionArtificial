import os       

YOLOannotations = "/Users/mentxaka/Github/TK-VisionArtificial/DataSetGenerator/FaceDataset/YOLOannotations"
dataset = "/Users/mentxaka/Github/TK-VisionArtificial/DataSetGenerator/FaceDataset/dataset"

print(YOLOannotations)
print(dataset)

def function1():
    counter = 0
    for filename in os.listdir(YOLOannotations):
        print(str(os.path.exists(YOLOannotations+os.path.sep+filename)) + " file in annotations")
        filename = filename.split(".")[0] + ".jpg"
        print(str(os.path.exists(dataset+os.path.sep+filename)) + " file in photos")
        print("---------------")
        '''print(dataset+os.path.sep+filename)
        if(not os.path.exists(dataset+os.path.sep+filename)):
            counter += 1
            print(filename)
        '''
        counter += 1
    print(counter)  



def function2():
    counter = 0
    for filename in os.listdir(dataset): 
        txtname = filename.split(".")[0] + ".txt"
        imgname = filename.split(".")[0] + ".jpg"
        if(not os.path.exists(YOLOannotations+os.path.sep+txtname)):
            print("Eliminamos "+dataset+os.path.sep+imgname)
            counter+=1
            os.remove(dataset+os.path.sep+filename)
    print(counter)

function2()
#function1()