__author__ = 'numcc'

'''
import os
a = os.path
print(a)


class Abk(object):

    def __init__(self,age,name):
        self.name = name
        self.age = age

    def promison(self,age):
        if age <= 10:
            print("ok")
        else:
            print("no")

    def peo(self):
        print('pep,name:%s,pep,age:%d'%name %age)



a = Abk('tom',18)
print(a.age)
print(a.name)

'''


class Foo(object):

    def hi(self):
        print('hi,Foo')

class Foo2(Foo):

    def hi(self):
        super(Foo2,self).hi()

if __name__ == '__main__':
    foo2 = Foo2()
    foo2.hi()
