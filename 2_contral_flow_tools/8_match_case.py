"""match case"""
import sys
from enum import Enum
from unittest import case

"""macth 语法
match subject:
    case <pattern 1>:
        <action>=1>
    case <pattern 2>:
        <action>=2>
    case <pattern 3>:
        <action>=3>
    case _:
        <action>=4

设置一个subject，用众多case来匹配这个目标，如果目标与模式匹配，就执行相应的语句。
subject:要匹配的目标，
case: <pattern> 表示期待匹配的模式
    每个case语句的主体，必须是表达式，可以是任何表达式，包括函数调用、变量、运算符、
    表达式组、元组、字典、类、对象、函数、lambda表达式、yield表达式、yield from表达式、with表达式、
    async表达式、await表达式、import表达式、del表达式、exec
    
然后在case后输入若干个模式，让模式与目标进行匹配，如果匹配就执行相应的语句。
    如果所有case的模式都无法与目标进行匹配，若有提供最后一个使用通配符（ _ ）的case语句，则它被认为是匹配的模式
    如果没有任何一个case语句与目标匹配，则整个match语句不执行任何操作。
    注：若有多个模式都能匹配，则执行case的第一个匹配模式的语句。
case语句可以（使用as语句）将模式的部分值与标识符进行绑定，用于匹配后的代码引用。
"""
flag = 100
match (100, 200):
    case (100, 300):
        print("100,300")
    case (100, 200) if flag > 100:
        # if flag > 100:是约束项，被称为守卫，除了模式匹配外，守卫为真才算匹配成功，如果守卫为假，则继续尝试下一个case
        print("100,200")
    case (100, y):
        print(f"100,y:{y}")
    case (x, 200):
        print(f"x,200:{x}")
    case _:
        print(f"_,_,_,_,_")

""" match 与 if 的不同
if 语句判断的是表达式的最终值，是真还是假，如果为真认为’匹配‘成功（满足条件），执行代码；
match 语句判断的是模式，可以认为是形式、结构或取值，比if语句功能更强大。
"""


def fun(score):
    match score:
        case 100:
            print("A")
        case score if score >= 80:
            print("B")
        case score if score >= 60:
            print("C")
        case score if score in [57, 58, 59]:
            print(f"差{60 - score}分及格。")
        case _:
            print("非法成绩")


# while True:
#     fun(int(input('请输入成绩：')))

"""或模式
| :表示或，匹配的时候会从左往右匹配，只要有任意一个匹配成功即匹配成功。
"""


def fun1(grade):
    match grade:
        case 1:
            print('A')
        case 2:
            print('B')
        case 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
            print('C-----------')
        case _:
            print('已毕业')


# fun1(4)


"""值模式
如果带（ . ），会被认为是对象的属性值，会在执行计算后进行匹配。即执行<subject>==object.attributes,为真时，匹配成功
"""


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


color = Color.GREEN
match color:
    case Color.RED:
        print('红色')
    case Color.GREEN:
        print('绿色')
    case Color.BLUE:
        print('蓝色')
    case _:
        print('其他')

'''类模式
通过类对象，可以将数据结构化，可以使用类名后跟一个类似于构造函数的参数列表作为一种模式，
    这种模式可以将类的属性捕捉到变量中。
'''


class Point:
    # Point类是一个简单的数据容器，用于存储坐标点的x和y值。
    x: int
    y: int


def location(point):
    match point:
        case Point(x=0, y=0):
            # 这条case分支的意思是：检查传入的point对象是否是一个Point实例，并且其x属性值为0、y属性值也为0。
            # 如果满足这个条件，那么就执行该分支内的代码逻辑。
            print('原点')
        case Point(x=0, y=y):
            print(f'X轴上{point.y}点')
        case Point(y=0, x=x):
            print(f'Y轴上{point.x}点')
        case Point(x=x, y=y):
            # 匹配的是任意非零坐标点（这里的x=x和y=y实际上并不需要指定变量名，因为它们已经隐含了任何非零值都会被匹配到，
            # 但这里为了清晰起见依然保留了变量名）
            print(f'X轴上{point.x}，Y轴上{point.y}点')
        case _:
            raise ValueError('非法坐标')


p = Point()
p.x = 4
p.y = 5
location(p)

"""序列模式
序列模式包含数个将与序列元素进行匹配的子模式，这些子模式会依次与序列元素进行匹配，类似与列表或者元组的解包。

"""
for thing in [[1, 2, 3], ['a', 'b', 'c'], 'this won\'t be matched']:
    match thing:
        case [int(x), int(second), int(z)] as y:
            print(f'Found a list with three ints: {y}')
            print(y, f'第二个是：{second}')
            print(y, f'第1个是：{x}')
            print(y, f'第3个是：{z}')
        case _:
            print('Not a list of three ints')

"""第一个case分支：
匹配条件：[int(), int(second), int()] as y
这个模式试图将thing解构为一个包含三个整数的列表，并将整个匹配到的列表赋值给变量y。同时，它尝试捕获第二个整数并将其赋值给变量second。
然而，这里的写法实际上是错误的，因为int()并不是用于匹配任意整数的方式，正确的方式应为int(x)、int(y)和int(z)，分别代表列表中的每个元素。
    即：将捕获的整数，赋值给x,y,z，而不是将整个列表赋值给x,y,z。
如果thing确实是一个包含三个整数的列表，将会执行以下操作：
打印出一条信息，表示找到了一个包含三个整数的列表及其内容。
打印出整个列表y以及第二个整数second。
"""
for thing in [[1, 2, 3], ['a', 'b', 'c'], 'this won\'t be matched']:
    match thing:
        case [*y]:
            print(y)
        case _:
            print('------')
