import  statsmodels.api as sm
import  numpy as np

X1 = np.array([[10],[20],[30],[50]])

X_train = sm.add_constant(X1) # 각행 1열에 1 추가
print(X_train)
print(X_train.shape)

# X1. shape : (4,1)

print(np.ones((X1.shape[0],1))) # 4행 1열로 1 입력
X_train1 = np.hstack([np.ones((X1.shape[0], 1)), X1]) # 각 행렬의 인덱스를 한 행렬로 행에 맞게 합침
print(X_train1)