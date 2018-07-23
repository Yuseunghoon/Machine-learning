import numpy as np

x = np.array([[2,3,],[4,5]])
y = 5

x1 = x + y

print(type(x))
print(type(y))
print(x1)

x2 = np.array([[2,3,],[7,8]])
y2 = np.array([[5,10]])

x3 = x2 + y2
print('x2 shape', x2.shape)
print('y2 shape', y2.shape)
print('x3 shape', x3.shape)

print('x3', x3)