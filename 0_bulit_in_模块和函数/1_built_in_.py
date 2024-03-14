import builtins
import time

print(dir(builtins))  # dir() 返回一个包含对象的属性名的列表
"""
builtins 在 Python 中是一个内置模块，它包含了所有在标准 Python 环境中可以直接使用的内建函数和异常类。
当你在编写 Python 代码时，无需显式导入 builtins 模块就能使用这些内建函数，比如 len(), print(), type(), divmod() 等。
当存在一个用户自定义的函数或变量与内建函数同名时，为了访问原始内建版本，可以通过 builtins 模块来引用：
"""
"""
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 
'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 
'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 
'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError',
'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError',
'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', 
'__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 
'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 
'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 
'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 
'sum', 'super', 'tuple', 'type', 'vars', 'zip']
"""

print(dir())
print(dir(time))

"""
 _ 
 用途1、在交互模式下使用_可查看最后一次计算的结果。
 用途2、伪装名称为_的变量，表示不会使用的变量。 
"""
# 进行10次操作，不关心序号
print(sum(1 for _ in range(10)))  # 不管元素是什么，都不使用其值
# 拆包，只接受第一个参数
head, *_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(head)  # 1
print(_)
_, second, _ = (1, 5, 9)
print(_)  # 9
print(second)  # 5
#
# import builtins
#
# print(builtins.__name__)  # 用import导入，可以获取模块名

# if __name__ == '__main__':  # 如果直接使用，那么__name__就是__main__
#     print(__name__)
a = range(1, 20, 3)
print(a)
print(id(a))
print(type(a))
print(dir(a))
b = ['count', 'index', 'start', 'step', 'stop']

print(list(a))
print(a.count(10))
print(a.index(16))
print(a.start, a.step, a.stop, sep=',')
print(a[1:4])  # 取出第2到第4个元素的子对象

print(help())

print(b.__class__)
