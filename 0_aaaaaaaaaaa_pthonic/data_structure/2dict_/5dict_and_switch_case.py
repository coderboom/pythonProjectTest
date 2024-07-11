import operator as op


def calculate(var1, car2, operator):
    """
    模拟switch-case 用法

    :param var1:
    :param car2:
    :param operator:
    :return:
    """
    operator_dict = {
        '+': op.add,
        '-': op.sub,
        '/': op.truediv,
        '*': op.mul
    }
    return operator_dict[operator](var1, car2)


print(calculate(1, 2, '+'))
print('-----------------------------函数是可调用对象--------------------------')
"""
函数在Python中被视为可调用对象（callable object）。
    在Python中，一个对象如果实现了__call__特殊方法，就可以被当作函数一样调用。
    对于常规函数而言，Python----已经内置----了__call__方法的支持，使得它们可以直接被调用。
    
当我们将函数名后跟一对括号（如 func()）时，实际上就是在调用这个函数。
    函数调用时可以传入参数，函数内部会对这些参数进行处理，并根据函数体内的逻辑执行相应的操作，最终可能返回一个结果。
    
    这里的op.add、op.sub、op.truediv和op.mul都是operator模块中的函数，同样作为可调用对象被存储在字典中。
    之后通过operator_dict[operator](var1, car2)的语法动态调用了字典中与operator键关联的函数，完成相应的数学运算。
"""
print('-------------------------------match case---------------------------')
"""match-case
和switch功能类似，甚至更强
"""
