import numpy as np
import cv2
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow


# punto 2
imagen = Image.open('img/jupiter.jpeg')
imagen_array = np.array(imagen)
# plt.imshow(imagen)
# plt.show()

# imagen.save('salidas/jupiter_copia.png')

print("primer pixel de la imagen ", imagen_array[0,0])

imagen_recortada_array = imagen_array[200:400, 200:400]
imagen_recortada = Image.fromarray(imagen_recortada_array.astype('uint8'))

# plt.imshow(imagen_recortada)
# plt.show()

# imagen_recortada.save('salidas/jupiter_recortada.png')