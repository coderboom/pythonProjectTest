"""动态处理对象属性"""
print('----------------------------------------')
"""Python可以借助__getattr__魔术方法来创建和控制处理类的属性。
当我们尝试使用 . 访问属性时，解释器将首先在其上调用__getattribute__内部方法。
假设没有找到该属性，那么该名称将作为参数传递给附加方法 __getattr__()。这样就可用于定义应如何构造和获取对象的返回值。

另外，对于__getattr__, __getattribute__, __setattr__的使用，我们更倾向于用来作为审核的功能。
    譬如日志拦截输出来辅助统计和记录访问过的属性的频率和时间点，还有就是控制访问权限。
    
对于这些魔术方法的使用，也不要过度的把逻辑嵌入到里面去了，要坚持单一职责的原则来设计与使用。
    代码的可维护性和可读性才是我们最应该追求的目标，而不是写出很技巧但是羞涩难懂的难以阅读维护的代码。
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print('** get attribute **', item)
        # return "-------"
        # return super().__getattribute__(item)
        # raise AttributeError(f"no attr {item}")

    def __getattribute__(self, item):
        print("## get attribute ##", item)

        return super().__getattribute__(item)
        # 在子类中重写了 __getattribute__ 方法，
        # 但仍然希望在某些情况下使用父类的 __getattribute__ 行为时，可以使用 super().__getattribute__(item)。
        # 这样，你可以控制何时使用子类的行为，何时使用父类的行为

    # def __setattr__(self, key, value):
    #     pass


person = Person('SSS')
person.age = 123
print(person.__dict__)
# print(person.name, person.age)
print(person.name, person.age, person.text)
""" 只存在方法： def __getattr__(self, item):
输出：
{'name': 'SSS', 'age': 123}
** get attribute ** text
SSS 123 None

它允许类定义对于没有找到的属性（attribute）的访问行为。
    当尝试访问一个不存在的属性时，Python 会自动调用这个方法。这对于动态地处理属性访问、提供默认行为或抛出自定义错误非常有用

调用时机：__getattr__ 只在属性查找失败之后被调用，也就是说，只有当尝试访问的属性没有在实例的字典、类的字典、基类中找到时才会触发。

不适用于特殊属性：对于特殊属性（如 __dict__, __class__）或使用 __getattribute__ 显式定义的属性访问，__getattr__ 不会被调用。

性能考量：频繁调用 __getattr__ 可能会影响性能，因为它在每次属性查找失败时都会被调用。

与 __getattribute__ 的区别：__getattribute__ 更为通用，它在任何属性访问时都会被调用，包括那些已经存在的属性。
    而 __getattr__ 只在属性未找到时被调用，是一个更轻量级的钩子。

应用场景
    动态属性：可以在 __getattr__ 中根据属性名动态生成或返回属性值。
    属性代理：可以用来代理对其他对象的属性访问。
    错误处理：自定义属性访问错误的处理方式，提供更友好的错误信息。
    懒加载：实现属性的懒加载，即在属性第一次被访问时才计算其值。
"""

print("---------------")

"""只存在方法： def __getattribute__(self, item):
输出：
## get attribute ## __dict__
Not Supported
## get attribute ## name
## get attribute ## age
## get attribute ## text
Not Supported Not Supported Not Supported

__getattribute__：它在访问任何对象的属性时都会被调用，无论属性是否存在。
    这个方法允许你完全控制对象属性的访问行为，包括在访问属性时执行额外的逻辑，如日志、验证或缓存。

注意事项
    调用时机：__getattribute__ 在每次属性访问时都会被调用，包括已定义的属性和未定义的属性。
    性能影响：由于每次属性访问都会调用 __getattribute__，因此过度使用可能会对性能产生负面影响，尤其是在大型数据结构中。
    覆盖默认行为：默认情况下，__getattribute__ 会查找实例的 __dict__，类的 __dict__，以及基类的属性。
        如果你重写了这个方法，确保正确处理属性的查找和返回，否则会导致意外的结果。
    与 __getattr__ 的区别：__getattr__ 只在常规查找失败后被调用，而 __getattribute__ 会在每次属性访问时调用，包括已存在的属性。
    
应用场景
    属性访问日志：记录每个属性访问事件。
    属性访问权限控制：在访问属性前进行权限检查。
    属性缓存：实现属性的缓存机制，避免重复计算。
    属性动态定义：在访问时动态决定属性的行为。

