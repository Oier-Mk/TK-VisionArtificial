#ESTE SCRIPT REALIZA UN BARRIDO POR TODO ESE TXT CON LOS N'UMEROS DE LOS QUE SE HA REALIZADO LA CONVERSI'ON DE LAS ANOTACIONES
#CON ESTE SCRIPT SE VER'A CUALES SON LAS FOTOS SIN ANOTACI'ON.

a = 10001
b = 12015

rango = list(range(a, b + 1))
lista = list()

path = "/Users/mentxaka/Documents/Y - Trabajo/TK - VisionArtificial/FaceBlur/data/train/"
numbers = path + "numbers.txt"

with open(numbers) as f:
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

with open(path+"noAnnotations.txt", 'w') as f:
    f.write(string)