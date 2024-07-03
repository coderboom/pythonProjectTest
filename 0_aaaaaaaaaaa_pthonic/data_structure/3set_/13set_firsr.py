programing_languages = {
    'Python', 'C++', 'Java', 'C#', 'Ruby', 'Go'
}
programing_languages1 = {'ACC', 'QWE'}

print(programing_languages1 & programing_languages)  # set()
print('----------')
squares = {x * x for x in range(10)}
print(programing_languages)
print(squares)

"""集合输出是无序的"""
# {'C#', 'Python', 'Go', 'Java', 'Ruby', 'C++'}
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

print('---------------------空集合的创建--------------------')
a = {}
b = set()
print(type(a), type(b))  # <class 'dict'> <class 'set'>
"""创建空集合应该使用set()"""

print('------------==========----集合操作-------==========------------')

dynamic_languages = {'Ruby', 'Python', 'JavaScript', 'Lua'}

# 并集
print(programing_languages | dynamic_languages)
# {'Java', 'Ruby', 'Lua', 'JavaScript', 'Python', 'C#', 'Go', 'C++'}

# 交集
print(programing_languages & dynamic_languages)
# {'Python', 'Ruby'}

# 差集
print(programing_languages - dynamic_languages)
# {'Go', 'C++', 'C#', 'Java'}
print(dynamic_languages - programing_languages)
# {'JavaScript', 'Lua'}

print(programing_languages - programing_languages)
# set()
"""集合操作之后得出得若是空集合，则返回的结果是：set()"""
