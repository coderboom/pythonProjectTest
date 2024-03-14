"""while"""

"""在Python中，while-else 结构是一种循环条件判断结构，它结合了 while 循环与 else 子句。
当循环因为条件不再满足而自然结束时（非通过 break 语句跳出循环），则执行 else 子句中的代码块

while 循环先对条件语句进行判断，如果条件为真，则执行循环体，条件为False，则结束循环。
    while后面如果是一个逻辑表达式，会产生布尔值；如果是一个对象，会隐匿执行bool(obj)产生布尔值。
"""
# 示例代码：

count = 0
limit = 5

while count < limit:
    print(f"当前计数：{count}")
    # 假设我们在循环体内做一些操作，比如增加 count 的值
    count += 1
    if count == 3:  # 这里仅仅为了演示，并非必须条件
        break  # 如果我们在此处使用 break，else 子句将不会被执行

else:
    print("循环已自然结束，未在中途退出。")


