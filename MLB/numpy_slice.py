import numpy as np

x1 = list(range(10))
x2 = x1[0:3]

print(x1,'\n', x2)

x2[1] = 100
print(x2)

y1 = np.array([0,1,2,3,4,5,6,7,8,9])

print(y1)

y2 = y1[0:3]
y2[1] = 100
print(y2)

