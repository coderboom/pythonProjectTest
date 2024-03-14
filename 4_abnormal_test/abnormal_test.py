'''没有结束循环的语句出现，这个程序会一直循环下去，直到用户输入一个有效的数字。'''
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

'''
try 语句的工作原理
1、首先，执行try子句（try 和 except 关键字之间的（多行）语句）。
2、如果没有触发异常，则跳过 except 子句，try 语句执行完毕。
3、如果在执行 try 子句的过程中触发异常，则停止执行 try 子句剩下的子句，开始执行 except 子句。
    如果异常的类型与 except 关键字后指定的异常相匹配，则会执行 except 子句，然后跳到 try/except 代码块之后继续执行。
4、如果发生的异常与 except 子句 中指定的异常不匹配，则它会被传递到外层的 try 语句中；
    如果没有找到处理句柄，则它是一个 未处理异常 且执行将停止并输出一条错误消息。
    注释：如果在Python程序中一个异常没有被任何except子句捕获，
        那么这个异常将会沿着调用栈向上冒泡，直到找到能够处理它的异常处理器（即另一个包含适当except子句的try-except块，或者全局的异常处理器）。
        如果没有在任何地方被捕获，那么当异常到达主程序级别时，程序会终止运行，并打印出未捕获异常的信息以及回溯（traceback），显示引发异常的代码位置。
        简而言之，如果没有捕获特定异常，则：
        异常将不会在当前try-except-finally结构内部得到处理。
        控制权将跳出当前try块并继续寻找上层调用栈中合适的异常处理机制。
        如果在整个程序范围内都没有找到合适的异常处理机制，则程序会终止执行，输出错误信息到标准错误流（stderr）并在控制台上显示出错信息和堆栈跟踪。
        
'''
print('1111111')
'''except 子句 可能会在异常名称后面指定一个变量。 这个变量将被绑定到异常实例，
该实例通常会有一个存储参数的 args 属性。 为了方便起见，
内置异常类型定义了 __str__() 来打印所有参数而不必显式地访问 .args。'''
# try:
#     # raise Exception('bbbb')
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)
'''
未处理异常的 __str__() 输出会被打印为该异常消息的最后部分 ('detail')。
BaseException 是所有异常的共同基类。它的一个子类， Exception ，是所有非致命异常的基类。
不是 Exception 的子类的异常通常不被处理，因为它们被用来指示程序应该终止。
它们包括由 sys.exit() 引发的 SystemExit ，以及当用户希望中断程序时引发的 KeyboardInterrupt 。
Exception 可以被用作通配符，捕获（几乎）一切。
然而，好的做法是，尽可能具体地说明我们打算处理的异常类型，并允许任何意外的异常传播下去。
'''
# print('w2w22222222')
# '''raise 支持强制触发指定的异常 '''
# raise NameError('HiThere')
# 参数是要触发的异常，这个参数必须是异常实例或异常类（派生自 BaseException 类，例如 Exception 或其子类）。
# 如果传递的是异常类，将通过调用没有参数的构造函数来隐式实例化

'''
如果一个未处理的异常发生在 except 部分内，它将会有被处理的异常附加到它上面，并包括在错误信息中
'''
'''
为了表明一个异常是另一个异常的直接后果， raise 语句允许一个可选的 from 子句
'''

# raise RuntimeError from exc
# def func():
#     raise ConnectionError
#
#
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc
#     # 表明Connection是导致Runtime的原因
#     # 使用 from None 表达禁用自动异常链

'''
自定义异常类 继承 BaseException 类，而不是 Exception 类
'''

'''try 语句的 finally 子句,  用于执行一些语句（清理操作），无论 try 语句成功或失败'''
# try:
#     print('try')
#     raise Exception('error')
# except Exception as e:
#     print('except:', e)
# finally:
#     print('finally')
#
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

'''
如果存在 finally 子句，则 finally 子句是 try 语句结束前执行的最后一项任务。
不论 try 语句是否触发异常，都会执行 finally 子句。以下内容介绍了几种比较复杂的触发异常情景：
1、如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。
    如果该异常没有 except 子句处理，在 finally 子句执行后会被重新触发。
2、except 或 else 子句执行期间也会触发异常。同样，该异常会在 finally 子句执行之后被重新触发。
3、如果 finally 子句中包含 break、continue 或 return 等语句，异常将不会被重新引发。
4、如果执行 try 语句时遇到 break,、continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。
5、如果 finally 子句中包含 return 语句，则返回值来自 finally 子句的某个 return 语句的返回值，而不是来自 try 子句的 return 语句的返回值。
'''

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
#
#
# print(bool_return())  # 上述第5种情况

'''
如果一个异常在try块中产生，并且没有匹配的except子句处理它，在finally子句执行完毕后，
该异常将继续向上冒泡到调用栈的更上层，直到找到能够捕获并处理它的异常处理器，或者在全局范围内未被捕获导致程序终止。

注：调用栈（Call Stack）是编程中的一种数据结构，它用于存储函数调用的上下文信息。
当一个程序运行时，每当发生函数调用，调用的信息（如函数参数、局部变量等）会被压入调用栈中形成一个新的栈帧（Stack Frame）。随着函数调用的嵌套，调用栈会不断增长。
当一个函数执行完毕并返回时，对应的栈帧将从调用栈中弹出，控制权返回到调用它的上一层函数，并恢复该层函数的执行环境。
在Python中，当异常发生且未被捕获时，解释器会从当前栈帧开始查找最近的能够处理该异常的except子句，如果在当前函数内部没有找到匹配的处理器，则异常会向上冒泡，即转到调用栈中的上一个函数继续寻找。
这个过程会一直持续到找到合适的异常处理器，或者到达全局作用域仍未捕获异常，此时程序将会终止，并显示错误信息和调用栈回溯（traceback），帮助开发者定位异常发生的准确位置。
'''

print('333333333333')
'''在有些情况下，有必要报告几个已经发生的异常。
这通常是在并发框架中当几个任务并行失败时的情况，但也有其他的用例，有时需要是继续执行并收集多个错误而不是引发第一个异常。
内置的 ExceptionGroup 打包了一个异常实例的列表，这样它们就可以一起被引发。它本身就是一个异常，所以它可以像其他异常一样被捕获。
'''


# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)
#
#
# # f()
# try:
#     f()
# except Exception as e:
#     print(f'caugh {type(e)}:e')
#
def f():
    raise ExceptionGroup("group1",
                         [OSError(1), SystemError(2), ExceptionGroup("group2", [OSError(3), RecursionError(4)])]
                         )


try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")


