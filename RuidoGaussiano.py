# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:31:52 2024

@author: Juliana
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

Img = cv2.imread('lenna.jpg')    # numpy-array of shape (N, M); dtype=np.uint8
Img_gris = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)#Convierte en escala de grises.

mean = 5.0   # valor medio
std = 20.0    # desviación estándar
ruidoGaussiano = np.random.normal(mean, std, Img_gris.shape) #genero ruido Gaussiano
imagen_con_ruido = Img_gris + ruidoGaussiano


#Aplico filtro gaussiano mascara de 9 x 9
blur = cv2.GaussianBlur(imagen_con_ruido,(9,9),0)

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)

plt.subplot(131),plt.imshow(Img_gris,cmap='gray',vmin=0,vmax=255),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(imagen_con_ruido,cmap='gray',vmin=0,vmax=255),plt.title('Con ruido')
plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(blur,cmap='gray',vmin=0,vmax=255),plt.title('Con filtro Gaussiano')
plt.xticks([]), plt.yticks([])
plt.show()




