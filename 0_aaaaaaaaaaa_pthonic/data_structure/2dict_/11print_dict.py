"""优雅的打印字典"""

books_map = {
    'name': 'python游戏编程',
    'author': 'Bobby',
    'start': 78,
    'publish_at': '2022-8-9',
    'info': {
        'alias': 'python game programming',
        'users': 10000,
        # 'id': 999999999999999
    }
}

print(books_map)
# 打印效果是： {'name': 'python游戏编程', 'author': 'Bobby', 'start': 78, 'publish_at': '2022-8-9', 'info': {'alias': 'python game programming', 'users': 10000, 'id': 999999999999999}}
print('------------------"""使用pprint模块"""-----------------')
"""使用pprint模块"""
from pprint import pprint

pprint(books_map, sort_dicts=False)
""" 打印效果是
{'name': 'python游戏编程',
 'author': 'Bobby',
 'start': 78,
 'publish_at': '2022-8-9',
 'info': {'alias': 'python game programming', 'users': 10000}}
 
 不足：对于内嵌的字典，无法显示出分层效果
"""

print('------------------"""使用json的dumps()来输出"""-----------------')
"""使用json的dumps()来输出"""
import json

books_map_toJson = json.dumps(books_map, indent=4, sort_keys=False)
print(books_map_toJson)
"""打印效果
{
    "name": "python\u6e38\u620f\u7f16\u7a0b",
    "author": "Bobby",
    "start": 78,
    "publish_at": "2022-8-9",
    "info": {
        "alias": "python game programming",
        "users": 10000
    }
}

优点：内嵌字典也层次分明

缺点：不能将内建的函数或者关键字序列化
"""
# print(json.dumps({all: {1, 2, 3, 4}}))
# TypeError: keys must be str, int, float, bool or None, not builtin_function_or_method

print('------------------"""Pyyaml"""-----------------')
import yaml

print(yaml.dump(books_map, allow_unicode=True))
"""输出

author: Bobby
info:
  alias: python game programming
  users: 10000
name: python游戏编程
publish_at: 2022-8-9
start: 78

"""
print('------------------------------pyyaml详解---------------------------')
"""PyYAML 是一个用于处理 YAML 数据格式的 Python 库，它支持读取和写入 YAML 文件以及在 Python 对象和 YAML 文档之间进行转换。
    YAML（YAML Ain't Markup Language）是一种直观、易于阅读的数据序列化格式，常用于配置文件、数据交换等场景。

以下是使用 PyYAML 的一些关键点和操作方法：


加载整个 YAML 文件：

with open('example.yaml', 'r') as file:
    data = yaml.safe_load(file)
print(data)

这里使用 safe_load 而非 load 是出于安全考虑，因为 load 可能执行潜在的不安全代码（如果YAML文件被恶意构造）。
"""
print('----------------------')

"""解析 YAML 字符串：
如果你有的不是文件而是字符串，可以直接解析字符串："""
yaml_str = """
name: John Doe
age: 30
skills:
  - Python
  - Java
"""
data = yaml.safe_load(yaml_str)
print(data)

"""将 Python 对象转为 YAML 字符串："""
data = {
    'name': 'Jane Doe',
    'age': 28,
    'languages': ['English', 'French']
}

yaml_str = yaml.dump(data)
print(yaml_str)

"""
YAML 语法特性
    大小写敏感：YAML 区分大小写。
    缩进：使用空格缩进表示层次结构，通常推荐使用2个空格。
    列表：用 - 开头表示列表项。
    映射（字典）：键值对以冒号 : 分隔，键后面必须有空格。
    注释：以 # 开头。
高级用法
    标签与构造器：PyYAML 支持自定义标签和构造器来处理特定类型的数据。
    别名与锚点：使用 & 定义锚点，* 引用锚点，实现数据复用。
注意事项
    安全性：避免使用 yaml.load 处理不可信的输入，因为它可能执行任意代码。始终使用 yaml.safe_load。
    编码：确保处理的文件或字符串编码与你的环境匹配，通常为UTF-8。
    PyYAML 提供了一套简洁而强大的API，使得在Python项目中使用 YAML 成为一件轻松的事情。
"""
