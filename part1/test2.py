class service:
    secret="영구는 배꼽이 두개"
    name = str()
    def __init__(self,name):
        self.name=name
    def sum(self,a,b):
        result = a+b
        print("%s님 %s+%s=%s 입니다" %(self.name,a,b,result))

pey=service("홍길동")
#pey.__init__()
print(pey.secret)
pey.sum(1,1)
print(dir(pey))

class bookreader:
    __country = 'south korea'
    def set_country(self, country):
        self.__country = country
    def get_country(self):
        return self.__country

aaa=bookreader()

#print(aaa.__country)
print(aaa.get_country())
aaa.set_country('USA')
print(aaa.get_country())

class init:
    def __init__(self, name):
        self.name=name

class book(init):
    def read(self, book):
        self.book=book
        print('%s : %s ' %(self.name, self.book))

class test(book):
    def test(self):
        print('%s : %s ' % (self.name, self.book))
        print(self.name + ' is C++')

#person=book('person')
#person.read('book name')
person=test('person')
person.read('book name')
person.test()


class fourcal:
    def setdata(self,a,b,):
        self.a=a
        self.b=b

    def sum(self):
        result= self.a + self.b
        return result

    def mul(self):
        result= self.a*self.b
        return result

    def sub(self):
        result=self.a-self.b
        return result

    def div(self):
        result= self.a / self.b
        return result

four=fourcal()
four.setdata(10,2)
print(four.sum())
print(four.mul())
print(four.sub())
print(four.div())


import datetime
dt=datetime.datetime.now()
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

dt=datetime.datetime(1992,12,24)
print(dt)
print(datetime.datetime(1999,12,24,2,3,5))

current = datetime.datetime.now()
past = datetime.datetime(1999,12,31)
print(current > past)

diff= current - past
print(diff)
datetime.timedelta(6697,56169,742005)
print(diff.days, diff.seconds, diff.microseconds)

dt = datetime.datetime.now()
print(dt.weekday())
print(dt.date())

print(dt.strftime('%Y/%m/%d'))
print(dt.strftime('%Y-%m-%d / %H:%M:%S / %A'))

str='2017-12-24 23:59'
print(datetime.datetime.strptime(str, '%Y-%m-%d %H:%M'))
print(datetime.datetime(2017, 12, 24, 23, 59))

import math
#import mymath



#import mymod
#print(mymod.add(10,20))
#print(mymod.subtract(10,20))
#print(mymod.multiply(10,20))
#print(mymod.divide(10,20))

#from math import *
#import mymod as m

from math import sin, cos, tan
from mymod import pi,name
print(sin(pi/6), cos(pi/3), tan(pi/4))

print("test modules = " + __name__)
print("mymod modules = " + name)


import mymod
import sys

for key in sys.modules.keys():
    print(key)

import sys
args = sys.argv[1:]
for x in args:
    print(x, end = '')

print(math.factorial(10))
print(math.pow(3,3))
print(3**3)
print(math.sqrt(4))

import re
list = """
primary email : sky1231.d@gmail.com
secondary email : lit_fjek@gmail.com
"""
result_list = re.findall(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)", list)
print(result_list)
for result in result_list:
    print(result)


import random
print(random.random())
print(random.randint(1,6))
print(random.randrange(1,100,3))

seqvar=["짬뽕","짜장면","짬짜면"]
random.shuffle(seqvar)
print(seqvar)
print(random.choice(seqvar))


cek='asdA223'















