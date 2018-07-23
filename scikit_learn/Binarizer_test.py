from sklearn.preprocessing import Binarizer
import numpy as np

binarizer = Binarizer()

X = np.array([[1,-1],[-1,0],[0,2]])
print("X :", X)
# 디폴트 0의 기준으로 0보다 크면 1, 0보다 작거나 같으면 0 변환
print("변환 값:", binarizer.transform(X))

# 기준점을 1.5로 변경하여 변환
binarizer1 = Binarizer(threshold=1.5)

print("X2",binarizer1.transform(X))