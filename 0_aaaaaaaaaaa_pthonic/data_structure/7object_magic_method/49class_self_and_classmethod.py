print(' 带有类属性的 self 或 classmethod')
print('---------------------------------')
"""
类级属性不需要类的实例即可使用。
    使用类属性在类继承的情况下，需要注意传递类的知识以及类的上下文，才能够让子类能够在继承复用父类功能的前提下，有这更好的扩展，而不会产生歧义。
"""


class Component:
    __tag__ = 'com'

    def get_tag(self):
        return Component.__tag__


class ListComponent(Component):
    __tag__ = 'List'


list_component = Component()
print(list_component.get_tag())  # com 是因为get_tag() 被写死了，失去了灵活性

print('==================== pythonic 方式解决继承中的冲突======================')
print('写法一')


class Component1:
    __tag__ = 'com'

    def get_tag(self):
        return self.__tag__  # self 代表了将来的子类；还要保证子类的实例变量和类变量不重名


print('写法二')


class Component2:
    __tag__ = 'com'

    def get_tag(self):  # 写法二 的方法 1
        """
        这段代码的作用是获取当前对象 self 的类。
            self 是指向实例对象的引用
            __class__ 是一个特殊属性，用于获取对象所属的类。
        """
        cls = self.__class__
        return cls.__tag__

    @classmethod
    def get_component_tags(cls):  # 写法二 的方法 2
        return cls.__tag__


class ListComponent2(Component2):
    __tag__ = 'List'


list_component2 = ListComponent2()
print(list_component2.get_tag())  # List
print(list_component2.get_component_tags())  # List
"""
1、查找子类: 首先，Python会在子类中查找这个方法。如果子类定义了get_component_tags方法，那么将执行子类中的版本。
2、查找父类: 如果子类没有定义get_component_tags方法，Python将继续在父类中查找。在这个例子中，它会找到定义在父类中的get_component_tags方法。
3、执行方法: 执行找到的get_component_tags方法。由于这是一个类方法，它会使用cls参数引用调用方法的类（这里是子类）。
4、访问__tag__属性: 方法内部尝试访问cls.__tag__。如果子类有自己的__tag__属性，那么将返回子类的__tag__；如果没有，Python会继续在父类中查找__tag__属性。

因此，当子类的实例调用get_component_tags时，它实际上是在获取子类（如果有定义的话）或继承自父类的__tag__属性的值。这体现了Python的多态性和继承特性。
"""
