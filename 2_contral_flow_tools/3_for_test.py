"""for 循环"""
print('----------------------')
"""
for循环是一种迭代机制，它允许程序员遍历序列（如列表、元组、字符串）或可迭代对象（包括生成器和迭代器）的元素，并对每个元素执行指定的操作。
以下是for循环的基本原理：
迭代过程： 当使用for循环时，Python会调用所迭代对象的__iter__()方法来获取一个迭代器————隐匿的通过iter(Iterable)将Iterable转变成一个迭代器。
迭代器是一个实现了__iter__()和__next__()特殊方法的对象，其中__next__()每次被调用时都会返回下一个值，直到没有更多的值可以返回，此时抛出StopIteration异常。
可迭代对象是实现了__iter__()方法的对象，但不一定是迭代器。
"""
# 对于一个列表进行for循环
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

"""在这段代码中，Python首先调用my_list.__iter__()——（或者是使用内置函数iter(iterable/iterator)）得到一个---迭代器对象---，
然后不断调用————迭代器对象.__next__()————方法，每次获取并打印列表中的下一个元素。

获取一个迭代器
显示调用：iter(iterable/iterator)
隐示调用：Iterable.__iter__()

迭代获取下一个元素
显示调用：next(iterator)
隐示调用：iterator.__iter__()

在Python中，for循环处理迭代器对象的方式是自动进行的，它隐式地调用了__iter__和__next__方法。
    而当不在for循环中时，如果你想手动控制迭代过程，就需要显式地使用iter()和next()函数。
在for循环中：
    当你使用for循环遍历一个对象，例如for item in some_iterable:，Python会自动执行以下操作：
    首先，它调用some_iterable.__iter__()来获取迭代器。如果some_iterable支持迭代，它通常会返回一个迭代器对象。
    然后，Python在每次迭代时隐式调用iterator.__next__()来获取下一个元素，直到StopIteration异常被抛出，表示迭代结束。
    
不在for循环中：
    如果你想手动控制迭代过程，你可以这样做：
    使用iter(some_iterable)来获取迭代器，这相当于调用some_iterable.__iter__()。
    然后，使用next(iterator)来获取迭代器的下一个元素，这相当于调用iterator.__next__()。
    你需要反复调用next()，直到StopIteration异常被抛出
"""
# 上面的例子等价于
iterator_my_list = iter(my_list)
while True:
    try:
        item = next(iterator_my_list)
        print(item)
    except StopIteration:
        break

"""for 循环执行流程
for <变量> in <可迭代对象>：
    <逻辑代码>
    
1、从<可迭代对象>中获取第一个元素，将它赋值给<变量>.
2、然后执行循环体中的<逻辑代码>。一般情况下，循环体中的语句会使用<变量>中的值来执行一些操作。
3、从头开始执，从<可迭代对象>中获取下一个元素。
————————4、如此往复，直至执行完<可迭代对象>的最后一个元素为止，或 直到遇到break语句或遇到StopIteration异常。————————
"""
print('----------------------')
"""
   for variable in iterable:
       # 这里是循环体内的语句
       
variable 是每次迭代时代表当前元素的临时变量。
iterable 是任意可迭代对象，它可以是列表、元组、字符串、字典视图、集合或其他支持迭代协议的对象。
步进与终止： Python的for循环内部自动处理了迭代的推进以及循环何时结束的问题，无需像C语言那样显式地声明步进值或循环条件。
    循环会一直持续到迭代器的__next__()方法抛出StopIteration异常为止。
无限循环与中断： 如果可迭代对象是无限的，那么for循环将不会自动停止，除非在循环体内添加适当的退出条件（例如使用break语句）。
    在某些情况下，可以结合else子句使用for循环，这样当循环正常完成（即未遇到break语句）时，else块中的代码会被执行。
配合range()函数： 在Python中，常通过内置函数range()创建一个数字序列用于for循环，比如按特定步长遍历某个范围内的整数：
"""

for i in range(5):  # 这将生成0, 1, 2, 3, 4
    print(i)

"""
在Python中，for variable in iterator: 是一个基本的迭代循环结构，它用于遍历任何可迭代对象（包括但不限于列表、元组、字符串、字典视图、集合以及自定义的迭代器对象）中的元素。
这里的 variable 是循环内部每次迭代时所代表当前元素的变量名。
    每次循环迭代开始时，Python会调用迭代器的 __next__() 方法获取下一个值，并将其赋给 variable。
    当迭代器没有更多的值可以返回时（即 __next__() 抛出 StopIteration 异常时），for 循环结束。
"""
print('----------------------------------')
"""break 和 continu"""

"""break：
当在循环体（如 for 或 while 循环）内部遇到 break 语句时，它会立即终止当前循环的执行，并跳出整个循环结构，继续执行循环之后的代码
"""
for i in range(10):
    if i == 5:
        break
    print(i)

"""多重循环
break 关键字通常用于跳出当前正在执行的循环结构。当在多重循环（如嵌套循环）中使用 break 时，它会结束最内层的循环，并继续执行该循环之外的下一行代码
当你在一个嵌套循环（多重循环）中使用 break 时，它只会跳出当前正在执行的循环。
"""
for i in range(3):  # 外层循环
    for j in range(5):  # 内层循环
        if i == 1 and j == 2:
            break  # 当 i=1 和 j=2 时，将跳出内层的 j 循环
        print(f"i: {i}, j: {j}")
print('-----------------------------')
"""然而，如果需要从整个多重循环中完全退出，单纯使用 break 是无法直接实现的"""
should_continue_outer_loop = True

for outer in range(3):
    if not should_continue_outer_loop:
        break

    for inner in range(5):
        if outer == 1 and inner == 2:
            should_continue_outer_loop = False  # 设置标志变量，表示应退出外层循环
            break
        print(outer, inner)

    if not should_continue_outer_loop:
        break  # 根据标志变量退出外层循环

    print(f"Outer loop: {outer}, Inner loop: {inner}")
print('-----------------------')

"""continue：
当在循环体内遇到 continue 语句时，它会立即结束当前迭代（即跳过当前循环体中 continue 之后的代码），并进入下一轮循环的判断阶段。
"""
for i in range(10):
    if i % 2 == 0:  # 如果i是偶数
        continue  # 跳过本次循环剩余部分
    print(i)  # 只打印奇数

"""continue和多层循环嵌套"""
for i in range(3):  # 外层循环
    for j in range(5):  # 内层循环
        if j % 2 == 0:  # 如果j是偶数
            continue  # 跳过本次内层循环的剩余部分，直接进入下一个j值
        print(f"i: {i}, j: {j}")

# 输出：
# i: 0, j: 1
# i: 0, j: 3
# i: 1, j: 1
# i: 1, j: 3
# i: 2, j: 1
# i: 2, j: 3
