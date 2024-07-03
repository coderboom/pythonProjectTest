"""对象的Properties和Attributes 序列的创建"""
print('----------------------------------------')
"""对于创建可迭代的序列的另一种替代方法，无需实现 __iter__() 方法。
    当找不到 __iter__ 时，解释器会寻找下一个最好的方法—— __getitem__() 方法。
    如果此方法也不存在，则解释器将引发 TypeError 异常。
    
为了定义一个序列，我们必须确保 __getitem__ 和 __len__方法都实现了。
    序列的元素从零开始索引，并且可迭代的对象应按该顺序单独返回它包含的元素。
    
__iter__方法的缺点是，如果您想在途中访问某个值，则必须从头迭代到该点，从而大大增加了 CPU 使用率和花费的时间。这是一个经典的权衡问题。
__iter__:
    优点：堆内存占用非常低
    缺点：随机查找耗CPU资源
    
我们可以通过使用序列生成来解决这个问题。
    序列将计算并将值存储在内存中，并将在更短的时间内启用迭代和随机访问(O(1) 用于访问元素)。缺点是它会比__iter__的方式使用更多的内存。
    
__getitem__()
特点：先占用内存布置好数据；随机查找时间复杂度O(1)
"""
from datetime import date, timedelta


class DateRange:
    def __init__(self, start_dt, end_dt):
        self.start_dt = start_dt
        self.end_dt = end_dt
        self._range_values = self._get_range_values()

    def _get_range_values(self):
        date = []
        current_dt = self.start_dt
        while current_dt < self.end_dt:
            date.append(current_dt)
            current_dt += timedelta(days=1)

        return date

    def __len__(self):
        return len(self._range_values)

    def __getitem__(self, item):
        return self._range_values[item]


my_date_range = DateRange(date(2022, 6, 1), date(2022, 6, 10))
for my_date in my_date_range:
    print(my_date)

print(my_date_range[2])  # 时间复杂度: O(1)
