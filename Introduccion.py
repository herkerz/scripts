# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:36:16 2024

@author: Juliana
"""
#Instalamos las librerías necesarias y las importamos.
#numpy es para operaciones
#Pillow y cv2 para manejo de imágenes
#matplotlib para hacer gráficos

import numpy as np
import cv2
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

#Ahora sí podemos leer la imagen


I = Image.open('daisy.jpg') 

#Y luego tomar información como tamaño, 
#si es en color o grises y desplegarla en la pantalla.

print("El tamaño de la imagen es",I.size)
print("El modo de la imagen es", I.mode) 
print("El tipo de imagen es",I.format) 
print(type(I))

#Usamos la librería matplotlib con
#su pseudónimo plt para el despliegue.

plt.imshow(I)
plt.axis('off')
plt.show()

#Convierte la imagen en gris. En este ejemplo se la guarda en otra variable

Igris = I.convert('L') 
#muestra la imagen en paleta de grises
plt.imshow(Igris, cmap="gray")
plt.axis('off')
plt.show()

##muestra la imagen en la paleta que tiene por default

plt.imshow(Igris)
plt.axis('off')
plt.show()

#Graba la imagen creada. Función propia de PIL pero es 
#necesario haber creado la carpeta "salidas"

Igris.save('salidas/daisygris.png') 

#Para poder manipular numéricamente los valores de intensidad es necesario 
#usar la librería numpy. Para eso se debe convertir la imagen en un array.

J = Image.open('lenna.jpg')
J_array = np.array(J)
imshow(J_array) 
plt.axis('off')
plt.show()

print("La imagen el tamaño es ",J.size,", el modo es ",J.mode," y el formato es", J.format)

print("El array: size da la cantidad de píxeles: ",J_array.size," y shape da las dimensiones:",
      J_array.shape)
print("Tipo de datos del array: ", J_array.dtype)

#Se puede llevar nuevamente el array a imagen y grabarla
#Al grabar en jpg se comprime el archivo y se modifican los datos
#(en general imperceptibles al ojo)

J_nueva=Image.fromarray(J_array.astype(np.uint8))
J_nueva.save('salidas/Lenna_prueba.jpg')

#Tomamos la banda del rojo de la imagen, en este caso usamos la librería matplotlib con
#su pseudónimo plt

rojo = J_array[:,:,0]
print("dimensiones de la componente roja (monocroma) =" , rojo.shape)
plt.imshow(rojo, cmap='gray')
plt.title('componente rojo')
plt.axis('off')
plt.show()

#Hacemos lo mismo con la banda del verde, observar que los colores de esta banda
#son más oscuros. 

verde = J_array[:,:,1]
print("dimensiones de la componente roja (monocroma) =" , verde.shape)
plt.imshow(verde, cmap='gray')
plt.title('componente verde')
plt.axis('off')
plt.show()

#Hacemos lo mismo con la imagen daisy

I_array=np.array(I)
imshow(I_array) 

Daisy_R = I_array[:,:,0]
Daisy_G = I_array[:,:,1]
Daisy_B = I_array[:,:,2]
plt.imshow(Daisy_R, cmap='gray')
plt.title('Banda del Rojo')
plt.show()
plt.imshow(Daisy_G, cmap='gray')
plt.title('Banda del Verde')
plt.show()
plt.imshow(Daisy_B, cmap='gray')
plt.title('Banda del Azul')
plt.show()

#Cambiamos el orden de los canales y observamos los valores del pixel en la posición 
#(0,0)

I_array_falsocolor=I_array[:,:,[1,2,0]]

plt.imshow(I_array_falsocolor)
plt.title('Falso color')
plt.show()
print("primer pixel imagen original:",I_array[0,0,:])
print("primer pixel falso color:",I_array_falsocolor[0,0,:])

#Si le damos un valor más pequeño a los pixels entonces se ve más oscura.
#Cuando dividimos por dos los números que componen la imagen ya no son enetros
#entonces no podemos mostrarla como imagen, por eso la pasamos a uint8

I_array_oscurecida = I_array[:,:,:]/2 

I_array_oscurecida = I_array_oscurecida.astype('uint8')
plt.imshow(I_array_oscurecida)
plt.title('Imagen Oscurecida')
plt.show()

print("primer pixel imagen oscurecida:", I_array_oscurecida[0:1,0:1,:])
