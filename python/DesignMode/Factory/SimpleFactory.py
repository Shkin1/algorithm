# coding:utf-8

__author__ = 'Pushkin'
__date__='$2018-01-28$'

"""
简单工厂模式(Simple Factory Pattern):是通过专门定义一个类来负责创建其他类的实例，被创建的实例通常都具有共同的父类.

用任意一种面向对象语言实现一个计算器控制台程序。要求输入两个数和运算符号，得到结果

"""

class Operation():
    def __init__(self,number1=0, number2=0):
        self.num1 = number1
        self.num2 = number2

    def getResult(self):
        pass
    pass


class OperationAdd(Operation):
    def getResult(self):
        return self.num1 + self.num2

class OperationSub(Operation):
    def getResult(self):
        return self.num1 - self.num2

class OperationMul(Operation):
    def getResult(self):
        return self.num1*self.num2

# 除法
class OperationDiv(Operation):
    def getResult(self):
        if self.num2 == 0:
            return 'not allow 0'
        return self.num1/self.num2

# 其他操作
class OperationUndef(Operation):
    def getResult(self):
        return '操作符错误'



class OperationFactory(object):
    def choose_oper(self,type):
        if type =='+':
            return OperationAdd()
        elif type == '-':
            return OperationSub()
        elif type == '*':
            return OperationMul()
        elif type == '/':
            return OperationDiv()
        else:
            return OperationUndef()

if __name__ == "__main__":
    type = ''
    while not type =='0':
        num1 = input('请输入第一个数值: ')
        oper = str(raw_input('请输入一个四则运算符: '))
        num2 = input('请输入第二个数值: ')
        of = OperationFactory()
        oper_obj = of.choose_oper(oper)
        oper_obj.num1 = num1
        oper_obj.num2 = num2
        print '运算结果为: ', oper_obj.getResult()

