abc = 'abcdefghij'
abcd = [*abc]
print(abcd)
"""尝试对循环中的每个元素进行解包。然而，在case [*y]这一部分，它试图将匹配的对象当作可迭代对象并将其内容解包到列表y中。
对于列表[1, 2, 3]和['a', 'b', 'c']，它们是可迭代的，因此可以成功地将元素解包至新列表y中，并分别输出 [1, 2, 3] 和 ['a', 'b', 'c']。

然而，对于字符串 'this won\'t be matched'，虽然在Python中字符串也是可迭代对象，但它在模式匹配的上下文中并不能直接被星号（*）解包，
    因为这里的星号期望的是一个可迭代的容器类型（如列表、元组等），而不是单个字符组成的序列。
"""

"""映射模式
可以用{key:value}形式来匹配字典模式
"""


def chack_massage(massage):
    match massage:
        case {'success': massage}:
            # 当传入的massage参数是一个包含键为success的字典时，会提取出该键对应的值并赋给内部的临时变量massage，然后打印“成功:”和该值。
            print(f'成功:{massage}')
        case {'error': massage}:
            print(f'失败:{massage}')
        case _:
            print(f'未知:{massage}')


message_success = {'success': 'ok!'}
message_error = {'error': 'error!'}

chack_massage(message_success)
chack_massage(message_error)

"""as模式
允许你在匹配表达式的同时，给匹配到的值绑定一个别名（alias），以便在相应的代码块中引用这个值
"""


def process_data(date):
    match date:
        case {'name': name as n, 'age': age as a}:
            print(f'姓名:{n}, 年龄:{a}')
        case (x, y) as coordinates if x == y:
            print(f'coordinates:{coordinates}')
        case _:
            print('未知')


process_data({'name': 'Alice', 'age': 25})
process_data((3, 4))
process_data((3, 3))

print('-----------------------------')


def alarm1(item):
    match item:
        # 在Python的结构化模式匹配（match-case）语句中，可以分开匹配元组的参数，
        # 这是因为match-case允许,根据元组的结构和其中元素的具体值,进行精确的模式匹配。
        # 当case表达式中的模式与输入的元组相匹配时，可以将元组中的各个元素赋值给相应的变量

        case ('早上' | '中午' | '下午') as time, ('打游戏' | '睡觉' | '看电视') as action, aaa:
            # case 期望匹配的是一个三个元素的元组，且前两个元素是三个可选字符串中的一个，第三个元素可以是任意类型
            print(type(item))
            print(f'闹钟设定成功，时间是{time}，动作是{action}, aaa是{aaa}')

        case (time, action, aaa) if time in ('早上', '中午', '下午') and action in ('打游戏', '睡觉', '看电视'):
            # case(time, action, aaa)
            # 模式会尝试匹配一个包含三个元素的元组，并将这三个元素分别绑定到time、action和aaa变量上。
            #                           ————很像海象运算符的升级版（但不是）；在Python 3.10及更高版本的match-case语句中，
            #                           通过模式匹配可以直接将元组或其他数据结构中的元素绑定到变量上，这是对结构化模式匹配功能的增强，
            #                           而非海象运算符的升级版。这两种语法特性分别服务于不同的场景和目的。

            # 这样做的好处在于可以直接针对每个元素的值进行后续处理，而无需手动提取元组的元素。
            # 虽然在你的示例代码中使用了管道符号 | 来合并字符串选项，但在实际的Python3.10
            # 及以上版本的match - case语法中，不支持这种用法来匹配元组的第一个元素为多个选项的情况。
            # 正确的写法应该是如上面所示的条件判断语句或使用 in 关键字进行检查
            print(f'闹钟设定成功，时间是{time}，动作是{action}, aaa是{aaa}')

        case ('早上' | '中午' | '下午') as time, action:
            # case 期望匹配的是一个二元组，第一个元素是('早上' | '中午' | '下午')中的一个字符串，第二个元素是任意类型
            print(type(item))
            print(f'闹钟设定成功，时间是{time}，动作是{action}')

        case _:
            print('闹钟设定失败')


alarm1(('下午', '打游戏', 'sdasd'))
alarm1(('下午', '吃饭', 'sdasd'))
alarm1(['下午', '睡觉', 'sdasd'])
alarm1(('下午', '睡觉'))

flag1 = 100
match (100, 200):
    case (100, 300):
        print("100,300")
    case (100, 200) if flag1 > 100:
        # if flag > 100:是约束项，被称为守卫，除了模式匹配外，守卫为真才算匹配成功，如果守卫为假，则继续尝试下一个case
        print("100,200")
    case ((100 | 200 | 300) as x, y):
        print(f"100,y:{y}")
    case (x, 200):
        print(f"x,200:{x}")
    case _:
        print(f"_,_,_,_,_")

"""对于匹配元组目标有两种方法
1、单个元素按位置匹配，即按位置匹配元组中的元素，而不是按元素值匹配。
    每个元素可以单独匹配，单独设置约束条件，但要使用as关键字将匹配到的值绑定到变量上。
    如：case ('早上' | '中午' | '下午') as time, ('打游戏' | '睡觉' | '看电视') as action, aaa:
    
2、匹配整个元组，用守卫来约束，即在匹配元组的同时，对元组中的每个元素进行约束，只有所有元素都满足约束条件，才算是匹配成功。
    如：case (time, action, aaa) if time in ('早上', '中午', '下午') and action in ('打游戏', '睡觉', '看电视'):
    
注：相比之下，方法2更加清晰明了。
"""
