"""Walrus Operator or Assignment Expression"""
from math import sqrt

"""
variable_name := expression

海象运算符将expression的结果赋值给variable_name
同时，整个表达式返回expression的值。

（variable_name := expression） 条件 
在同一行，先将expression的值赋给variable_name，然后返回expression的值。再判断条件是否成立。———— 一行语句完成了赋值和判断两个操作。
    ————在作用域内，可以使用variable_name，而不用声明变量名。

variable_name作用域
局部作用域：如果variable_name是在一个函数内部定义的，则它具有局部作用域，只能在该函数内部被访问
全局作用域：如果variable_name是在全局作用域（脚本或模块的最外层）首次赋值，并且没有用global关键字声明，则其作用域为局部作用域，但仅限于当前运行的代码块
全局/内置作用域：如果在函数内部希望variable_name具有全局作用域，需要使用global关键字明确声明。


在条件判断中使用：
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    while item := list1.pop():  # 如果list.pop()不返回None（即列表非空），则item被赋予弹出的元素并继续循环
        print(item)
except IndexError:
    print('list is empty')

print(item)

"""
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    status_code = getattr(e, 'status_code', None)  # 使用传统方式需要先赋值再检查
    if status_code == 404:
        handle_not_found()
else:
    process_response(response)

# 使用海象运算符简化为
try:
    status_code := getattr(requests.get(url), 'status_code', None)
    if status_code == 404:
        handle_not_found()
    else:
        process_response(requests.get(url))
except requests.exceptions.RequestException:
    pass
    
"""

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# bb := len(list2)  # 语法错误
# print(bb)
"""因为bb := len(list2)被当作一个单独的语句处理，而不是作为条件、循环或任何其他允许嵌入赋值表达式的上下文。
要使这段代码正确执行并使用海象运算符，你需要将它置于适当的上下文中，例如在一个条件判断、循环或者作为一个表达式的一部分：
"""


def my_function():
    if (value := len(list2)) > 1:  # value 在此函数内有局部作用域
        print(value)


my_function()
# print(value)  # 报错，因为value在此处未定义

a = [a1 := 2, 23, 12, 5, 46, 2, 972]
b = ('sdoaihsd', b1 := 'sdoaihsd', 1032)
c = {1, 4738, c1 := 'asdiahsd'}
match m1 := 100:
    case 100:
        print('100')

n = (n1 := 1999)
print(a1, b1, c1, m1, n1)

"""海牙运算符 用在lambda函数，让lambda函数可以复用"""
aa = [y := (lambda x: (x + 1) ** 12)(2), y ** 2, y ** 3, y ** 4, y ** 5]
print(aa)

a3 = [a1 := 'a22', 'B23', 's12', 'i5', 'q46', 'p25', 'g972']
a3.sort(key=(f := lambda x: int(x[1:])))
print(f'a3: {a3}', '\n', f'f: {f}', '\n', f'a1: {a1}')

a4 = ['a772', 'B243', 's102', 'i51', a7 := 'q4699999', 'p2111111111115', 'g979090990902']
a4.sort(key=f)
print(f'a3: {a4}', '\n', f'f: {f}', '\n', f'a1: {a7}')

nn = [nn1 := i for i in range(100)]
print(nn, '\n', nn1)
