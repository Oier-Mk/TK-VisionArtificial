a = 10001
b = 18207


rango = list(range(a, b + 1))
lista = list()

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/dataSet/numbers.txt"

with open(path) as f:
    for i in f.readlines():
        lista.append(int(i))
f.close()

for i in range(a, b+1):
    print("numero actual " + str(i))
    if i in lista and i in rango:
        lista.remove(i)        
        rango.remove(i)

string = ''
for i in rango:
    string += str(i) + "\n"

with open("/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/dataSet/noAnnotations.txt", 'w') as f:
    f.write(string)