# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:27:27 2024

@author: Juliana
"""

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

def ajuste_gamma(imagen,gamma):
    imagenresultado=255*((imagen/255)**gamma)
    imagenresultado=imagenresultado.astype('uint8')
    return imagenresultado

clara=ajuste_gamma(img, 0.2)
oscura=ajuste_gamma(img, 2)

fig, axs = plt.subplots(nrows=1, ncols=3, sharex=True)
fig.set_figheight(4)
fig.set_figwidth(15)
axs[0].imshow(img, cmap='gray',vmin=0 ,vmax=255)
axs[0].set_title('Imagen original')
axs[1].imshow(clara, cmap='gray',vmin=0 ,vmax=255)
axs[1].set_title('Modificación gamma = 0.2')
axs[2].imshow(oscura, cmap='gray',vmin=0 ,vmax=255)
axs[2].set_title('Modificación gamma = 2')
plt.show()

fig, axs = plt.subplots(nrows=1, ncols=3, sharex=True)
fig.set_figheight(4)
fig.set_figwidth(15)
axs[0].hist(img[:,:].ravel(), 256,[0,256] ) 
axs[0].set_title('Histograma de original')
axs[0].set_xlabel('intensidad de iluminacion')
axs[0].set_ylabel('cantidad de pixeles')
axs[1].hist(clara[:,:].ravel(), 256,[0,256] ) 
axs[1].set_title('Histograma de aclarada')
axs[1].set_xlabel('intensidad de iluminacion')
axs[1].set_ylabel('cantidad de pixeles')
axs[2].hist(oscura[:,:].ravel(), 256,[0,256] ) 
axs[2].set_title('Histograma de oscurecida')
axs[2].set_xlabel('intensidad de iluminacion')
axs[2].set_ylabel('cantidad de pixeles')
plt.show()
