letras = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
numeros = '0123456789'
extractedInformation = '10478LFR'
from collections import Counter
A = Counter(numeros)
B = Counter(extractedInformation[:-3])
print( (A&B) == B )
A = Counter(letras)
B = Counter(extractedInformation[5:])
print( (A&B) == B )
