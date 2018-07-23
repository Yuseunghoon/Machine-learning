import pandas as pd

iris2 = pd.read_csv('C:/Users/bit-user/PycharmProjects/test/Pandas/iris2.txt', sep='\s+',
                    names=['sl', 'sw', 'pl', 'pw', 'regression'])

# skiprows = [0,1] 1, 2줄 행 제외

print(iris2)

iris2.to_csv('C:/Users/bit-user/PycharmProjects/test/Pandas/iris2.csv')
