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

# 策略模式: 它定义了算法家族, 分别封装起来, 让它们之间可以互相转换, 此模式让算法的变化, 不会影响到使用算法的客户
# 策略与简单工厂结合(将客户端操作转移过来,不需要客户端去判断加减乘除)
# 简单工厂模式 客户端需要认识两个类,Operation,OperationFactory.   策略模式与工厂模式可以让客户端只需要认识一个类OperaContext就行===> 降低耦合
# 这样使得具体算法彻底与客户端分离==> 让算法的父类Operation都不让客户端认识了
class OperaContext():
    def __init__(self,num1,num2):
        self.Operation = Operation(num1,num2)

    def getResult(self,type):
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


"""
策略模式 是一种定义一系列算法的方法, 从概念上来看, 所有这些算法完成的都是相同的工作,只是实现不同,它可以以相同的方式调用所有的算法
        减少了各种算法类与使用算法类之间的耦合
        
        stategy类层次为Context定义了一系列的可供重用的算法或行为.  继承有助于析取出这些算法中的公共功能
        
        另一优点 是简化了单元测试,因为每个算法都有自己的类,可以通过自己的接口单独测试(每个算法可保证它没有错误,修改其中任一
        个时也不会影响其他算法)
        
初期开发中,不得不在客户端的代码中为了判断用哪一个算法而用了switch条件分支,.... 当不同的行为堆砌在一个类中时,就很难避免使用条件
语句来选择合适的行为. 但将这些行为封装在一个个独立的strategy类中,可以在使用这些行为的类中消除条件语句
=====> 尽量减少在客户端的业务逻辑...
=====> 策略模式 封装了 变化!!!!

策略模式就是用来封装算法的,  但在实际中, 我们发现可以用它来封装几乎任何类型的规则, 只要再分析过程中听到需要在不同时间应用不同
的业务规则,就可以考虑使用策略模式处理这种变化的可能性!!!!


缺点与不足:
    因为在OperaContext里还是会用到switch/if判断,也就是当增加一种算法时, 就必须要修改其switch !!!!  

任何需求的变更都是需要成本的!!!!!!

解决 : 反射反射,程序员的快乐....
    
"""














