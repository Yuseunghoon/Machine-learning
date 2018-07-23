from pandas import DataFrame, Series

data = {'지역':['서울','서울','서울','인천','인천'],
        '연도':[2010, 2011, 2012, 2011, 2012],
        '가격':[10, 15, 20, 3, 5]
        }
df = DataFrame(data)
df1 = DataFrame(data, columns=['지역','연도','가격','인구'], index=['첫째','둘째','셋째','넷째','다섯째'])
df1.인구 = 100

print(df)
print(df1)
print(df1.columns)
print(df1.values)
print(df1.index)

print(df1.연도)
print(df1['연도'])
print(type(df1['연도']))

print("리스트 인덱싱 :", df1[["연도","지역"]])
print("리스트 인덱싱 type :", type(df1[["연도","지역"]]))

val = Series([500,500], index = ['첫째','넷째'])

df1.인구 = val
print(df1)

del df1['인구']
print(df1)
print(df1.T)