print('python 对象是 区分类变量和实例变量')
"""
Python 对象区分实例变量和类变量。类的范围内定义的方法和属性独立于类的任何实例。它们将信息保存在类级别，并且每个实例化对象都可以访问相同的类变量。利用类变量可以在类的所有实例之间共享信息。
另一方面，实例变量特定于创建的对象。这些变量的信息存储在特定于该对象的内存中。它们独立于其他实例变量。
相同的名称实例变量比类变量具有更高的优先级。
通过实例的展示和图例的分析加上源代码的分析，知道这些陷阱的来龙去脉，底层原理，让大家可以在实际生产中避开这些陷阱。
"""


class Laptop:
    category = 'computer'

    def __init__(self, name, price):
        self.name = name
        self.price = price


print(Laptop.category)  # computer
mac_book = Laptop('mac book', 8999898)
asus_book = Laptop('asus book', 222222222)
print(mac_book.category)  # computer
print(asus_book.category)  # computer

Laptop.category = 'Iphone'
print(Laptop.category)  # Iphone
print(mac_book.category)  # Iphone
asus_book.category = 'PCCCCC'  # 其实是创建了一个实例属性，覆盖了类属性
print(asus_book.category)  # PCCCCC
print(asus_book.__class__.category)  # Iphone
"""
类属性访问：
    当你最初打印 asus_book.category 时，它实际上访问的是类 Laptop 的 category 属性，因为在实例上没有定义这个属性时，Python会去类中查找。
    此时，由于之前已经将 Laptop.category 改为了 'Iphone'，所以输出为 'Iphone'。
    
实例属性赋值：
    执行 asus_book.category = 'PCCCCC' 时，你实际上在 asus_book 这个实例上创建了一个新的名为 category 的属性，
    这个属性遮蔽（shadow）了从类 Laptop 继承来的 category 属性。
    因此，当你紧接着打印 asus_book.category 时，它现在显示的是实例级别的属性值 'PCCCCC'。
    
类属性访问再次尝试：
    当你使用 asus_book.__class__.category 时，这实际上直接访问了类 Laptop 的 category 属性，完全绕过了实例属性。
    由于之前已经把类的 category 改为了 'Iphone'，并且这个类属性没有再被修改过，所以输出为 'Iphone'。
    
总结来说:
    asus_book.category = 'PCCCCC' 创建了一个与实例 asus_book 相关联的局部（实例）属性，它覆盖了从类继承的同名属性，但并没有改变类本身的 category 属性。
    而 asus_book.__class__.category 则是直接访问类的属性，不受实例属性的影响。
"""
