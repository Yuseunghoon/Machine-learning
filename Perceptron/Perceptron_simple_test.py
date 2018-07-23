# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:46:11 2017

@author: BEAST
"""
# 퍼셉트론의 classificatin 확장.
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:18:43 2017

@author: BEAST
"""

import numpy as np
import matplotlib.pyplot as plt
# import sklearn.linear_model.perceptron as p
from sklearn.linear_model import Perceptron

# Needed to show the plots inline
# %matplotlib inline
# Data

colormap = np.array(['r', 'k'])


def make_cal(X_train, y_train):
    # Create the model
    net = Perceptron(max_iter=100, verbose=0, random_state=1, fit_intercept=True, eta0=0.002)
    net.fit(X_train, y_train)  # X_train의 점들과 점의 목표값인 0, 1를 가지고 머신러닝

    # Print the results
    print("Actual     " + str(y_train))
    print("Prediction :", net.predict(X_train)) # 점 여러개를 0, 1 로 예측
    print("Accuracy :", net.score(X_train, y_train)) # X_train의 예측값이 y_train과 얼마나 같은지

    # Plot the original data
    plt.scatter(X_train[:, 0], X_train[:, 1], c=colormap[y_train], s=40)
    # plt.scatter(X_train[:,0], X_train[:,1], c=colormap[y_train], s=40)


    # Output the values
    print("Coefficient 1:", net.coef_[0, 0])
    print("Coefficient 2:", net.coef_[0, 1])
    print("Bias :", net.intercept_)


    # Calc the hyperplane (decision boundary)
    plt.ylim([0, 10])
    ymin, ymax = plt.ylim()

    print('ymin :', ymin, 'ymax :', ymax)

    w1 = net.coef_[0] # 가중치 w0, w1
    a1 = -w1[1]/w1[0]

    xx1 = np.linspace(ymin, ymax)
    yy1 = a1 * xx1 -(net.intercept_[0]/w1[0])

    # Plot the line
    plt.plot(yy1, xx1, 'k-')
    plt.show()





X_train = np.array([[2, 2], [1, 3], [2, 3], [5, 3], [7, 3], [2, 4],
                    [3, 4], [6, 4], [1, 5], [2, 5], [5, 5], [4, 6], [6, 6], [5, 9]])

# Labels
y_train = np.array([0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1])

make_cal(X_train, y_train)





