
# def matchFormat(lecturaNombre,lecturaResultado):
#     import re   

#     for i, val in enumerate(lecturaResultado):

#         match = re.search('([1234567890]{4})([BCDFGHJKLMNPQRSTWXYZ]{3})', val) 

#         if match:
#             lecturaResultado[i] = match.group()
#         else:
#             lecturaResultado.pop(i)
#             lecturaNombre.pop(i)

#     return lecturaNombre, lecturaResultado
    
# # Program to extract numbers from a string
# string1 = '0919HH'
# string2 = 'HGG1234'
# string3 = '123D4GG'
# string4 = 'H20'
# string5 = '5088FWK'

# lecturaResultado = [string1,string2,string3,string4,string5]
# lecturaNombre = ["1","2","3","4","5"]

# lecturaNombre, lecturaResultado = matchFormat(lecturaNombre,lecturaResultado)

# print(lecturaNombre)
# print(lecturaResultado)

import re

#Check if the string starts with "The" and ends with "Spain":

string1 = "loHMC"
string2 = "0919`HHC"
string3 = "9950EFX"
string4 = "77950EFX"
string5 = "DOM"
string6 = "	"
string7 = "7LCZD"
string8 = "8674CZD"
string9 = "7FNM"
string10 = "FNM3477"
string11 = "8477FNM"
string12 = "0477FhV"
string13 = "ELLZHCX"
string14 = "33HVV"
string15 = "0133HVV"
string16 = "0133AVV"
string17 = "TV"
string18 = "EL64JNR"
string19 = "1464JNR"
string20 = "4464JNR"
string21 = "JNRLL6L"



lecturaResultado = [string1,string2,string3,string4,string5,string6,string7,string8,string9,string10,string11,string12,string13,string14,string15,string16,string17,string18,string19,string20,string21]

for idx, val in enumerate(lecturaResultado):
  match = re.search('([1234567890]{4})([BCDFGHJKLMNPQRSTWXYZ]{3})', val) 
  if match:
    print(f"YES! We have a match! idx = {idx} $$ val = {lecturaResultado[idx]}")
  else:
    print("No match")
