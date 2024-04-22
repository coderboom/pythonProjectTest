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
