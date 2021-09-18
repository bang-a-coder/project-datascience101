import math
import numpy as np
import matplotlib.pyplot as plt

x_coords = []
y_coords = []
counter = -1
for i in np.arange(-2, 2, 0.1):
    for k in np.arange(-2, 2, 0.1):
	    y_coords.append(k)
	    x_coords.append(i)




complex_list = []
for counter in range(0, len(x_coords)):
	complex_list.append(complex(x_coords[counter], y_coords[counter]))

mandelbrot = []
for counter in range(0, len(x_coords)):
    Z = 0
    for i in range(50):
	    Z_after = Z*Z + complex_list[counter]
	    Z = Z_after
    if np.abs(Z)>= 2:
        mandelbrot.append(0)
    else:
        mandelbrot.append(1)
print(mandelbrot)
print(len(x_coords))
#coordinates = list(zip(x_coords, y_coords))
img=np.full((len(x_coords),len(y_coords)), 5)

for x in range(0, len(x_coords)):
 	for y in range(0, len(x_coords)):
 		img[x][y] = 5 - mandelbrot[x]

plt.imshow(img, cmap="plasma")
plt.axis("off")
plt.show()

