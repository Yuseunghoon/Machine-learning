# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:42:00 2017

@author: BEAST

Scikit-Learn 패키지를 이용한 선형 회귀 분석 모델 작성.


"""
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

# scikit_learn에서 제공하는 데이터 제공 함수
X_train, y_train, coef = make_regression(n_samples=50, n_features=1, bias=50, noise=20, coef=True, random_state=1) # 가상 데이터 생성

# 상수항이 있으면
model = LinearRegression(fit_intercept=True)
model.fit(X_train, y_train)

# 선형회귀 직선을 작성하기 위해 데이터 생성
# X_train 데이터의 초대, 최소 값 사이를 100의 데이터로 구분한다.
x_new = np.linspace(np.min(X_train), np.max(X_train), 100)
#linspace(start, end, num-point(개수))

X_new = x_new.reshape(-1,1)
# reshape 함수를 이용하여 행수와 열수를 조절 가능
# 1차원 배열을 -> 2 * 5 배열로 변형가능
print('X_new :', X_new)

# 그래프를 그리기 위한 y 예측 값 --> 직선을 그리기 위한 x 값과 그에 따른 y 값 정의
y_predict= model.predict(X_new)

# 예측 값
y_pred = model.predict(X_train)


#mse = mean_squared_error(y_train, y_pred)

#print('MSE :' ,mse)

plt.plot(X_new, y_predict, 'g-', label ="regression")
plt.scatter(X_train, y_train, c='r', label="data")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")
plt.legend()
plt.show()
