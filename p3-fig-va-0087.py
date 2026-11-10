import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 

# Alonso Lopez Garcia NC = 0087 | Fecha 10/11/2026
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
print("Alonso Lopez Garcia NC = 0087 | Fecha 10/11/2026")
mi_imagen = cv2.imread("ElizabethOlsen.jpg")
plt.imshow(mi_imagen)
plt.title("Elizabeth Olsen y Alonso Lopez -- 0087")
plt.show()
print(" ")
print("----- Puntos en la imagen -----")
plt.imshow(mi_imagen)
x = [100, 100, 300]
y = [100, 400, 500]
plt.scatter(x, y, s = 20, c = "red")
plt.show()
