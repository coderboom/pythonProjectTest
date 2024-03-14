"""
Python 的数字类型可以存储在数学上的各种数字，包括常见的自然数、复数中的虚数、巨大的数字、正负数、带小数点的数、不同进制的数等等，非常灵活丰富。
"""

x = 1  # int, 整型
y = 1.2  # float, 浮点
z = 1j  # complex, 复数
"""
类型	                           描述	                                                                                    示例
int	      有符号整数，它们通常被称为整数或整型。它们是没有小数点的0、正或负整数。 Python3 中的整数是无限大小的	                        2, -1, 0, 0×69
float	  浮点实数值，也称为浮点数，它们表示实数，并用小数点写整数和小数部分。 浮点数也可以是科学符号，E或e表示10的幂	                0.00, 1.4, -23.22, -32.54e100
complex	  复数是以a + bJ的形式，其中a和b是浮点，J(或j)表示-1的平方根(虚数)。数字的实部是a，虚部是b。复数在Python编程中用处较少	        3.14j, 9.322e-36j
"""

"""整型 int
可以使用前缀 0x，0o 和 0b 分别表示 16、8、2 进制的表示方式。"""
a = 97  # 10 进制
b = 0b01100001  # 2 进制
c = 0x61  # 16 进制
d = 0o301  # 8 进制

"""浮点 float
float('inf') 的结果 inf 正无穷，float("-inf") 负无穷。float("nan") 代表缺失值。
"""
x = 1.10
y = 1.0
y2 = 1.  # 1.0
z = -11.01
z2 = .1
"""用科学计数法赋值"""
e = 3.5e5  # 350000.0 e后面跟着的表示是10的幂次
f = 1E6  # 1000000.0

"""Python 3.6 开始支持新的数字下划线功能，对于很大的数字以提高可读性。"""

a = 123_456_789  # 123456789 可以在较大的数字用下划线连接
b = 123_456.888  # 123456.888
print(f'{10000000000:_}')  # 10_000_000_000
print('zhi {:_} shi'.format(10000000000))  # 10_000_000_000
"""
见input_output内的Format_string_literal

最复杂：填充符+对齐符+显示符号(+/-/(空格))+占位符位宽(数量)+千位分隔符+格式化字符的精度控制
"""


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        return self.age >= 18


s1 = Student('zhangsan', 18)
print(bool(s1))

if s1:  # Student(name='zhangs', age=16):
    print('成年人')
else:
    print('未成年')

print(divmod(20, 3))  # 以元组的形式返回商和余数
print('00000000000000')
print(b'a')
print(b"saihdasndasjhiasd")

"""bytes
bytes() 函数用来创建 bytes 对象。bytes() 接收一个字符串参数，返回bytes对象。"""

"""b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'"""
print(bytes(20))
print(help(bytes))

"""bytearray(),创建字节数组对象，可读写。
"""
print(bytearray(b'12'))
print(bytearray(10))

"""
内存视图（memoryview）是一种内置类型，它提供了一种机制来访问对象的底层数据缓冲区而不进行复制。
这意味着可以在不消耗额外内存的情况下对原始数据进行读取和写入操作，这对于处理大型数据结构或者需要高效内存管理的场景尤其有用。
内存视图可以应用于任何实现了Python缓冲协议（buffer protocol）的对象，这包括但不限于：
字节字符串（bytes）
字节数组（bytearray）
Numpy数组


通过内存视图，你可以像操作数组一样切片、索引，并且不会创建新的副本，对于大文件或大数据流的操作非常有效率。
同时，由于它是引用原数据，所以在处理完数据后，不需要手动释放内存资源。
"""
mv = memoryview(b'hello')
print(mv)
print(mv[1])
print(mv[:4])
print(mv[:4].tobytes())
print(bytes(mv[:4]))

print(1111111111111111111111111111111111111111111111111111111111111111111111111111111111)
print(int('1010', 2))
print(int('12', 8))
print(int('12', 16))

print(bin(10))  # 将数字转换为二进制
print(oct(10))  # 将数字转换为八进制
print(hex(10))  # 将数字转换为十六进制

print(format(10, '#b'))  # 将数字转换为二进制，带0b
print(format(10, 'b'))  # 将数字转换为二进制，不带0b

print(format(10, "#o"))  # 将数字转换为八进制，带0o
print(format(10, "o"))  # 将数字转换为八进制，不带0o

print(format(10, "#x"))  # 将数字转换为十六进制，带0x
print(format(10, "x"))  # 将数字转换为十六进制，不带0x

print(float(10))
print(float('nan'))
print(float('inf'))
print(float('-inf'))

# 创建一个包含ASCII字符的bytes对象
ascii_string = "Hello, World!"
ascii_bytes = ascii_string.encode('ascii')
print(ascii_bytes)


def fibonacci_recursive(n):
    # 斐波那契数列的基准情况（终止条件）
    if n <= 0:
        return "输入值应大于0"
    elif n == 1:
        return 0  # 第0项为0
    elif n == 2:
        return 1  # 第1项为1
    else:
        # 递归情况：F(n) = F(n-1) + F(n-2)
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 示例用法
n_terms = int(input("请输入要计算的斐波那契数列项的位置："))
fib_value = fibonacci_recursive(n_terms)
print(f"斐波那契数列第{n_terms}项的值是：{fib_value}")
