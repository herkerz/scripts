# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:08:12 2024

@author: Juliana
"""

#Operaciones puntuales: Modificación de Rango y Ajuste Gamma

import PIL
import cv2
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

#Lectura de imagen
I = Image.open('daisy.jpg') 
I_array = np.array(I)
imshow(I_array) 
plt.axis('off')

#Multiplicación por un escalar

J1 = 2* I_array
J1_im = Image.fromarray(J1.astype(np.uint8))
J1_im.save('salidas/ejemploOpPuntual.png') 
imshow(J1) 
plt.axis('off')

J2 = 0.5* I_array
J2 = J2.astype('uint8')
imshow(J2) 
plt.axis('off')