"""
print('-----------当__getattribute__和__getattr__-----------------------')
"""当__getattribute__和__getattr__

1、 __getattribute__:
    这是类的一个非常强大的方法，它在尝试访问任何属性时都会被调用，包括那些通过继承或其他方式动态添加的属性。
    如果一个类定义了__getattribute__，那么对于该类实例的每一次属性访问，都会首先调用这个方法，无论该属性是否实际存在。
    这意味着即使访问像self.name这样的常规属性，也会先经过__getattribute__，
        除非在__getattribute__内部显式地调用了父类的实现（比如通过super().__getattribute__(name)）来避免无限递归。
        
2、__getattr__:
    相较之下，__getattr__则是在属性通过正常机制找不到时才被调用。
        也就是说，当尝试访问的属性在实例字典中不存在，且没有在__getattribute__中处理时，才会调用__getattr__。
    它通常用于动态属性的获取，或者作为属性访问失败的一种“回退”机制。
    __getattr__不覆盖继承的属性或类属性，也不影响特殊方法（如__str__）的查找。
    
3、同时存在时的行为:
    当一个类同时定义了__getattribute__和__getattr__，__getattribute__将优先执行。这意味着对于任何属性访问，首先尝试通过__getattribute__处理。
    
    如果在__getattribute__中没有找到属性，也没有显式抛出AttributeError，那么不会自动调用__getattr__。
        只有当__getattribute__内显式地处理未找到的属性并希望触发__getattr__逻辑时，才可能进一步调用__getattr__。
        
    通常，如果在__getattribute__中处理所有属性访问（包括不存在的属性），那么__getattr__可能不会有机会被调用，
        除非__getattribute__明确地将某些操作委托给它。
        
总结来说，__getattribute__提供了更全面的控制，而__getattr__作为补充，在属性无法通过常规手段获取时提供一种额外的处理途径。
    两者同时存在时，__getattribute__的优先级更高，但通过精心设计，可以实现复杂的属性访问逻辑。
"""


class MyClass:
    def __getattribute__(self, name):
        # 对于每一个属性访问，不论是否已定义，都会调用此方法
        print(f"Accessing attribute: {name}")
        return super().__getattribute__(name)
        # 每当尝试访问 MyClass 实例的任何属性时，__getattribute__ 方法都会被调用，并打印出正在访问的属性名。
        # 然后，通过 super().__getattribute__(name) 调用父类的 __getattribute__ 方法，从而继续正常的属性查找流程


class CachingObject:
    def __init__(self):
        self._cache = {}  # 新建一个空的字典，空集合需要用set()

    def __getattribute__(self, name):
        if name == '_cache' or name.startswith('_'):
            # 不缓存私有属性
            return super().__getattribute__(name)

        if name in self._cache.keys():
            return self._cache[name]
        else:
            value = super().__getattribute__(name)
            self._cache[name] = value
            return value


# CachingObject 类实现了属性访问时的缓存机制。只有非私有属性的值会被缓存，当再次访问时，直接从缓存中返回，而不是重新计算
print('-------------------pythonic eg---------------------')


class Context:
    def __init__(self, user: str, roles=None) -> None:
        """

        :type roles: object
        """
        if roles is None:
            roles = []
        self.user = user
        self.roles = set(roles)

    def has_permission(self, role: str) -> bool:
        return role in self.roles

    def grant_permission(self, role: str) -> None:
        self.roles.add(role)


class Project:
    def __init__(self, name: str, price: float, context: Context) -> None:
        self.name = name
        self.price = price
        self.context = context

    def __getattribute__(self, attr):
        if attr == 'price':
            if self.context.has_permission('owner'):
                return super().__getattribute__(attr)
            else:
                raise AttributeError(f"访问属性:{attr}失败。")
        return super().__getattribute__(attr)
        # 调用父类的__getattribute__：
        # 使用super().__getattribute__(name)，你可以直接调用父类的__getattribute__方法来处理属性访问。
        #       这样，当你在当前类的__getattribute__中遇到一个属性访问时，而不是自己处理，你可以让父类的实现来处理这个请求。
        # 这样做可以确保属性查找沿着MRO（Method Resolution Order，方法解析顺序）链进行，避免当前类的__getattribute__再次被调用，从而防止了无限递归。


context = Context('Steven', ['user', 'admin'])
context.grant_permission('owner')
# print(context.has_permission('admin'))
project = Project('Big Project', 16999999.0, context)
print(project.price)
