# coding:utf-8
"""
 test 反射
"""

class A:
    def __init__(self):
        self.name='shijinpu'

    def method(self):
        print 'method print'



if __name__ == '__main__':
    instance = A()
    print getattr(instance,'name', 'name not find')
    print getattr(instance, 'age', 'age not find')

    setattr(instance,'name', 'shkin')
    print getattr(instance, 'name', 'name not find')
    print getattr(instance, 'method', 'method not find')()

    print getattr(instance, 'methods', 'method not find')

