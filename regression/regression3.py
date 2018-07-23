from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

X_train = np.array([[10],[20],[30],[50]])
y_train = np.array([[25],[45],[65],[105]])

model = LinearRegression(fit_intercept = True)
model.fit(X_train, y_train)

X_test = 40
y_predict = model.predict(X_test)

y_pred = model.predict(X_train)
mse = mean_squared_error(y_train, y_pred)
print(mse)

print("가중치:", model.coef_)
print("상수 :", model.intercept_)
print("예측값:","x 값:", X_test, "y_predict", y_predict)