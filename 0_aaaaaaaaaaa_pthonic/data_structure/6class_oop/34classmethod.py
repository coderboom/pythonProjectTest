"""类方法"""
import json

"""
类方法是通过classmethod装饰器定义的，它与类而不是与类的实例相关联。
以下是类方法的一些关键点：

定义： 使用@classmethod装饰器来定义一个类方法。类方法的第一个参数是cls，代表类本身，而不是实例对象
   class MyClass:
       @classmethod
       def class_method(cls):
           print(f"This is a class method, and the class is {cls}")

调用： 类方法可以通过类名或者类的实例来调用，但它们总是接收类作为第一个参数，而不是实例。

作用：
    类方法通常用于操作类的属性或行为，而不需要实例化对象。
    它们可以用来创建工厂方法，即根据某些条件返回不同类型的实例。
    类方法可以修改类的元信息，如添加或删除类属性。
    
区别于实例方法：
    实例方法的第一个参数通常是self，代表对象实例，类方法则是cls，代表类本身。
    实例方法可以直接访问实例的属性，而类方法只能通过cls访问类属性。
    
区别于静态方法：
    静态方法不接收self或cls作为参数，它们完全独立于类和实例，只是在类的上下文中定义的普通函数。
    类方法可以访问类的信息，而静态方法不能。
----------------------------------------------------------------
总结：
    类方法可以通过类对象或者实例对象调用。如果是通过实例对象调用的，那么实例对象会被忽略，通过间接转换为其类对象进行调用。
        类对象，会以参数形式传给类方法，作为类方法的第一个参数，也就是cls参数。
        
    类方法在多个实例中都只有一个内存片段来存储方法实体，所以对大量的对象的场景下是有优势的。
    
    类方法与静态方法很多相似之处，除了第一个cls参数不一样之外，其他都雷同。也可以通过子类继承父类进行override父类的类方法达到行为修改的目的。
    
    在实际的应用场景中，类方法作为工厂方法实例化不同的对象可以简化调用方的使用，把初始化逻辑封装在了工厂方法之内，
        让调用者不需要知道太多的内部的逻辑与知识，是一种好的编程实践体验。
----------------------------------------------------------------

例子： 以下是一个使用类方法的例子，它创建了一个工厂方法来根据类型创建不同的对象：
"""


class Product:
    MULTI = 5

    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Product: {self.name} - {self.weight}g"

    @classmethod
    def from_dict(cls, data: dict):
        name = data.get('name')
        weight = data.get('weight')
        actual_weight = weight * cls.MULTI
        return Product(name, actual_weight)

    @classmethod
    def from_json(cls, data: str):
        data_dict = json.loads(data)
        return cls.from_dict(data_dict)


product = Product.from_dict({'name': 'Toy', 'weight': 99})
print(product)
product_one = Product.from_json('{"name":"Bond","weight":88}')
print(product_one)

print('------------------------------------')

"""
类方法（@classmethod）是通过类来调用的，它们继承到子类中，并且在子类中仍然可以以类方法的身份被调用。
    类方法的主要特点是可以访问到调用它的类对象，而不直接与类的实例相关联。

以下是关于类方法继承的一些要点：
    继承：子类会自动继承父类的所有非私有（非_开头）的方法，包括类方法、静态方法。这意味着，如果父类有一个类方法，子类无需重新定义，就可以直接使用。
    
    调用：子类可以通过自己的类名或实例来调用继承的类方法。调用时，类方法的cls参数会被设置为调用它的类对象。
        如果是通过子类实例调用，cls将是子类；如果是通过子类名调用，cls将是子类。
        
    覆盖：如果子类定义了与父类同名的类方法，那么子类的类方法会覆盖父类的类方法。
        子类的这个方法会被调用，而不会调用父类的对应方法，除非显式地通过父类名调用。
        
    访问父类的类方法：子类的类方法可以使用super()函数或者直接通过父类名称来调用父类的类方法，如果需要保持原有的行为。
"""


class AdvanceProduct(Product):
    UP_VALUE = 2

    def __repr__(self):
        return f"Advance_Product: {self.name} - {self.weight}g"

    @classmethod
    def from_dict(cls, data: dict):
        name = data.get('name')
        weight = data.get('weight')
        actual_weight = weight * (cls.MULTI + cls.UP_VALUE)
        return Product(name, actual_weight)


product = AdvanceProduct.from_dict({'name': 'Toy', 'weight': 99})
print(product)

products = [AdvanceProduct(f"Ton - {i}", i * 3) for i in range(1, 11)]
for p in products:
    print(id(p), id(p.from_dict))
"""
4529302864 4531440512
4374036176 4531440512
4531373456 4531440512
4531373648 4531440512
4531376592 4531440512
4529410640 4531440512
4529406160 4531440512
4531437840 4531440512
4531440336 4531440512
4531376976 4531440512

不同的实例对象，对应着相同的类方法地址，
    说明和 @staticmathod 方法类似，只是在堆里面生成一个代码片段，不同的实例对象有相同的指向这个代码片段的指针（地址）
"""
