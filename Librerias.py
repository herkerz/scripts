# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:05:57 2024

@author: Juliana Gambini

"""

#Qué es una librería?
#En informática, una biblioteca es un conjunto de implementaciones funciones, codificadas 
#en un lenguaje de programación, que realizan una serie de tareas específicas y 
#se incluyen o importan en el programa evitando tener que reescribir esos códigos.
#Librería numpy: sirve para realizar operaciones matriciales en Python.



#Dado un vector llamado v:
#np.len(v) np.sum(v) np.mean(v) np.median(v) np.max(v) np.min(v) np.std(v) np.round(v)
#np.float32(v) np.int32(v) cambia el tipo de dato
#np.concatenate((array2D_1,array2D_2),axis=1) o np.concatenate((array2D_1,array2D_2),axis=0)
#np.unique(v) #quita los elementos repetidos

#%%
import numpy as np #np es el alias
ve = [25., 8., 20., 75.]
print(ve)
print(type(ve))

v = np.array(ve) #Transformo la lista en vector
print("v =", v) #El vector no lleva comas separando los elementos
print("tipo de v:", type(v)) #el tipo es numpy.ndarray
print("longitud de v:", len(v))

# máximo y mínimo valor de v
print("máximo de v:", v.max()) #función de numpy.ndarray: np.max()
print("mínimo de v:", v.min())
print("suma de los valores de v", v.sum())
print("El valor medio es",v.mean())
#También puede hacer
#print(np.min(v)), np.max(v), np.sum(v))

#%%
#Ejemplo

#Definir dos vectores y mostrarlos
    # Defina el vector u=[5, 9, 10, -1]

    # Defina el vector v=[-2, 0, 5, 4]

#Calcule y muestre la suma
#Multiplique el vector suma por el escalar 2. Muestre.
#Reste a cada elemento del vector anterior el escalar 3.
#Muestre el valor medio del vector obtenido



u = np.array([6, 9,  10, -1]) #Transforma la lista en vector
v = np.array([-2, 0, 5, 4])
print("vector u", u)
print("vector v",v)

z = u + v
print("vector suma=",z)

w = 2 * z
print("2 * vector suma=",w)

t = w - 3
print("Restamos 3 a cada elemento del vector anterior",t)

print("Valor medio del vector resultado",np.mean(t))

#%%
#Otras utilidades
#np.zeros(n) Vector de n ceros
#np.ones(n) Vector de n unos
#np.full(n,m) Vector de n elementos todos iguales al valor m
#np.linspace(a,b,n)
# Ejemplo:np.linspace(0,1,5) Vector que empieza en 0 termina en 1 y tiene 5 valores.

x = np.zeros(4) #Genera vector de 4 ceros
u = np.ones(4) #Genera vector de 4 unos
t = np.full(4,7)#Genera vector de 4 sietes
print("x=",x,"u=",u,"t=",t),print()#Muestra los tres vectores generados y deja línea en blanco

print(np.arange(5,16,2)) #secuencia de 5 a 16 en paso de 2
s = np.arange(5,16,2)#Lo guarda en la variable s
print(s)#Muestra el vector s

print(type(s[0]))#Muestra el tipo de dato de los elementos de s
sn = np.float32(s)#Cambia el tipo de dato a float32 y lo asigna a una variable sn
print(type(sn[0]))#Muestra el tipo de dato de sn



