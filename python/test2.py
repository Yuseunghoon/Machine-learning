for i in range(1,101):
    print("{} = {}".format(i,(lambda x: x%2 ==0)(i)))


for i in range(1,101):
    if i%2==0:
        print(i, end = ' ')


