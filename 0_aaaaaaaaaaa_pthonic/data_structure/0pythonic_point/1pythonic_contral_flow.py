matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
width = 3
high = 3
result = [
    [matrix[row][col] for row in range(0, high)] for col in range(0, width)
]
print(result)


# pythonic
def f(x):
    return 100 / x


# no pythonic
fx = lambda x: 100 / x

# f(0)
"""
Traceback (most recent call last):
  File "/Users/chenhao/PycharmProjects/pythonProjectTest/2_contral_flow_tools/1pythonic_contral_flow.py", line 20, in <module>
    f(0)
  File "/Users/chenhao/PycharmProjects/pythonProjectTest/2_contral_flow_tools/1pythonic_contral_flow.py", line 14, in f
    return 100 / x
           ~~~~^~~
ZeroDivisionError: division by zero

"""
print('----------------------------lambda 表达式不好处理0作为除数的情况-----------------------------')
# fx(0)
"""
Traceback (most recent call last):
  File "/Users/chenhao/PycharmProjects/pythonProjectTest/2_contral_flow_tools/1pythonic_contral_flow.py", line 31, in <module>
    fx(0)
  File "/Users/chenhao/PycharmProjects/pythonProjectTest/2_contral_flow_tools/1pythonic_contral_flow.py", line 18, in <lambda>
    fx = lambda x: 100 / x
                   ~~~~^~~
ZeroDivisionError: division by zero
"""

"""
注意使用场景，pythonic 推荐使用定义函数的形式来代替lambda， function形式代码逻辑更清晰
"""

for data in [2, 3, 4, 6, 7, 9]:
    print('in the list')
else:
    print('normal over')

data1 = [2, 3, 4, 6, 7, 9]
while data1:
    x = data1.pop()
    if x == 4:
        break
    print(x, ':in the list')

else:
    print('normal over')
"""
for else 和 while else
是在程序正常迭代完才会执行else
"""

print('------------------------列表推导式和生成器的区别-------------------------')
from typing import Iterator


def read_lines_from(path: str) -> [str]:
    with open(path, 'r') as f:
        lines = [line for line in f]
    print(lines)


read_lines_from('/99_pd_/abcde.txt')


def read_lines(path: str) -> Iterator[str]:
    with open(path, 'r') as f:
        for line in f:
            print(line)
            yield line


lines = read_lines('/99_pd_/abcde.txt')
print(*lines)

"""
若文件非常大
列表推导式：会将文件内容全部获取出来，保存在内存中，非常占用内存——————以空间换时间

生成器：每次需要用到时获取，占用内存小，会经常生成，花费时间，在并发中延迟高—————— 以时间换空间
"""
print('------------------------range() 占用的内存固定-------------------------')
range(12)
print(range(122) == range(122))  # True
print(range(122) == range(100000000000000000000000000))  # False
"""
内存占用：尽管range()对象可以表示很大的整数序列，但实际上它并不一次性生成所有的整数值并存储在内存中。
    range()返回的是一个特殊的迭代器对象，只有在迭代时才会按需生成每个值。
    因此，无论range()表示的序列有多大，其占用的内存都是相对固定的，与序列大小无关。
    这种特性使得range()非常适合用于处理大范围的整数序列，尤其是在需要节省内存或处理无限序列时。
"""
print(range(35)[9:])  # 输出range(9, 35)
"""
尽量使用range() 代替遍历列表
"""
