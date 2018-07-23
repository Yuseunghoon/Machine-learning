from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()

X = ['A','B','C','D','A','B']

lb.fit(X)

# X에 존재하는 값 A,B,C,D
print("어떻게 분류 했나 :", lb.classes_)

# A,B,C,D의 라벨 값
print("0과 1로 변형된 값 :", lb.transform(X))

