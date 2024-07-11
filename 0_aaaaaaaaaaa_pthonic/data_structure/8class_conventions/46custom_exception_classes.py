import string

print('自定义异常类')

"""
Python 带有一系列异常类型和相应的处理程序类。有时，在编写自己的软件时，您可能想要创建自己的自定义异常。
它们不仅有助于为调试代码中的错误添加更多信息，而且还可以在适当的时候保持代码库的可维护性。
自定义的异常类要从业务角度出发去定义和衍生。不能随意，否则项目规模变化后会有很多模糊的界限产生，带来不必要的维护成本。
通过对官方的 EAFP——“求原谅比求许可更容易” 和 LYBL——“先查看后跳跃”进行讲解”，让大家了解两种不同的编风格以便在实际中选择。
同时从代码易维护和可读性的角度强调了编码规范的一些要点。
"""

MIN_PASSWORD_LENGTH = 12
EMPTY_SET = set()


class InvalidPasswordError(ValueError):
    def __init__(self, *args):
        # if args is None:
        #     self.args = ()
        # 简化了对 args 的处理，因为 args 在没有显式传入时默认为空元组,所以上面两行代码可不用
        self.args = args

    def __call__(self):
        return f"{self.args}"


def less_length(password: str, min_length: int) -> bool:
    if not isinstance(min_length, int) or min_length <= 0:
        raise ValueError("min_length must be a positive integer")
    return len(password) < min_length


def lack_of_lowercase(password: str) -> bool:
    return set(password) & set(string.ascii_lowercase) == EMPTY_SET


def lack_of_uppercase(password: str) -> bool:
    return set(password) & set(string.ascii_uppercase) == EMPTY_SET


def lack_of_digits(password: str) -> bool:
    return set(password) & set(string.digits) == EMPTY_SET


def lack_of_punctuation(password: str) -> bool:
    return set(password) & set(string.punctuation) == EMPTY_SET


def validate_password(
        password: str,
        min_length: MIN_PASSWORD_LENGTH) -> bool:
    # a = False
    # 对 min_length 进行了类型和值的检查
    if not isinstance(min_length, int) or min_length <= 0:
        raise ValueError("min_length must be a positive integer")
    
    if (less_length(password, min_length) or
            lack_of_lowercase(password) or
            lack_of_uppercase(password) or
            lack_of_digits(password) or
            lack_of_punctuation(password)):  # 有一个条件为真时就会触发raise ValueError，只有都为false时才会执行判断执行体demo
        raise InvalidPasswordError('password is bad')
    print('password is OK')

    return True


validate_password('a6d54', 12)

"""
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
"""
