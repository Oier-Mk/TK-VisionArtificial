from imageRotator import points2yolo
import csv
def getCSVpoints(filename):
    lines = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("Leyendo las columnas...")
                line_count+=1
            else:
                imgname = row[0]
                width = row[1]
                height = row[2]
                xmin = row[3]
                ymin = row[4]
                xmax = row[5]
                ymax = row[6]

                points2yolo([[xmin,ymin],[xmax,ymax]],[width,height])

                with open('{}.txt'.format(imgname), 'w') as f:
                    f.write("0 {} {} {} {}".format(points2yolo([[xmin,ymin],[xmax,ymax]],[width,height])))




