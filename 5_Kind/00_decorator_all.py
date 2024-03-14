"""装饰器"""
"""函数装饰器：
函数装饰器是最常见的一种装饰器，它是一个接收一个函数作为参数，并返回一个新的函数的高阶函数。通过在目标函数定义前使用 @decorator_name 语法应用装饰器，
    可以在不修改原始函数代码的基础上添加额外的功能（如日志记录、性能监控、权限检查等）。
"""


# 1.装饰器(不带参数)
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call.")
        result = func(*args, **kwargs)
        print("After function call.")
        return result

    return wrapper


@simple_decorator
def hello_world():
    print("Hello, world!")


# 2.装饰器(带参数)
def logged_decorator(fix, args1=1):
    def simple_decorator1(func):
        def wrapper(*args, **kwargs):
            print(fix, args1)
            print("Before function call.")
            result = func(*args, **kwargs)
            print("After function call.")

            return result

        return wrapper

    return simple_decorator1


@logged_decorator(fix='11111', args1=2)
def hello_world1():
    print("Hello, world!")


hello_world1()
print('----------------------------------')
"""类装饰器：
类装饰器是定义了一个类，该类实现了 __call__ 方法，使得它的实例可以像函数一样被调用。类装饰器通常用于需要保存状态或更复杂逻辑的情况。
"""


# 3.类装饰器(不带参数)
class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在这里执行前置和后置操作
        print("Decorating with a class...")
        result = self.func(*args, **kwargs)
        return result


@ClassDecorator
def decorated_function():
    pass


# 4.类装饰器(带参数)
class ParametrizedDecorator:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"Using parameters: {self.param1}, {self.param2}")
            # 在这里可以使用传递给装饰器的参数进行自定义操作
            result = func(*args, **kwargs)
            return result

        return wrapper


# 工厂函数用于接收装饰器参数
def create_decorator(param1, param2):
    return ParametrizedDecorator(param1, param2)


# 使用带有参数的装饰器
@create_decorator("value1", "value2")
def my_function():
    print("Function execution")


my_function()


print('----------------------------------')
