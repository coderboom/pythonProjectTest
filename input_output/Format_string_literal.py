"""'
使用格式化字符串字面值，在 Python 3.6 之后，可以使用 f'{}' 的方式来格式化字符串。
 {}花括号内的字段，称为格式字段，常是表达式替换的变量和表达式;
  f-string 在功能和性能方面比 %-formatting 和 str.format()函数优秀

"""

import math

month = 12
year = '2910'
event = 'sdaiuhsdaiuhsdaiuh'
print(f'在{year}年{event}事件发生')
print(f'zai {year=} shi will heppen {event=}')
print(f'{month=}')
print(f'{month + 12}sdhaosudau')

"""
f-string 可以用 {content:format} 设置字符串的格式，format 为格式描述符:content的显示格式

对齐和填充：
:< width：左对齐，空格填充到指定宽度。
:> width：右对齐，空格填充到指定宽度。
:^ width：居中对齐，空格填充到指定宽度。
:{fill_char}<width 或 :{fill_char}>width 或 :{fill_char}^width：使用指定字符填充。

精度控制：
    precision:格式字段需要占位的宽度
: . precision f 对浮点数表示小数点后的位数（precision）。
: . precision g 对数值自动选择合适的精度（根据情况采用f或e格式）。
: . precision e 用科学计数法表示，保留小数点后指定位数（precision）。
: . precision s 对字符串进行截断或者尾部填充到指定长度（precision）。
: . precision % 增加precision位小数，再添加百分号，整个数值表示为百分比。

符号：
:+ 总是显示正负号。
:- 只对负数显示负号。
: （空格）对于正数前面显示空格代替加号。

千位分隔符：
：,  使用,  作为千位分隔符
：_  使用_  作为千位分隔符

类型转换：
:d 整数格式。
:f 浮点数格式。
:g 自动选择f或e格式（更紧凑的一种）。
:e 科学记数法。
:s 字符串（默认）。
:x、:X 十六进制整数（小写、大写）。
:c 单个字符。

顺序：
数字最复杂：填充符+对齐符+显示符号(+/-/(空格))+占位符位宽(数量)+千位分隔符+格式化字符的精度控制
字符串：填充符+对齐符+格式化字符的精度控制（截断到指定长度）
"""
print(f'PI的值是{math.pi:^40}bbbbbb')  # 格式字段占位40个字符，默认字符串位置是所占的字符数的右边,^:剧中显示
print(f'PI的值是{math.pi:<40}bbbbbb')  # 格式字段占位40个字符，设置字符串位置是所占的字符位置的左边显示
print(f'PI的值是{math.pi:.10f}')

print(f'zui gao{8080:+}m')
print(f'zui di{-8080:}m')
print(f'zui di{-8080: }m')
print(f'zui di{8080: }m')
print(f'zui di{8080:@^ 20.5%}m')

xiaoshu = 2361.4537598
print(f'xiaoshu:{xiaoshu:.5f}lelel')
print(f'xiaoshu:{xiaoshu:20.5f}lelel')
print(f'xiaoshu:{xiaoshu:^20.5f}lelel')
print(f'xiaoshu:{xiaoshu:^20.10%}lelel')
print(f'xiaoshu:{xiaoshu:*^30.5f}lelel')
print(f'xiaoshu:{xiaoshu:g}')
print(f'xiaoshu:{xiaoshu:.2%}')
# print(f'xiaoshu:{xiaoshu:s}') # 报错

xiaoshu1 = 1800000000000000
print(f'xiaoshu:{xiaoshu1:*^30g}')
print(f'xiaoshu:{xiaoshu1:*^30.2%}')
print(f'xiaoshu:{xiaoshu:_^+30.3f}')
print(f'xiaoshu:{xiaoshu:_^+40.3%}')
print(f'xiaoshu:{xiaoshu1:_^+40_}')
print(f'xiaoshu:{xiaoshu1:_^ 40,.2%}')

str_num = 'dfoa1237nscka'
print(f'str_num:{str_num:_^30}')
print(f'str_num:{str_num:_^30s}')
print(f'str_num:{str_num:_^30.3s}')
print(f'str_num:{str_num:_^30.9s}')  # 对字符串截断到指定长度

print(f'圆面积是{(lambda x: 3.14 * x ** 2)(4)}')
print(f'圆面积是{(lambda x: 3.14 * x ** 2)(100):<7.2f}')

print(f'圆面积是{(lambda x: 3.14 * x ** 2)(100):<+7.2f}')
print(f'圆面积是{(lambda x: 3.14 * x ** 2)(103):<+10.2%}')

'''字符串format()方法'''
# print('we are the {} whoe say "{}" is bbb'.format(year, event))
print('we are the {0} whoe say "{1}" is bbb'.format(year, event))
print('we are the {1} whoe say "{0}" is bbb'.format(year, event))

print('we are the {year} whoe say "{event}" is bbb'.format(year=2019, event='aaaaa'))
print('we are the {1} whoe say "{0}" is bbb {qqqq}'.format(291023, 'ashoahd', qqqq='123ssdaq'))
# print('we are the {1} whoe say "{0}" is bbb {qqqq}'.format(291023,qqqq='123ssdaq', 'ashoahd')) #位置参数只能放在前面

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
'''用方括号 '[]' 访问键来完成'''
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))  # 最好使用按名称引用变量进行格式化
'''将 table 字典作为采用 ** 标记的关键字参数传入来实现'''
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('------------------------------------------')
C = 3 - 6J
print('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'.format(C))

coord = (4, 5, 6)
print('x={0[0]};y={0[1]};z={0[2]}'.format(coord))
print('The {} coordinates are {}, {}, {}'.format('cartesian', *coord))

# 代替%s，和 %r
# !r表示repr()，!s表示str()
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

print('{:*^30}'.format('centered'))

# 替代 %+f, %-f 和 % f 以及指定正负号
print('{:+f}; {:+f}; {:+f}'.format(3.14, -3.14, 3.14e100))
# 替代 %x 和 %o 以及转换基于不同进位制的值
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

import datetime

d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
