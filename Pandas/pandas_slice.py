from pandas import Series


'''
house_price = Series([10,20,30,40,50])
print(house_price)
print(house_price[2])

'''
house_price = Series([10,20,30,40,50], index=['강원','인천','전라','제주','서울'])

'''
print(house_price)
print(house_price['전라'])
print("index", house_price.index)
print('value', house_price.values)
'''

print(house_price - 5)
print(house_price[[0,3]])
print(house_price['서울'])