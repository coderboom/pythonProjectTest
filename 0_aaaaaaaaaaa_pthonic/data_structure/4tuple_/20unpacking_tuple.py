"""解包"""
csv_file_row = ['jacky', 'jacky@local.com', '55']
(a, b, c) = csv_file_row
aa, *bb = csv_file_row
print(a, b, c)
print(aa, bb, type(bb))  # <class 'list'>


def display_user(*users):
    print(type(users))  # <class 'tuple'>
    for u in users:
        print(u)


display_user('asd', 'difhiah', 'nvih', 'dfiyf', 123)
"""
<class 'tuple'>
asd
difhiah
nvih
dfiyf
123
"""
"""为什么*号变量出现list和tuple两种类型

解压赋值（Unpacking）: 在csv_file_row的解压赋值中，(*bb)用于将列表中的剩余元素解压到一个列表bb中。
    在csv_file_row = ['jacky', 'jacky@local.com', '55']的情况下，aa将得到第一个元素'jacky'，
    而bb将是一个包含剩余元素的列表['jacky@local.com', '55']。所以type(bb)是<class 'list'>。
    
可变参数（Variable-Length Argument Lists）: 
    在display_user函数中，*users是一个可变参数，它将传入的所有参数收集到一个元组中。
    因此，当你调用display_user('asd', 'difhiah', 'nvih', 'dfiyf', 123)时，
    users将是一个元组('asd', 'difhiah', 'nvih', 'dfiyf', 123)，这就是为什么print(type(users))输出<class 'tuple'>。
    
所以，*号在解压赋值时产生了一个列表，在函数参数中则创建了一个元组。
    这是因为这两种情况下的*运算符的作用不同：解压赋值用于分配列表或元组的元素，而可变参数用于收集函数调用的多个参数。
"""


def get_data_info(data) -> tuple:
    average = float(sum(data) / len(data))
    sum_value = sum(data)
    max_value = max(data)
    min_value = min(data)
    return (average, sum_value, min_value, max_value)


c = get_data_info([1, 2, 3, 2, 1, 324, 2, 5, 36, 5, 74, 5, 24, 3, 8, 7, 65, 424, 2, 7, 65])
print(c)  # (50.714285714285715, 1065, 1, 424)
