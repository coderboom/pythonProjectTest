from collections import deque

"""Python 标准库集合框架中的 deque 类实现了一个线程安全的双端队列，支持在 O(1) 时间内从两端插入和删除。
考虑到双端操作，您可以将这些数据结构用作队列和堆栈。
在内部，Python 中的双端队列被实现为双向链表，在插入和删除操作中保持一致的性能，但在随机访问堆栈中的中间元素的 O(n) 性能方面表现不佳。"""

stack = deque()
stack.append('cat')
stack.append('dog')
stack.append('tiger')
print(stack)
print(stack.pop())  # 栈

print(stack.popleft())  # 队列


def tail(filename, n=10):
    """return the last n lines of a file """
    with open(filename, 'r') as f:
        return deque(f, n)


file_path = '/Users/chenhao/PycharmProjects/pythonProjectTest/ZZ_2Decoupling_of_classes/product_report.txt'
data = tail(file_path, 4)
print(data)

"""列表的轮转
实现成队列，通过rotate()进行轮转,
"""
d = deque([1, 2, 3, 4, 5, 6])
d.rotate(1)  # deque([6, 1, 2, 3, 4, 5])
d.rotate(1)  # deque([5, 6, 1, 2, 3, 4])
d.rotate(-2)  # deque([1, 2, 3, 4, 5, 6])
print(d)

print('----------------------实现轮巡----------------------')
"""roundrobin('ABC','D','EF')——> A D E B F C"""


def roundrobin(*iterables):
    """roundrobin('ABC','D','EF')——> A D E B F C"""
    print(type(iterables))
    iterators = deque(map(iter, iterables))  # iterators的数据是3个迭代器对象
    print(type(iterators))

    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()


list_data = ['ABC', 'D', 'EF']
print([*roundrobin(*list_data)])
# print(list(roundrobin('ABC', 'D', 'EF')))
