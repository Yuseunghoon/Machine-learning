import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

def predict(x):
    return w0 + w1 * x

X1 = np.array([[10],[20],[30],[50]])
y_label = np.array([[25],[45],[65],[105]])

X_train = sm.add_constant(X1)

w = np.dot(np.dot(np.linalg.inv(np.dot(X_train.T, X_train)), X_train.T), y_label)

w0 = w[0]
w1= w[1]

X_test = 40
y_predict = predict(X_test)

print("가중치",w1)
print("상수",w0)
print("x 값:", X_test,  "y_predic :", y_predict)