book=list()
book.append({'name':'Python','year':1992,'company':'비트','page':510,'best':True})
book.append({'name':'Machine Learning','year':2000,'company':'한국','page':433,'best':True})
book.append({'name':'Jave','year': 2004,'company':'비트','page':234,'best':False})
book.append({'name':'Deep Learning','year': 2005,'company':'한국','page':777,'best':True})
book.append({'name':'IoT','year':1999,'company':'한국','page':432,'best':True})

page500=list()
recommend=list()
total=int()
com = set()

print("list")

for b in book:
 print(b)
 
 if b['page']>500:
     page500.append(b['name'])
     
 if b['company']=='비트':
     com.add(b['name'])
     
 if b['best']==True:
     recommend.append(b['name'])
     
 if b['page']:
     total += b['page']

print('\n')
print("500 page up")
print(page500)
print("company 비트")
print(com)
print("best")
print(recommend)
print("total page")
print(total)

