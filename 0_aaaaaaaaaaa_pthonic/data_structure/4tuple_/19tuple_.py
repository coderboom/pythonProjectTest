"""元组"""
"""
在以下情况下使用元组：
1、在函数中作为参数使用
2、函数返回值包含多个项的时候使用
3、遍历字典的键值对的时候使用
4、作为字符串格式占位符使用

处理表格数据 常用namedtuple
namedtuple 是 Python 中 collections 模块提供的一个工厂函数，它用来快速创建一个具有命名字段的元组子类
        ——————namedtuple本质是一个继承类元组的类，tuple有的功能它都有
        
它通常用于需要元组的地方，但元组本身没有字段名，只能通过整数索引来访问元组元素。使用 namedtuple，您可以通过名称访问元组的元素，这样代码更易于理解和维护。
"""
from collections import namedtuple

Car1 = namedtuple('Car', 'color mileage')  # Car1是namedtuple生成的Car类
my_car = Car1('red', 3888.9)
print(my_car.color, my_car.mileage)  # red 3888.9
print(my_car[0], my_car[1])  # red 3888.9


class MyCarWithWmethods(Car1):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithWmethods('red', 1233)
print(c)  # MyCarWithWmethods(color='red', mileage=1233)
print(c.hexcolor())  ##ff0000

import csv

"""
E = namedtuple('Employee', 'name,age,title,department')
这里，namedtuple 函数创建了一个名为 Employee 的新元组类型，并且这个类型被赋值给了变量 E。
    这意味着 E 实际上是一个类，具体来说，它是 namedtuple 生成的 Employee 类。

当你使用 E 创建对象时，例如：
employee = E('Alice', 30, 'Engineer', 'R&D')
你实际上创建了一个 Employee 类型的实例，但是通过 E 这个别名来引用它。因此，employee 是一个具有姓名、年龄、职位和部门字段的 Employee 对象。

Employee 是 namedtuple 所创建的类的名字，这个名字主要用于调试和文档字符串中，帮助程序员理解这个类型代表什么。
E 是一个变量名，用来引用 Employee 类型。在 Python 中，类型本身也是对象，可以被赋值给变量。
    所以，E 和 Employee 在这里是等价的，只是 E 是我们用来引用这个类型的名称。

总结
因此，从实际用途来看，E 和 Employee 没有区别：它们都引用了同一个由 namedtuple 创建的类型。
    区别只在于名称：Employee 是类型的名字，E 是这个类型的一个引用。
    在 Python 编程中，可以选择用 E 来代替 Employee 作为类型名称，这样可以使代码更简洁，或者符合特定的命名约定。
    
"""
E = namedtuple('Employee', 'name,age,title,department')

"""从CSV文件读取数据"""
# for employee in map(Employee._make, csv.reader(open('./tmp/employees.csv', 'r'))):
#     print(employee.name, employee.title, employee.department)
