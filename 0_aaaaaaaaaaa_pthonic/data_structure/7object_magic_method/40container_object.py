""" 对象的Properties和Attributes 容器对象 """
"""
Python 中实现 __contains__ 魔术方法，并返回真值的对象称为容器。它通常与 in 运算符一起使用，以检查成员资格。

容器是包含任意数量的其他对象的对象。通常，容器提供了一种访问所包含对象并对其进行迭代的方法。

Python内建的容器包括 tuple、list、set、dict等。
    在实践中，所有容器都将具有 __contains__ 魔术方法。
    测试一个对象是否是一个容器时，应该使用 isinstance(x, collections.abc.Container) 。
    
另外，从面向对象与代码维护的角度看，容器对象用好了，可以写出容易维护的代码。
"""


class Product:
    def __init__(self, name, price, spec_num):
        self.name = name
        self.price = price
        self.spec_num = spec_num


class Promotion:
    def __init__(self, lower_num, uper_num, rate):
        self.__lower_num = lower_num
        self.__uper_num = uper_num
        self.__rate = rate

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        self.__rate = rate

    def __contains__(self, item: Product) -> bool:
        return self.__lower_num <= item.spec_num <= self.__uper_num


def get_total_price(products: [Product], promotions: [Promotion]) -> float:
    total_price1 = 0
    for product in products:
        promotion = [promotion for promotion in promotions if product in promotion][0]
        # print(promotion.rate)
        """ product in promotion
        python 检测到 in 关键字，尝试找到promotion对象的__contains__方法
        如果promotion是一个实例，会查找该实例的类中是否有__contains__方法
        如果找到__contains__方法，python会调用它，将item设置成product，并执行该方法体的代码
        
        隐式调用的代码： result=promotion.__contains__(product)
        
        """
        total_price1 += product.price * promotion.rate
    return total_price1


top_promotion = Promotion(100, 199, 0.5)
average_promotion = Promotion(50, 99, 0.8)
none_promotion = Promotion(0, 49, 1.0)
promotions = (top_promotion, average_promotion, none_promotion)

products = (
    Product('cart', 1999.9, 188),
    Product('computer', 5999.9, 88),
    Product('toy', 22.5, 33)
)

total_price = get_total_price(products, promotions)
print(total_price)

print('----------------------------------传统方式--------------------------------')


def get_total_price_legacy(products: [Product]) -> float:
    total_price2 = 0
    for product in products:
        rate = 1.0
        if 100 <= product.spec_num <= 199:
            rate = 0.5
        elif 50 <= product.spec_num <= 99:
            rate = 0.8
        elif 0 <= product.spec_num <= 49:
            rate = 1.0
        total_price2 += product.price * rate

    return total_price2


print(get_total_price_legacy(products))

import collections

print(isinstance(top_promotion, collections.abc.Container))  # True
