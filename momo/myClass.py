import sys


class MyClass(object):
    def __init__(self):
        pass

    def __myPrivateFunction(self):
        print('On est dans myPrivateFunction de MyClass')

    def myPublicFunction(self):
        print('On est dans myPublicFunction de MyClass')


class MyInheritedClass(MyClass):
    def __init__(self):
        super

    def myPublicFunction(self):
        print('On est dans myPublicFunction de MyInheritedClass')


myClass = MyClass()
myClass.myPublicFunction()
myInherited = MyInheritedClass()
myInherited.myPublicFunction()


