# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:05:12 2024

@author: Juliana
"""

#Este programa calcula el histograma de una imagen

import PIL
import cv2 #opencv
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

#Lectura y despliegue

I = Image.open('daisy.jpg') 
I_array = np.array(I)
#imshow(I_array) 
#plt.axis('off')

img = cv2.imread('lenna.jpg',0)
print("El tamaño de la imagen es",img.size)
#imshow(img, cmap='gray',vmin=0 ,vmax=255)

#La función de opencv que vamos a usar para calcular el histograma
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) Devuelve un vector

#El nombre de la imagen debe estar entre corchetes
#Channels indica para qué canal se pide el histograma. Puede ser 0, 1 o 2. 
#Si la imagen es gris se pone 0.
#Si el histograma es de la imagen completa se coloca como máscara None. 
#Se puede pedir el histograma de una parte de la imagen, mediante una máscara. 
#histsize indica la cantidad de bins. Si queremos contabilizar la frecuencia de todas las intensidades
#y tenemos 256 valores, colocamos 256 entre corchetes. Podemos agruparlos. Pedir por ejemplo 16 bins.
#ranges es el rango. En nuestro caso es [0,256]
#Así hist será un array de 256x1

hist = cv2.calcHist([img],[0],None,[256],[0,256])
hist = hist/img.size
plt.plot(hist)
plt.xlabel("Intensidad")
plt.ylabel("Cantidad de Píxeles")
plt.title("Histograma")
plt.show()

#Imagen e Histograma

plt.subplot(121), plt.imshow(img, 'gray'),plt.title('Imagen'), plt.axis('off')
plt.subplot(122), plt.plot(hist), plt.xlabel('Intensidad'),plt.ylabel("Cantidad píxeles"),
plt.xlim([0,256])


plt.show()

#Se puede estudiar el histograma de una parte de la imagen
# crea la máscara
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img=cv2.bitwise_and(img, mask)#toma los pixels de la imagen

# Calcula el histograma de la imagen

hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
#Calcula el histograma dentro de la máscara
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])


plt.subplot(221), plt.imshow(img, 'gray'),plt.title('imagen completa'), plt.axis('off')
plt.subplot(222), plt.imshow(mask,'gray'),plt.title('máscara con lugares')
plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('imagen en la máscara')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask),plt.xlabel('Intensidad'),plt.ylabel("Cantidad píxeles"),plt.legend(['completa', 'máscara'])
plt.xlim([0,256])

plt.show()

#Histogramas de la imagen modificada