
import numpy as np


def softmax(a):
    c = np.max(a)
    print('softmax c :', c)
    exp_a = np.exp(a-c) # 자연상수 e 지수함수로 변환
    print('exp_a :', exp_a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# e100 은 0 dl 40 개가 넘는 큰값
def softmax1(a):
    c = np.max(a)
    print('softmax1 c :', c)
    exp_a = np.exp(a)   # overflow 대비책
    print('exp_a :', exp_a)

    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3, 2.9, 4.0])
#a= np.array([1010, 1000, 990])

y = softmax(a)
y1= softmax1(a)

# Softmax 결과의미
# 1) 확률
# 2) 각 원소간의 관계 변하지 않음 : exp 함수가 단조 증가함수이기 때문에


print( "Softmax Result :", y)
print( "SUM : " , np.sum(y))
print( "Softmax1 Result :", y1)
print( "SUM : " , np.sum(y1))