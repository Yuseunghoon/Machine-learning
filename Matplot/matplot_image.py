import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('C:/Users/bit-user/PycharmProjects/test/Matplot/test.jpg')

x_value = [500, 1500]
y_value = [550, 1770]

x_value1 = [1000, 2000]
y_value1 = [550, 1770]

x_value2 = [1500, 2500]
y_value2 = [550, 1770]

plt.plot(x_value, y_value)
plt.plot(x_value1, y_value1)
plt.plot(x_value2, y_value2)

plt.imshow(img)
plt.show()