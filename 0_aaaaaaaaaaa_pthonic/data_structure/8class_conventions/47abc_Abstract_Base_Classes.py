print("----")
"""
设计一个项目时，我们都会先指定一个蓝图，这个蓝图就是我们的抽象基类：
* 基类不应允许初始化。
* 接口方法未实现时报告相关错误。

Python的ABC模块有两种方式定义抽象基类：
    继承ABC
    metaclass=ABCMeta

抽象的方法用@abstractmethod的decorator来修饰，衍生基类的子类必须要实现定义的抽象方法。
抽象方法作为类的蓝图的接口（契约），留给子类去做相应的实现，让系统的架构显得灵活、健壮、易于维护。
通过实例的讲解和微型框架的例子，让大家清楚了解到抽象的重要，特别是在框架设计的时候。抽象可以让我们把不变和变化的部分分清界限，做好设计。

抽象基类（Abstract Base Class，简称ABC）在编程语言中，如Python，扮演着重要的角色，它的主要作用包括但不限于以下几点：

    接口规范：抽象基类定义了一组接口（即抽象方法），强制要求所有子类遵循这些接口规范。这有助于确保不同子类之间的一致性和互换性，使得代码更加模块化和易于维护。
    设计约束：通过定义哪些方法是必须被子类实现的，抽象基类为开发者设定了明确的设计约束，有助于指导面向对象设计，避免不当的继承和实现。
    代码复用：虽然抽象基类自身不提供具体实现，但它可以包含一些通用的实现代码（非抽象方法），供所有子类继承和复用，减少重复代码。
    多态支持：利用抽象基类，可以编写处理各种子类的多态函数和方法，无需了解子类的具体类型，只要求它们遵循抽象基类定义的接口。
    早期错误检测：在实例化抽象基类的子类时，如果子类没有实现所有的抽象方法，Python会在运行时抛出错误，这有助于提前发现和修正错误。
    提高可读性和可扩展性：通过接口而非实现进行编程，使得代码的意图更加清晰，便于其他人阅读和理解，同时也为未来的扩展提供了便利。
    协作开发：在大型项目或团队开发中，抽象基类可以作为不同模块间约定的接口，使得每个开发者只需关注自己模块的实现，而不必担心与其他模块的集成问题。
"""

from abc import abstractmethod, ABCMeta, ABC

""" 抽象基类的三种定义方式
1、继承 metaclass=ABCMeta 
2、继承 ABC  
注：方式2，基类的 mro 会出现ABC类，方式1不会出现，如果继承情况很复杂，需要考虑那种抽象基类定义方式
抽象方法子类必须实现，继承的一般方法不用

"""


class Component(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        """
        抽象基类不能实现.__init__(self)
        """
        pass

    @abstractmethod
    def bind_data(self):
        pass

    @abstractmethod
    def render(self):
        pass


class ProductList(Component):

    def bind_data(self):
        pass

    def render(self):
        pass


print(ProductList.mro())
"""
继承  metaclass=ABCMeta   时：[<class '__main__.ProductList'>, <class '__main__.Component'>, <class 'object'>]
继承  ABC 时：[<class '__main__.ProductList'>, <class '__main__.Component'>, <class 'abc.ABC'>, <class 'object'>]
"""
print('--------------------构建网页的例子 见47图--------------------------------')


class PageContext:
    def __init__(self):
        self.param_items: dict = {}
        self.data: [str] = []
        self.page: str = ''
        self.show_page = True


class Page(metaclass=ABCMeta):
    @abstractmethod
    def init(self, context: PageContext) -> None:
        pass

    @abstractmethod
    def pre_render(self, context: PageContext):
        pass

    @abstractmethod
    def render(self, context: PageContext):
        pass

    @abstractmethod
    def completed(self, context: PageContext):
        pass


def page_handler(params: dict, page: Page):
    """
    处理页面的引擎
    白话： 要加载一个网页，我只知道需要这几个生命周期，只要做好了这几个生命周期，我就认为网页完成了，但是每个生命周期中具体整么做时不管的。
    :param params:
    :param page:
    :return:
    """
    content = PageContext()
    content.param_items = params  # 条用网页内容需要用的数据，用params 初始化 PageContext()
    page.init(content)  # 初始阶段，准备调用方提供的params，构造好page的初始结构， 准备数据是params初始化的 PageContext 实例
    page.pre_render(content)  # 预渲染，渲染数据准备
    page.render(content)  # 渲染，生成结果项
    page.completed(content)  # 最终完成环节，可做过滤处理
    return content.page  # 最后返回处理好的页面


class WebPage(Page):
    def init(self, context: PageContext) -> None:
        print('init', context.param_items)

    def pre_render(self, context: PageContext):
        print('pre_render')
        context.data = ['1', '2', '3', '4', '2']

    def render(self, context: PageContext) -> None:
        print('render')
        context.page = '\n'.join([item for item in context.data])

    def completed(self, context: PageContext):
        print('competed')
        if not context.show_page:
            context.page = 'Permission Dennied.'


web_page = WebPage()
page_content = page_handler({}, web_page)
print(page_content)
