
# Program to extract numbers from a string
string1 = '0919HHCsdjfghjakflkasdfklj'
string2 = 'asdfasd0919HHCsdjfghjakflkasdfklj'
string3 = '0919HHCsdjf!s2ghjakflkasdfklj'
string4 = '091]9HHCsdjfghjakflkasdfklj'
lecturaResultado = [string1,string2,string3,string4]
lecturaNombre = ["1","2","3","4"]

# def getRepIndexes(array, element):
#     indexes = [] 
#     if element not in array: return None
#     for idx, ele in enumerate(array):
#         if (element == ele): indexes.append(idx)
#     return indexes

# prov = []
# for idx, plate in enumerate(lecturaResultado):
#     prov.append(plate.replace(" ",""))
# lecturaResultado = prov


import re

def matchFormat(lecturaNombre,lecturaResultado):
        
    # Three digit number followed by space followed by two digit number
    pattern = '(\d{4})([BCDFGHJKLMNPQRSTWXYZ]{3})'

    for i, val in enumerate(lecturaResultado):

        match = re.search(pattern, val) 

        if match:
            lecturaResultado[i] = match.group()
        else:
            lecturaResultado.pop(i)
            lecturaNombre.pop(i)

    return lecturaNombre, lecturaResultado

lecturaNombre, lecturaResultado = matchFormat(lecturaNombre,lecturaResultado)

print(lecturaNombre)
print(lecturaResultado)

# # Program to extract numbers from a string
# string1 = '0919HHCsdjfghjakflkasdfklj'
# string2 = 'asdfasd0919HHCsdjfghjakflkasdfklj'
# string3 = '0919HHCsdjf!s2ghjakflkasdfklj'
# string4 = '091]9HHCsdjfghjakflkasdfklj'
# lecturaResultado = [string1,string2,string3,string4]
# lecturaNombre = ["1","2","3","4"]

# import re

# def matchFormat(string):
        
#     # Three digit number followed by space followed by two digit number
#     pattern = '(\d{4})([BCDFGHJKLMNPQRSTWXYZ]{3})'

#     # match variable contains a Match object.
#     match = re.search(pattern, string) 

#     if match:
#         print(match.group())
#         return(True,match.group())
#     else:
#         print("pattern not found")
#         return(False,None)


# for i,val in enumerate(lecturaResultado):
#     t,v = matchFormat(val)
#     if(t): lecturaResultado[i] = v
#     if(not t):
#         lecturaResultado.pop(i)
#         lecturaNombre.pop(i)
# print(lecturaNombre)
# print(lecturaResultado)



# # string1 = '0919HHCsdjfghjakflkasdfklj'
# # matchFormat(string1)
# # string2 = 'asdfasd0919HHCsdjfghjakflkasdfklj'
# # matchFormat(string2)
# # string3 = '0919HHCsdjf!s2ghjakflkasdfklj'
# # matchFormat(string3)
# # string4 = '091]9HHCsdjfghjakflkasdfklj'
# # matchFormat(string4)

