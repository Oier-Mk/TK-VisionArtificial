import tensorflow as tf
import pathlib
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def clearTerminal():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def printDataSet(dataset,param):
    string = param
    for elem in dataset:
        string += '-'+str(elem.numpy())
    print(string)

def mecanicaBasica():
        
    print("MECANICA BÁSICA")

    dataset = tf.data.Dataset.from_tensor_slices([8, 3, 0, 8, 2, 1])
    dataset
    printDataSet(dataset,"dataset")

    it = iter(dataset) #hacemos el dataset iterable
    print(next(it).numpy())

    print("Suma de los elementos del data set con \"reduce:\" "+str(dataset.reduce(0, lambda state, value: state + value).numpy())) #suma de todos los elementos del dataset, reduce todos los elementos del dataset a uno 
    # donde se define que se tiene que reducir sumando los elementos del dataset
    print("Suma de los elementos del data set a lo bruto: "+str(8+3+0+8+2+1))

    print("---------------")

def estructurasDatos():

    print("ESTRUCTURA DEL CONJUNTO DE DATOS")
    dataset1 = tf.data.Dataset.from_tensor_slices(tf.random.uniform([4, 10]))
    print("dataset 1 "+ str(dataset1.element_spec))
    printDataSet(dataset1,"dataset1")

    dataset2 = tf.data.Dataset.from_tensor_slices(
    (tf.random.uniform([4]),
        tf.random.uniform([4, 100], maxval=100, dtype=tf.int32)))

    print("dataset 2 "+ str(dataset2.element_spec))
    #printDataSet(dataset2,"dataset2")

    dataset3 = tf.data.Dataset.zip((dataset1, dataset2))

    print("dataset 3 "+ str(dataset3.element_spec))
    #printDataSet(dataset3,"dataset3")

    # Dataset containing a sparse tensor.
    dataset4 = tf.data.Dataset.from_tensors(tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4]))

    print("dataset 4 "+ str(dataset4.element_spec))
    #printDataSet(dataset4,"dataset4")

    # Use value_type to see the type of value represented by the element spec
    print(dataset4.element_spec.value_type)

    dataset1 = tf.data.Dataset.from_tensor_slices(
        tf.random.uniform([4, 10], minval=1, maxval=10, dtype=tf.int32))

    print(dataset1)
    printDataSet(dataset1,"dataset1")

    dataset2 = tf.data.Dataset.from_tensor_slices(
    (tf.random.uniform([4]),
        tf.random.uniform([4, 100], maxval=100, dtype=tf.int32)))

    print(dataset2)

    dataset3 = tf.data.Dataset.zip((dataset1, dataset2))
    print(dataset3)
    print("Printeo dataset 3, zip dataset")
    for a, (b,c) in dataset3:
        print('shapes: {a.shape}, {b.shape}, {c.shape}'.format(a=a, b=b, c=c))

    print("---------------")

def matricesNumpy():
    print("CONSUMIR MATRICES NUMPY")
    train, test = tf.keras.datasets.fashion_mnist.load_data()
    images, labels = train
    images = images/255

    dataset = tf.data.Dataset.from_tensor_slices((images, labels))
    print(dataset)
    # no descomentar, hace un print de un dataset muy grande
    # for i in dataset:
    #     print(i)
    print("---------------")


def generadoresPython():
    print("CONSUMO DE GENERADORES DE PYTHON")
    def count(stop):
        i = 0
        while i<stop:
            yield i #genera los elementos on the fly, al momento.
            i += 1
    for n in count(5):
        print(n)

    ds_counter = tf.data.Dataset.from_generator(count, args=[30], output_types=tf.int32, output_shapes = (), )
    for count_batch in ds_counter.repeat().batch(10).take(10):
        print(count_batch.numpy())

def main():

    clearTerminal()
    print("$$$ Para hacer este turorial se ha seguido el de la siguiente pagina web $$$\nhttps://www.tensorflow.org/guide/data?hl=es-419")    
    np.set_printoptions(precision=4)

    #mecanicaBasica()
    #estructurasDatos()
    #matricesNumpy()
    generadoresPython()

    print("funciona")

main()
