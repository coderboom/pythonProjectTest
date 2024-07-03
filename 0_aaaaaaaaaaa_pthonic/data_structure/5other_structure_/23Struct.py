from struct import Struct

"""
struct 模块在Python中的主要作用是实现Python数据类型与C语言结构体之间的转换，以便于处理二进制数据。

它的核心功能围绕以下几个方面：
    数据打包（Pack）：将Python的基本数据类型（如整数、浮点数、字符串等）转换为特定格式的二进制数据（字节串）。
        这在需要将数据写入文件、通过网络发送或以其他方式存储为二进制格式时非常有用。
        
    数据解包（Unpack）：将从文件、网络或其他来源接收到的二进制数据解码回Python的数据类型。这使得程序能够读取和理解外部的二进制数据结构。
    
    大小计算（Calcsize）：根据格式字符串计算出打包后数据的总字节数，这对于预先分配缓冲区或验证数据完整性很有帮助。
    
    内存操作优化：通过直接操作缓冲区（使用 pack_into() 和 unpack_from() 方法），可以在处理大量数据时减少数据复制，提高效率。
    
    大小端支持：允许用户指定数据的字节序（大端或小端），这对于跨平台通信尤其重要，确保数据在不同系统间的一致性。
    
    灵活处理字符串和字节：支持处理固定长度字符串、变长字符串以及字节数据，适用于多种数据编码和格式需求。
    
简而言之，struct 模块使得开发者能够方便地在Python的高级数据表示与底层二进制数据表示之间进行转换，
    是处理二进制数据、实现与其他语言或系统的互操作性、以及进行低级别数据操作的强大工具。
    
"""
print('------------------------------------------------------------------------------------------------')
"""Python 的 struct 模块是一个强大的工具，用于处理二进制数据，尤
    其是当你需要在 Python 数据类型（如整数、浮点数、字符串等）和它们对应的二进制表示之间转换时。

下面是对 struct 模块的详细解析：
1. 导入模块
使用 struct 模块前，首先需要导入它

2. 格式化字符串
格式化字符串定义了如何将Python数据类型转换为二进制，以及如何将二进制数据解码回Python数据类型。
这个字符串由一系列字符组成，每个字符代表一种数据类型及其大小端模式。
    例如，'i' 表示一个有符号整数，'f' 表示一个单精度浮点数，字符前加 < 表示小端模式，> 表示大端模式，如果不指定，默认取决于平台。

3. pack() 方法
功能：将Python数据类型打包成二进制数据。
语法：struct.pack(fmt, v1, v2, ...)
例子：
    packed_data = struct.pack('>if', 1, 2.718)

4. unpack() 方法
功能：将二进制数据解包为Python数据类型。
语法：struct.unpack(fmt, data)
例子：
    data = b'\x00\x00\x00\x01\x40\x09\x21\xfb'
    unpacked_values = struct.unpack('>if', data)
    print(unpacked_values)  # 输出: (1, 2.718)
    使用与 pack() 相同的格式字符串来解包对应的数据。

5. pack_into() 和 unpack_from()

pack_into()：类似于 pack()，但允许你指定数据写入的缓冲区及偏移量。
语法：struct.pack_into(fmt, buffer, offset, v1, v2, ...)

unpack_from()：类似于 unpack()，但可以从缓冲区的特定位置开始解包。
语法：struct.unpack_from(fmt, buffer, offset=0)

6. 计算大小
calcsize()：计算给定格式字符串对应的二进制数据长度。
语法：struct.calcsize(fmt)
例子：
    size = struct.calcsize('>if')
    print(size)  # 输出: 8 (假设整数4字节，浮点数4字节)
    
    
7. 常用格式字符
    'x'：空位，不占用任何空间。
    'c'：单个字节的字符。
    'b'：有符号字节。
    'B'：无符号字节。
    'h'：有符号短整型（通常2字节）。
    'H'：无符号短整型。
    'i'：有符号整型。
    'I'：无符号整型。
    'l', 'q'：分别对应有符号长整型和有符号长整型（可能为4或8字节，具体取决于平台）。
    'L', 'Q'：无符号版本。
    'f'：单精度浮点数。
    'd'：双精度浮点数。
    's'：字节串，后面需要跟上字节数，如 '5s' 表示5字节的字符串。

8. 注意事项
    确保格式字符串与实际数据类型和数量匹配。
    处理非ASCII字符串时，可能需要使用特殊的格式字符，如 'p' 或 's' 后面指定字节数。
    在跨平台应用中，明确指定大小端模式以确保兼容性。
    struct 模块在处理二进制文件、网络协议、硬件交互等场景下非常有用，通过精确控制数据的二进制布局，可以实现高效的数据交换。

"""

my_struct = Struct('i?f')
data = my_struct.pack(102, False, 15.8)
print(data)  # b'f\x00\x00\x00\x00\x00\x00\x00\xcd\xcc|A'

unpack_data = my_struct.unpack(data)
print(unpack_data)  # (102, False, 15.800000190734863)

print('----------------------------------------------')
from collections import namedtuple

Person = namedtuple('Person', 'name,desc,age,upgraded,score')
person = Person(
    bytes('Bobby', encoding='UTF-8'),
    bytes('Hello,Bobby!测试o!', encoding='utf-8'),
    23,
    False,
    99.5
)

print(person)

# 将数据打包成二进制数据
my_struct1 = Struct(f"{len(person.name)}s{len(person.desc)}si?f")
data = my_struct1.pack(*person)
print(data)  # b'BobbyHello,Bobby!\xe6\xb5\x8b\xe8\xaf\x95o!\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc7B'

unpack_data = my_struct1.unpack(data)
print(unpack_data,
      type(unpack_data))  # (b'Bobby', b'Hello,Bobby!\xe6\xb5\x8b\xe8\xaf\x95o!', 23, False, 99.5) <class 'tuple'>
"""通过调用 Person._make(unpack_data)，将解包后的数据元组转换回 Person 实例。
    _make() 是 namedtuple 提供的一个方法，它接受一个可迭代对象（如列表或元组），并用这些值来创建一个新的 namedtuple 实例。
    这意味着 person 变量现在再次引用了一个 Person 对象，其内容与原始对象相同，只是从二进制数据恢复而来。
"""
person = Person._make(unpack_data)
print(
    person)  # Person(name=b'Bobby', desc=b'Hello,Bobby!\xe6\xb5\x8b\xe8\xaf\x95o!', age=23, upgraded=False, score=99.5)
