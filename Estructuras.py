# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:49:58 2024

@author: Juliana Gambini
"""

#Ejemplo for en lista
#Permite recorrer todos los elementos de una lista


#El objetivo es sumar todos los elementos de la lista
#El acumulador debe inicializarse en 0
#De lo contrario guardará el valor en caso de hacerse otras corridas

suma = 0
mis_numeros = [4,8,12,18]
for numero in mis_numeros:
    suma = suma + numero
    print("esto imprime sumas parciales porque está dentro del for", suma)

print()
print("esto se imprime fuera del ciclo")
print('La lista es',mis_numeros)
print("La suma de los números de la lista es:")
print(suma)

#%%
#Función range: #con un parámetro, este indica la cantidad de elementos. 
#Empieza en 0, salto implícito 1. 
#con dos parámetros, el primero indica el principio, el otro el final que es abierto 
#(no lo incluye). 
#con tres parámetros, indican principio, el final abierto, el paso o salto.
#El intervalo es abierto a derecha
a = range(3)
b = range(2,6)
c = range(1,10,2)

print("Un for para range de 0 a 2")
for i in a:
    print(i)
print("Un for para range de 2 a 5:")
for j in b:
    print(j)

print("Un for para range de 1 a 9, paso 2")
for z in c:
    print(z)

#%%
#Funciones creadas por el usuario

#Definir y usar una función que dé el signo de un número
def signo(x):
    if x > 0:
        return 'positivo'
    elif x < 0:
        return 'negativo'
    else:
        return 'cero'
#Llamar a la función
for x in [-1, 0, 1]:
    print(signo(x))






