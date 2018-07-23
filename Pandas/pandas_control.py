from pandas import DataFrame, Series

s = Series([1,2,3, None, 5])
print('Series count :', s.count())

data = {'연도': [2010, 2011, 2012, 2011, 2012],
        '가격': [10, 15, 20, None, 5]
}


s1 = DataFrame(data)
print(s1)
print(s1.count())

s2 = DataFrame(data)

print('sum : ', s2.sum())

s3 = s2.T
print(s3)
print(s3.sum(axis=1))