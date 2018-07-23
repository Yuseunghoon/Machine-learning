import pandas as pd

iris = pd.read_csv('C:/Users/bit-user/PycharmProjects/test/Pandas/iris.csv',
                    names = ['sl','sw','pl','pw','regression'])
print(iris)
print(type(iris))

print('head(5) :', iris.head()) # 앞에서 5개
print('tail(3) :', iris.tail()) # 뒤에서 5개

