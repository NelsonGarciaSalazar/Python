# -*- coding: utf-8 -*-
"""
Created on Fri May  6 18:08:16 2022

@author: nelson.garcia

El game of the hanged consist in guess a word, in several attempts, if in a attempt fall go build a graph
graphic where the goes quedando ahorcado con cada intento. En cada turno se van selecionando letras que pueden
hacer parte de la palabra.
"""
import random

vidas = 5
palabras = ["python", "programacion", "mintic", "lenguaje"]

listaPalabra = []
listaGuiones = []
palabra = random.choice(palabras)
print(palabra)

for letra in palabra:
    listaPalabra.append(letra)
    listaGuiones.append("_")

cotVidas = 0
while cotVidas < 5:
    letraIngresda = input("Ingrese la letra: ")

    for i in range(len(listaPalabra)):
        if listaPalabra[i] == letraIngresda:
            listaPalabra[i] = letraIngresda

print(listaGuiones)