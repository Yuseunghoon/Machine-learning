import numpy as np

'''
a.shape 는 행렬 2 * 3 나타냄
a 는 행렬 보여줌
'''

a=np.array([[1,2,3],[4,5,6]])
print(a.shape)
print(a)

print('*'*30)

b=np.array([[7,8],[9,10],[11,12]])
print(b.shape)
print(b)

print('*'*30)

# a와 b를 내적을 하면, 행렬계산
c=np.dot(a,b)
print(c.shape)
print(c)

print('*'*30)

# 전치행렬
at=np.array([[1,2,3],[4,5,6]])
at=a.T
print(at)

print('*'*30)

#역행렬
import numpy.linalg as lin

a= np.array([[1,2],[4,5]])
print(a)

c = lin.inv(a)
print(c.shape)
print(c)

e1 = np.dot(a,c)
print(e1)

