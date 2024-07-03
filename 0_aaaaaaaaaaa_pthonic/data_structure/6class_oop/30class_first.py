print('----')
"""面向对象编程是一种范式，它使开发人员能够借助称为类的通用蓝图创建虚拟对象。面向对象的模型简化了创建程序的过程，让意大利面条代码都可以用非常结构化的方式编写。
Python 作为一种语言，支持多种范式。这意味着开发人员不必总是使用 OOP，可以自由选择最适合用例的范式，或者随着项目的发展在编写 Python 代码时从多种范式中进行选择。
在 Python 中，一切都被视为类的实例或对象——它们包含有关实体的数据结构和元信息

Python 类的约定
当我们开始学习 Python 时，让我们着迷的一个特性是，我们不需要每次编写一段代码时都创建一个类，这与 Java 不同。
灵活性对学习者来说是件好事，但是当您开始处理大型 Python 项目时，您会意识到类确实很有意义。 Python 3 捆绑了几个面向对象的特性和改进。
我们将研究 Python 中类的一些突出的和鲜为人知的特性，这些特性将有助于编写更好的可维护代码。

优化类的大小
把一大堆东西塞进一个类是很糟糕的。特别是对于已经获得专业或受过编程培训的开发人员来说，困境总是在于类和模块的明确定义。
何时应该停止向类添加功能以及何时将功能拆分为单独的类？其中大部分来自随着时间的推移的经验。
但这里有一些指针，如下所示：
Single Responsibility Principle (SRP): 如果您评估您的类具有明确定义的单一职责或工作单元，并且您可以轻松地将其与其他类区分开来，那么您不必太在意代码行数或类的大小。
在一个文件中编写一个类的代码，这是最清晰的划分方式。但是，在某些情况下，您可能在同一个文件中有多个紧密耦合的类。
评估每个方法和代码单元的适合性，以确保它属于该类的责任范围。
找到重复或复制的代码是一个信号，表明您的类可能做的比预期的要多。需要将其拆分为不同的部分以隔离重叠的代码。
如果当前类做不止一件事，是时候创建一个不同的类了。
在开始项目之前确定类、模块和包结构的范围至关重要，并且要遵守设计，这有助于解决大多数较大的类问题。
"""


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def is_old(self):
        return self.age > 10

    def out_put(self):
        print(f"My name is :{self.name}")

    def out_put_json(self):
        print(F"out put json{self.age}")


"""上面一个类把所有事情都做类，可以把输出拆分开，简单化User类，让类简单简洁化

用一个专门的类来控制打印、日志写出或写入数据库等
"""


class User1:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def is_old(self):
        return self.age > 10


class PrintOutPut:

    def out_put(self, user: User1):
        print(f"My name is :{user.name}")

    def out_put_json(self, user: User1):
        print(F"out put json{user.age}")


p_out_put = PrintOutPut()
p_out_put.out_put(User1('abcd', 29))

print('------------------------')
