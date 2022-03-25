
def getRepIndexes(array, element):
    indexes = [] 
    if element not in array: return None
    for idx, ele in enumerate(array):
        if (element == ele): indexes.append(idx)
    return indexes

def remSpace(lecturaResultado):
    print("borrando espacio")
    prov = []
    for idx, plate in enumerate(lecturaResultado):
        prov.append(plate.replace(" ",""))
    lecturaResultado = prov
    print("espacios borrados")
    return(lecturaResultado)


def remEquals(lecturaNombre, lecturaResultado):
    print("borrando iguales")
    for plate in lecturaResultado:
        indexes = getRepIndexes(lecturaResultado, plate)
        lecturaResultado[indexes[0]].replace(" ","")
        indexes.pop(0)
        for idx in indexes:
            print(f"index {idx}   {lecturaResultado[idx]}   {lecturaNombre[idx]}")
            lecturaResultado.pop(idx)
            lecturaNombre.pop(idx)
    print("iguales borrados")
    return(lecturaNombre,lecturaResultado)

lecturaResultado = ["8674CZD", "8674CZD", "8477FNM", "8477FNM", "8477FNM", "8477FNM", "1464JNR", "L4464JNR]", "8674CZD", "8674CZD", "8477FNM", "8477FNM", "8477FNM", "8477FNM", "1464JNR", "L4464JNR]"]
lecturaNombre =    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

for plate in lecturaResultado:
  indexes = getRepIndexes(lecturaResultado, plate) #0,5
  print(f"original {lecturaResultado[indexes[0]]}")
  indexes.pop(0) #5
  print(indexes)
  for i, idx in enumerate(indexes): 
    print(f"i  {i}")
    print(lecturaResultado[idx-i])
    lecturaResultado.pop(idx-i) #-5
    lecturaNombre.pop(idx-i)
  print(f"iteracion   {len(indexes)}")
  print(lecturaResultado)
  print(lecturaNombre)
  print("\n")
  #print(indexes)
  