name = 'asdih sdoa qwenk'

newname = name[0:5] + ' 123131' + name[5:]  # 修改字符串的方法

print(name)
print(newname)

eggs = [1, 2, 3, 4]
eggs = [5, 6, 7, 8, 9]  # 复写eggs

good = 'Good hello help hump'
boy = 'asdo sod nfAAfh UUUUwiu vkCCCjnzxb 12u0'
number_list = [str(i) for i in range(1, 11)]
"""不是更改原有字符串"""
print(good.replace('h', 'H'))  # 默认替换所有字符，可以指定替换次数,
print(good.replace('h', 'H', 1))
print(good)

print(good.split(' '))  # 用空格切割字符串，返回的是列表,['Good', 'hello', 'help', 'hump']
print(good)

print('-'.join(number_list))  # 用-连接字符串，返回的是字符串 '1-2-3-4-5-6-7-8-9-10'
print('和'.join(number_list))  # 1和2和3和4和5和6和7和8和9和10

print(boy.upper())  # 所有字符转大写 ASDO SOD NFAAFH UUUUWIU VKCCCJNZXB 12U0
print(boy.lower())  # 所有字符转小写 asdo sod nfaafh uuuuwiu vkcccjnzxb 12u0
print(boy.swapcase())  # 交替大小写 ASDO SOD NFaaFH uuuuWIU VKcccJNZXB 12U0
print(boy.capitalize())  # 字符串首字母大写 Asdo sod nfaafh uuuuwiu vkcccjnzxb 12u0

print(boy.islower())  # 判断字符串是否全部小写
print(boy.isupper())  # 判断字符串是否全部大写
print(boy.title())  # 字符串首字母大写,其他字符转小写 Asdo sod nfaafh uuuuwiu vkcccjnzxb 12u0
boy1 = boy.title()
print(boy1.istitle())  # 判断字符串是否全部首字母大写
print(boy.endswith('jnzxb'))  # 判断字符串是否以指定字符结尾
print(boy.startswith('asdo'))  # 判断字符串是否以指定字符开头
print(boy.center(100, '-'))  # 字符串居中，返回字符串，中间用-填充，长度为100
print(boy.isspace())  # 判断字符串是否为空
print(boy.ljust(100, '*'))  # 字符串左对齐，返回字符串，长度为10，在给定宽度内左对齐，右补*
print(boy.rjust(100, '*'))  # 字符串右对齐，返回字符串，长度为10，在给定宽度内右对齐，左补*

print(boy.count('h'))  # 字符串中字符h出现的次数
print(boy.count('j', 1, 20))  # 字符串中字符j出现的次数，从下标1开始，到下标20结束
print(boy.zfill(100))  # 字符串左对齐，返回字符串，长度为100，在给定宽度内左对齐，右补0,若字符串长度大于等于宽度，则不操作，返回原字符串

print(max(good))  # 返回字符串中最大的字符
print(min(good))  # 返回字符串中最小的字符

print(good.find('y', 1, 20))  # 返回字符串中第一个字符y的下标，找不到返回-1' 可以有切片操作
print(boy.index('h', 1, 20))  # 返回字符串中字符h的首个下标，找不到返回异常,可以有切片操作
print(boy.lstrip('b'))  # 返回字符串中去除字符串左侧字符b后的字符串
print(boy.rstrip('bb'))  # 返回字符串中去字符串右侧字符bb后的字符串

print('999999999')
print(dir(str(123)))  # 查看字符串的方法
print(help(str))  # 查看字符串的方法——文档形式

bbb = 'asdiah'
print(repr(bbb))  # 返回字符串的表示形式
print(repr(10))
print(repr(True))
print(repr(bool))

"""ASCII码（American Standard Code for Information Interchange，美国信息交换标准代码）是一种字符编码标准，
最早于1963年由美国制定，并在之后的几十年里成为计算机系统中最广泛使用的字符集编码方案之一。
它最初设计为7位二进制数来表示128种不同的字符，包括：
33个可打印的控制字符（如换行符\n、制表符\t等）
95个图形字符，包括：
大写和小写字母（A-Z, a-z）
数字0-9
标点符号和其他特殊符号
随着计算机技术的发展，为了支持更多的字符，后来出现了扩展ASCII编码，使用了8位二进制数，能够表示最多256个字符。
扩展ASCII方案并没有统一的标准，不同系统可能有不同的扩展方式，但基本的前128个字符与原始ASCII码保持一致。
以下是一个简单的ASCII码表示例，展示了部分字符及其对应的十进制和二进制数值：
字符
ASCII           十进制值            ASCII 二进制值
NUL                 0               00000000
SOH                 1               00000001
!                   33              00100001
A                   65              01000001
a                   97              01100001
0                   48              00110000
@                   64              01000000
在Python中，可以使用内置函数ord()获取一个字符的ASCII码值，chr()函数则可以将ASCII码转换回对应的字符：

注：bytes 存储以字节位单位的数据
什么是字节：一个字节等于8个位（bit），一个汉字占2个字节
字节是0到255的整数，用来表示一个字节的取值。
"""
aa = 65
cc = 'A'
print(cc, 'ascii demo is:', ord(cc))  # 返回字符的ascii码
print(aa, '对应的ascii码是:', chr(aa))  # 返回将ASCII码转换回对应的字符

# 创建一个包含ASCII字符的bytes对象
ascii_string = "Hello, World!"
ascii_bytes = ascii_string.encode('ascii')
print(ascii_bytes)

"""
什么是bytes对象：b'str'
-->str的每个元素是字节，字节是0到255的整数，显示时是将整数翻译成ascii码对应的字符

在计算机科学中，一个字节（byte）通常是由8位（bits）组成，它可以表示从0到255的整数值。
在Python中，可以通过bytes对象来表示单个或多个字节的数据
"""
a = b'ashdoqwhqbiuabsAISHAISBC'  # 创建一个包含ASCII字符的bytes对象
print(a)
print(bytes(22))  # 创建指定长度以0值填充的bytes对象
print(a[2])  # 输出: b'h' ，h的ASCII码值为: 104

"""接收一个整数迭代器作为参数，并创建一个新的字节对象，其中每个元素都是迭代器中对应整数的8位无符号表示形式,即字节（范围从0到255）"""
byte_sequence = bytes([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])
print(byte_sequence)  # 输出: b'Hello, World!'
print(bytes((1, 72, 101, 108, 108, 111)))

# print(help(bytes))

print('000000000000')
# 创建一个bytearray，并修改其中的内容
b = bytearray()  # 创建一个空bytearray
bb = bytearray(20)  # 创建一个长度为20的bytearray

mutable_ascii = bytearray(b'Hello, ')
mutable_ascii.extend(b'World!')
print(mutable_ascii)
# mutable_ascii.append(b'a')  # “bytes”对象不能被解释为整数
mutable_ascii.append(99)
print(mutable_ascii)
