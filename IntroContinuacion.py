# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:03:12 2024

@author: Juliana
"""

import PIL
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

#Lemos la imagen, la pasamos a array y la desplegamos

I = Image.open('daisy.jpg') 
I_array=np.array(I)
imshow(I_array)
plt.axis('off')
plt.show

#Recortar una imagen: 1- conocer el tamaño

print("tamaño: ",I_array.size," y  dimensiones:",
      I_array.shape)

I_Recortada = I_array[100:200, 100:200,:]
plt.figure(figsize=(2,2))
imshow(I_Recortada) 
plt.axis('off')

I_array_falsocolor1 = I_array[:,:,(1,2,0)]
imshow(I_array_falsocolor1) 
plt.axis('off')

I_array_falsocolor2 = I_array[:,:,(2,0,1)]
imshow(I_array_falsocolor2) 
plt.axis('off')

#Mostrar todas las imágenes juntas, primero se define el espacio de despliegue.
fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)

axs[0,0].imshow(I_array) 
axs[0,0].set_title("Imagen original") 
plt.axis('off')
axs[0,1].imshow(I_Recortada) 
axs[0,1].set_title("Imagen Recortada") 
plt.axis('off')
axs[1,0].imshow(I_array_falsocolor1) 
axs[1,0].set_title("El falso color 1") 
plt.axis('off')
axs[1,1].imshow(I_array_falsocolor2) 
axs[1,1].set_title("El falso color 2") 
plt.axis('off')

#Guardar Imágenes Resultado

I_r = Image.fromarray(I_Recortada)
I_r.save("salidas/flor_recorte.png")
I_fc = Image.fromarray(I_array_falsocolor1)
I_fc.save('salidas/flor_falsocolor1.png')
I_d = Image.fromarray(I_array_falsocolor2)
I_d.save('salidas/flor_falsocolor2.png')

#Cambiar el tamaño de la imagen

imagenachicada = I.resize((100,100))
imagenagrandada = I.resize((150,400))

imagenachicada_a = np.array(imagenachicada)
imagenagrandada_a = np.array(imagenagrandada)

fig, axs = plt.subplots(nrows=1, ncols=2)

axs[0].imshow(imagenachicada_a)
axs[0].set_title("Achicada")
plt.axis('off')
axs[1].imshow(imagenagrandada_a)
axs[1].set_title("Agrandada en el eje y")

#Crear una imagen:
#1-Crear un cuadrado blanco
#2-Poner ceros en lugares estratégicos

cruz = np.ones((192,192)) 
cruz[:,64:129] = 0
cruz[64:129,:] = 0
fig, axs = plt.subplots(nrows=1, ncols=1)
plt.imshow(cruz, cmap='gray')
plt.show()
print(cruz.shape)