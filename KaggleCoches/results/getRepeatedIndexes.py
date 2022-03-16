
def getRepIndexes(array, element):
    indexes = [] 
    if element not in array: return None
    for idx, ele in enumerate(array):
        if (element == ele): indexes.append(idx)
    return indexes

# array = ["A", "B", "C", "D", "E", "F", "A", "B", "A"]
# element = "A"


# print(getRepIndexes(array, element))

lecturaNombre = ["hola","buenas","nombre","apellido","hola","nombre"]
lecturaResultado = ["1234","2345","3456","4567","1234","3456"]
    
for plate in lecturaResultado:
    indexes = getRepIndexes(lecturaResultado, plate)
    indexes.pop(0)
    for idx in indexes:
        lecturaResultado.pop(idx)
        lecturaNombre.pop(idx)

print(lecturaNombre)
print(lecturaResultado)