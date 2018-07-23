
# 미분해주는 컴퓨터 공식, lim->0의 접선의 기울기
def getDifferential(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h))/(2*h)

def equation1(x):
    return 10*x**3 + 5*x**2 + 4*x

def equation2(x):
    return 0.01 * x**2 + 0.1*x

d = getDifferential(equation1,5)
print(d)

a = getDifferential(equation2,10)
print(a)

#식 f= x**2 +y**2
#점 x=3, y=4에서의 편미분을 구하시오

def function_1(x):
    return x*x + 4.0 **2.0

print(getDifferential(function_1,3))

def function_2(y):
    return 3.0 ** 2.0 + y*y

print(getDifferential(function_1, 4.0))