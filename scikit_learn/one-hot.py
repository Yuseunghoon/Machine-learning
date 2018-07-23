from sklearn.preprocessing import OneHotEncoder
import numpy as np

ohe = OneHotEncoder()
X = np.array([[2],[1],[0]])
print("X :", X)

print("X onehot result :", ohe.fit_transform(X).toarray())

print("입력 값의 구분 갯수 :", ohe.n_values_)
print("원소들이 어떻게 나누어졌나 :",ohe.feature_indices_)
print("색인값 :", ohe.active_features_)