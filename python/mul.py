num_in=input("num : ")
num=int(num_in)

i=0
for x in range(1,10):
    print("{} * {} = {}".format(num, x, num*x), end='\n')


print("\n문자열 대소문자 변경")

a=input("input = ")
print(a.swapcase())

print("\n문자열 역순")
print(a[::-1])
