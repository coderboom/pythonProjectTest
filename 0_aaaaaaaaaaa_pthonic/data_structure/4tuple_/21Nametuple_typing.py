from typing import NamedTuple

"""
typing模块是Python标准库的一部分，它引入了类型提示（Type Hints）的支持，帮助程序员编写更易于理解和维护的代码。
    在typing模块中，NamedTuple是一个类工厂，用于创建具有命名字段的元组子类，类似于collections.namedtuple，但提供了额外的类型注解功能。

以下是typing.NamedTuple的详细说明：
"""


class Employee(NamedTuple):
    name: str
    age: int
    title: str
    department: str


"""在这个例子中，我们定义了一个名为Employee的NamedTuple子类，
    它有四个字段：name（类型为str）、age（类型为int）、title（类型为str）和department（类型也为str）。
    类型注解提供了额外的信息，有助于静态分析工具、IDEs等提供更好的代码补全、类型检查等功能。
"""

john_doe = Employee('John Doe', 30, 'Software Engineer', 'Engineering')

"""
类型安全: 
    typing.NamedTuple支持类型注解，提高了代码的可读性和静态类型检查的准确性。
    
不可变性: 
    和collections.namedtuple一样，typing.NamedTuple创建的对象也是不可变的，保证了数据的安全性。
    
性能: 
    由于是元组的子类，NamedTuple实例在内存中占用的空间较小，访问速度快。
    
语法糖: 
    提供了一种更接近类定义的语法来创建命名元组，使得代码更加直观。
    
与collections.namedtuple的区别
    尽管两者都用于创建具有命名字段的元组，typing.NamedTuple的主要优势在于它支持类型注解，更适合在需要类型提示的现代Python代码中使用。
    而collections.namedtuple则在Python早期版本中就已经存在，不支持直接的类型注解，但使用上可能稍微简洁一些，特别是在不需要类型提示的场景下。
    
总结
typing.NamedTuple是Python类型提示系统的一部分，它允许你创建具有命名字段和类型注解的元组子类，增强了代码的自我文档化能力和静态分析工具的支持。在追求代码清晰度和类型安全的项目中，它是定义简单数据结构的优选方式。
"""

# john_doe['name'] = 'iavhdsiha'
# #TypeError: 'Employee' object does not support item assignment
