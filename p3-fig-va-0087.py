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
print(" ----- Puntos en la imagen -----")
plt.imshow(mi_imagen)
x = [100, 100, 300, 340]
y = [100, 400, 500, 300]
plt.scatter(x, y, s = 20, c = "red")
plt.show()
print(" ----- Cuadro en la imagen -----")
img_Lizzie = cv2.imread("ElizabethOlsen.jpg")
plt.imshow(img_Lizzie)
# x = [136, 136, 555, 555, 136]
# y = [436, 35, 35, 436, 436]
x = [186, 186, 500, 500, 186]
y = [336, 35, 35, 336, 336]
plt.plot(x, y, c = "blue")
plt.show()
print(" ----- Colocar circulo verde a la imagen ----- ")
I = cv2.imread("ElizabethOlsen.jpg")
plt.imshow(I)
N = 30 
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc, yc) = (340, 320)
r = 150
for i in range (N+1):
    t =  2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)

plt.plot(x, y, c="green")
plt.show()