

from ast import Not


def funcion(X1,peso):
    valor = X1*peso
    pass

def perceptron(X1,Z1):
    tasaAprendizaje = 0.3
    peso = 0
    salida = funcion(X1*peso)
    if salida != Z1 :
        error = Z1 - salida
        peso = tasaAprendizaje * error + peso