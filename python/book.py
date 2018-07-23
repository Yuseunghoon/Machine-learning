book = ['Python','Machine Learning','Jave','Deep Learning','IoT']
year = [1992,2000,2004,2005,2007]
com = ['비트','한국','비트','한국','한국']
page = [510,380,400,600,550]
best = [True,True,False,True,True]

list=[[book],[year],[com],[page],[best]]

i=0

for num in book:
 list[i]=[book[i],year[i],com[i],page[i],best[i]]
 print(list[i], end='\n')
 i+=1




