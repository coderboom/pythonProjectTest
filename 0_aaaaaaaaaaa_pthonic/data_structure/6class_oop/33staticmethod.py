print("静态方法")

"""类的静态方法 staticmethod 定义了一个函数，但它还做了一件事————它使函数成为一个类变量。
    它的不仅聚合业务领域概念，也可以在合适的场景下节省内存资源的使用。
    
静态方法是一种代码组织与风格。有时一个模块有很多类，并且一些辅助函数在逻辑上与给定的类相关联，而不是与其他类相关联，
    因此不要用许多“自由函数”“污染”模块是有意义的，这时候使用使用静态方法是最合适的。
    比只是为了表明它们是“相关的”就在代码中混合类和函数定义的糟糕风格要来的好多了。


staticmethod的特征：
* 简单的没有隐含参数的函数——————第一个参数不是self或者cls
* 可以作为类或实例的方法调用——————不依赖self、cls
* 使用内建的@staticmethod来创建
* 内聚在类之中，有强烈的归属感,与类要表达的业务逻辑息息相关
* 相对于使用模块级别的函数来说，减少了过多的import
* 子类不需要重新声明就可以使用父类的静态方法
* 子类可以覆盖父类的静态方法

使用场景
工具函数：当一个方法提供了一些通用功能，与类的具体实例无关时，可以使用静态方法。
常量访问：虽然不是最佳实践，但有时静态方法被用来访问类中的常量或执行基于这些常量的计算。
逻辑分组：将一些逻辑上与类相关的功能方法放在类中，即使它们不依赖于实例状态，这样做可以让代码更加组织化和易于理解。

"""

print('------使用静态方法可优化内存大小------')

"""
使用静态方法可优化内存大小——————见 33不含有静态方法的堆栈.png、33含有静态方法的堆栈.png
"""

print('------子类不需要重新声明就可以使用父类的静态方法------')


class A:
    @staticmethod
    def do_some(name):
        return f"super:{name}"

    @staticmethod
    def write(text):
        return F'{text}'


class B(A):

    @staticmethod
    def do_some(name):  # 覆盖类父类的静态方法，实现了需要的逻辑
        return f"SUB:   {name}"

    @classmethod  # 类方法也能调用父类的静态方法
    def some_super_some(cls):
        """在B类的some_super_some方法中，它是类方法，所以cls参数代表B类。
        尽管write是A类的静态方法，但cls（即B类）具有访问其父类A的所有属性和方法的权限，包括静态方法。
        因此，B.some_super_some可以通过cls.write('super')调用A类的write静态方法。

        在这个例子中，some_super_some是一个类方法，它可以通过cls调用A类的静态方法write。
        由于write是静态方法，它不需要cls或self，所以可以跨类调用。
        当some_super_some被调用时，它会使用B类的上下文（即cls），但这并不影响它访问A类的静态方法write。
        """
        return cls.write('super')

    def sub_some(self):
        return self.do_some('TEST')


b = B()
print(b.do_some('----------'))
print(b.sub_some())
print(b.do_some('qaqaqa'))

# 直接调用
print(B.some_super_some())

b2 = B()

print(id(b), id(b2))
print(id(b.do_some('b')), id(b2.do_some('b2')))
"""
4372960208 4434177104
4436188592 4436188592

不同的实例对象，其静态方法是同一个地址。
"""
