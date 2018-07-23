# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:29:03 2017


숫자인식 예제
PythonProgramming.net 참조
@author: BEAST
"""



import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

X_train, y_train = digits.data, digits.target
print(X_train, y_train)

digits_index = 9

svm_model = svm.SVC(gamma=0.0001, C=100)
svm_model.fit(X_train, y_train)
# x,y 2차원 데이터에서 x 값인 X_train과 y 값인 y_train을 가지고 y= ax+b 같은 예측함수를 파악한다.
# predict 라이브러리에서 test x 값을 넣으면 test y 값과 비슷하게 나오게 하기
# X_train = 1797 * 64, 이미지의 픽셀 64가 1797개로 3차원 디지털 값 배열
# y_train는 0~9의 64 픽셀 이미지가 1797개로 반복되어 있음

plt.imshow(digits.images[digits_index], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()