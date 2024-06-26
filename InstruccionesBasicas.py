# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:14:51 2024

@author: Juliana Gambini
"""
#cadena de caracteres
#%% 
cadena = input("Introduce un texto:")
# Recibe el texto ingresado y lo almacena en la variable cadena que es string
print ("La cadena que ingresó es: ",cadena)
print("El tipo del dato ingresado es ",type(cadena))
print('La cadena que ingresó es: "',cadena,'"')

#Se ingresa un número por teclado, se muestra el número y el tipo de dato.
# Si no indicamos el tipo de dato se lo toma como string (cadena de caracteres)
#%% 
numero1 = input("Ingrese un número: ")
print("El nro ingresado es: ",numero1)
print("El tipo del dato ingresado es ",type(numero1))

#%% 
numero2 = int(input('Ingrese un número: '))
print("El nro ingresado es: ",numero2)
print("El tipo del dato ingresado es ",type(numero2))

#Tipos de datos básicos en Python
#int (entero)
#float (decimal)
#bool (booleano)
#complex (complejo)
#str (cadena de caracteres)

#Algunas funciones no necesitan librerías
#Como calcular el valor absoluto de un número (no es necesario cargar librerías)
#%% 
n = -3.2
c = abs(n)
print(c)

#%% 
#Convertir tipos de datos numéricos con las funciones

h = 3.4
o = int(h)
l = complex(h)
a = float(o)
print(h, o, l, a)

#%%
#Operaciones entre números enteros: cociente y resto (o módulo)
a = 7
b = 3
print(a//b)# Devuelve el Cociente entre enteros
print(a % b)# Devuelve el Resto de dividir a por b

#Lista de Operadores de Asignación
#Operador =
#Operador +=
#Operador -=
#Operador *=
#Operador /=
#Operador**=
#Operador //=
#Operador %=

#%%
a = 9
a += 2
print(a)
a //= 2
print(a)
a /= 3
print(a)
print(round(a))

#Datos booleanos (True y False)
#Operaciones Lógicas AND, OR y NOT

#%%
#Tipo de dato booleano: 'bool'
v1 = True #el valor verdadero: True
v2 = False #el valor falso: False

print("Valor de v1: ",v1, "Su tipo es: ", type(v1))
print("Valor de v2: ",v2, "Su tipo es: ", type(v2))
print()

#Operaciones Lógicas y, o y negación
print("v1 and v2= ", v1 and v2) # y lógico
print("v1 or v2= ",v1 or v2)  # o lógico
print("negación de v1= ",not v1)   # negación lógica

#Operadores para de comparación:
#== ; != ; < ; > ; <= ; >=
#%%
print ("3 == 5",3 == 5)  # Imprime False ya que son distintos
print("3 != 6",3 != 6)  # Imprime True ya que son distintos
print("3 < 5",3 < 5)  # Imprime True ya que 3 es menor que 5

#Estructura de Decisión: if
#if condición :
#    cuerpo del if #indentado con 4 espacios
#else:
#    cuerpo del else #indentado con 4 espacios

#Ejemplo
#%%
edad = 12

print("La persona es")
if (edad < 18):
    print("Menor")
else:
    print("Mayor")    
    
#Ejemplo opciones múltiples
#%%
edad = int(input("Ingrese edad: "))
if edad < 0:
    print("Error")
elif edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")    

#el mismo ejemplo pero usando operadores lógicos
edad = int(input("Ingrese edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    if (edad >= 0 and edad < 18):
        print("Menor de edad")
    else:
        print("Error")
        
#%%
#Comparaciones
nro1 = int(input('Ingrese nro: '))
nro2 = int(input('Ingrese nro: '))
if nro1 == nro2:
    print('\nLos números ingresados son iguales')
else:
    print('\nLos números ingresados son diferentes')        
#%%
#Indicar si el número es divisibe por 3
nrouno = int(input('Ingrese nro: '))
if nrouno%3 == 0:
    print('\nEl número es divisible por tres')
else:
    print('\nEl número no es divisible por tres')

#Listas
#Elementos de una lista: se colocan entre corchetes y se separan mediante comas
#El Python fue pensado para trabajar con listas
#Para operaciones matemáticas necesitaremos matrices
#Para trabajar con matrices necesitamos una biblioteca que se llama Numpy
#Las listas pueden tener elementos de distinto tipo
#Las matrices o arrays multidimensionales tienen todos sus elementos del mismo tipo
#%%
#Definamos una Lista
#Para hacerlo se usan corchetes y se separan los elementos mediante coma
lista=[1,3,5]
print("lista= ",lista, "su tipo es ", type(lista))

#acceso a un elemento de la lista
print(lista[0])

#%%
lista=['gato', 1, 2,3]
print('lista vieja ',lista)
lista[0]=5
print('lista nueva:', lista)
#%%
lista_nueva = list.copy(lista)
#agrego elemento
lista_nueva.append('perro')
print("Lista vieja",lista)
print('Nueva lista: ', lista_nueva)

#%%
#Operadores in y not in
print(2 in lista_nueva)
print(6 not in lista_nueva)








