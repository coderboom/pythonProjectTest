import random

print(random.random())
print('-------------------')
"""base64编码
base64编码是一种将二进制数据转换成ASCII可打印字符的过程，以便可以在那些不支持二进制数据或仅支持文本数据的环境中传输和存储。
    Python标准库提供了base64模块来实现这种编码和解码操作。
"""
import base64

binary_data = b'hello world'  # 一个二进制字符串或者字节串需要编码
encoded_data = base64.b64encode(binary_data)  # b64encode() 函数接收一个字节对象作为参数，并返回一个编码后的字节对象
print(encoded_data)

encoded_str = 'SGVsbG8sIFdvcmxkIQ=='  # 已编码的 base64 数据
decoded_data = base64.b64decode(encoded_str)  # 将 base64 编码的数据解码回原始的二进制数据
print(decoded_data)
"""这里 b64decode() 函数接收一个表示 base64 编码的字符串（必须先将其转换为字节串），并返回解码后的原始字节对象。
    如果原始数据是文本，则可以进一步使用 .decode() 方法将其转换回文本字符串。
"""

print('-------------------')

"""json 编码解码
使用 json 模块可以方便地进行 JSON（JavaScript Object Notation）数据的编码（序列化）和解码（反序列化）。
    JSON是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。
"""
import json

# 示例 Python 对象：一个字典
python_obj = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(python_obj)  # 将 Python 对象编码为 JSON 字符串
print(json_string)
"""json.dumps() 方法用于将 Python 对象转换成 JSON 格式的字符串。如果对象中包含不能直接转换成 JSON 的类型（如 datetime 对象），
    可以通过提供 default 参数来定义自定义的序列化函数。
"""
json_string = '{"name": "Bob", "age": 35, "city": "San Francisco"}'
python_obj1 = json.loads(json_string)
print(python_obj1)
"""json.loads() 方法用于将 JSON 格式的字符串转换回 Python 对象，通常是字典或列表。
此外，对于文件操作，还可以使用 json.dump() 和 json.load() 函数分别将 Python 对象写入文件和从文件读取并转换为 Python 对象：
"""
# 写入 JSON 数据到文件
with open('data.json', 'w') as f:
    json.dump(python_obj, f)

# 从文件读取 JSON 数据并转换为 Python 对象
with open('data.json', 'r') as f:
    loaded_obj = json.load(f)

print(loaded_obj)  # 输出与之前写入文件的对象相同

import datetime
from datetime import date

date_t = date(2022, 1, 3)
print(date_t)
print(date.today())
print(date.today().month)
print(date.fromtimestamp(1606639383))
