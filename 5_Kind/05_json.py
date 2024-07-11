"""json 与 字典"""
import json

print('---------------------------字典转换为JSON字符串----------------------------')
books_map = {'name': 'python游戏编程', 'author': 'Bobby', 'start': 78, 'publish_at': '2022-8-9',
             'info': {'alias': 'python game programming', 'users': 10000, 'id': 999999999999999}}

"""将字典转换成json字符串,-----美化输出-----"""
# json_string = json.dumps(books_map, indent=4, sort_keys=False)
json_string = json.dumps(books_map, indent='******', sort_keys=False)

print(json_string)
"""输出结果
{
    "name": "python\u6e38\u620f\u7f16\u7a0b",
    "author": "Bobby",
    "start": 78,
    "publish_at": "2022-8-9",
    "info": {
        "alias": "python game programming",
        "users": 10000,
        "id": 999999999999999
    }
}

{
******"name": "python\u6e38\u620f\u7f16\u7a0b",
******"author": "Bobby",
******"start": 78,
******"publish_at": "2022-8-9",
******"info": {
************"alias": "python game programming",
************"users": 10000,
************"id": 999999999999999
******}
}

"""

print('---------------------------将JSON字符串转换为字典----------------------------')

"""将JSON字符串转换为字典"""

json_data = '{"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "Physics"]}'

dict_data = json.loads(json_data)
print(dict_data)
"""输出结果

{'name': 'Alice', 'age': 30, 'is_student': False, 'courses': ['Math', 'Physics']}
"""

print('--------------------------将字典写入JSON文件：使用json.dump()。----------------------------')

with open('data.json', 'w') as json_file:
    json.dump(books_map, json_file)

print('--------------------------从JSON文件读取到字典：使用json.load()。----------------------------')
"""
使用这个 转换表 将 fp (一个支持 .read() 并包含一个 JSON 文档的 text file 或者 binary file) ---反序列化---为一个 Python 对象。
使用这个 转换表 将 s (一个包含 JSON 文档的 str, bytes 或 bytearray 实例) 反序列化为 Python 对象。
"""
with open('data.json', 'r') as json_file1:
    response = json.load(json_file1)

print(response)

print('------------------------拓展JSONEncoder------------------------')


class ComplexEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, complex):
            return [o.real, o.imag]
        return json.JSONEncoder.default(self, o)


print(json.dumps(2 + 3j, cls=ComplexEncoder))
print(ComplexEncoder().encode(2 + 1j))
print(list(ComplexEncoder().iterencode(2 + 1j)))

print('------------------------request请求返回的response，调用.json()------------------------')
"""当您在发送一个HTTP请求后，通常会收到一个响应（Response）。
在很多现代的编程语言和库中，对于这个响应对象，调用.json()方法是为了将响应体中的JSON格式数据转换为可操作的对象或字典。
    这样做的目的是使得开发者能够方便地处理这些数据，进行后续逻辑操作
"""
import requests

response = requests.get('https://api.example.com/data')

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()  # 将响应内容转换为Python字典
    print(data)
else:
    print(f"Request failed with status {response.status_code}")

"""loads 是Python中用于反序列化JSON字符串的函数，它属于 json 模块。
    当你有一个JSON格式的字符串，并且想要将其转换为Python的数据结构（如字典、列表等），就会使用 loads 函数。
    然而，当我们讨论HTTP请求的响应处理时，通常不会直接用到 loads，原因如下：
    
数据来源不同：
    loads 用于处理已经存在于内存中的JSON字符串。
        比如，你可能从文件读取了一个JSON字符串，或者收到了一个JSON格式的消息。
    而在处理HTTP请求响应时，如前所述，使用 .json() 方法（在requests库中）或类似的机制（其他语言和库中），
    是因为响应对象本身直接提供了将响应体内容（假设是JSON格式）转换为语言原生数据结构的功能。
自动化处理：
    库如requests为了简化开发者的工作，内置了对JSON响应的处理。这意味着你不需要手动读取响应的原始文本内容，再用 loads 去解析，库已经帮你完成了这一步。
错误处理和便捷性：
    使用 .json() 方法还内置了对响应内容类型的检查和错误处理，如果响应不是有效的JSON格式，这些库通常会抛出异常，便于开发者捕获和处理。
上下文适用性：
    loads 更适用于那些你直接控制或明确知道是JSON字符串的场景，比如处理配置文件、数据库中的JSON字段等。
    在网络请求上下文中，使用响应对象提供的方法直接获取解析后的数据，更加自然和高效。
    
总结来说，虽然 loads 是一个强大的工具，尤其在处理存储或传输中的JSON数据时，但在处理HTTP响应时，
    直接使用响应对象提供的方法（如Python的requests库中的 .json()）更加方便和直接，因为它直接针对网络请求的上下文进行了优化。
"""
