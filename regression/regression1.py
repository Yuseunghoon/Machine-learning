import matplotlib.pyplot as plt
import numpy as np

def predict(x):
    return w0 + w1 *x

sample_data = [[10,25], [20, 45], [30,65], [50, 105]]

X_train = []
y_train = []

X_train_a = []
y_train_a = []

total_size = 0
sum_xy = 0
sum_x = 0
sum_y = 0
sum_x_square = 0

for row in sample_data:
    X_train = row[0]
    y_train = row[1]
    X_train_a.append(row[0])
    y_train_a.append(row[1])
    sum_xy += X_train
    sum_y += y_train
    sum_x_square += X_train * X_train
    total_size += 1

w1 = (total_size * sum_xy - sum_x * sum_y) / (total_size * sum_x_square - sum_x * sum_x)
w0 = (sum_x_square * sum_y - sum_xy * sum_x) / (total_size * sum_x_square - sum_x * sum_x)

X_test = 40
y_predict = predict(X_test)

print("가중치:", w1)
print("상수:", w0)
print("예상 값:", "x값:", X_test, "y_predict:", y_predict)

plt.scatter(X_train_a,y_train_a)
plt.scatter(X_test,y_predict)
plt.plot(X_train_a,y_train_a)
plt.show()