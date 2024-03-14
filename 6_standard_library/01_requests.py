"""request"""
import json

import requests

"""
    属性或方法	                                说明
    apparent_encoding	                        编码方式
    close()	                                    关闭与服务器的连接
    content	                                    返回响应的内容，以字节为单位
    cookies	                                    返回一个 CookieJar 对象，包含了从服务器发回的 cookie
    elapsed	                                    返回一个 timedelta 对象，包含了从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。
                                                    比如 r.elapsed.microseconds 表示响应到达需要多少微秒。
    encoding	                                解码 r.text 的编码方式
    headers	                                    返回响应头，字典格式
    history	                                    返回包含请求历史的响应对象列表（url）
    is_permanent_redirect	                    如果响应是永久重定向的 url，则返回 True，否则返回 False
    is_redirect	                                如果响应被重定向，则返回 True，否则返回 False
    iter_content()	                            迭代响应
    iter_lines()	                            迭代响应的行
    json()	                                    返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误)
    links	                                    返回响应的解析头链接
    next	                                    返回重定向链中下一个请求的 PreparedRequest 对象
    ok	                                        检查 "status_code" 的值，如果小于400，则返回 True，如果不小于 400，则返回 False
    raise_for_status()	                        如果发生错误，方法返回一个 HTTPError 对象
    reason	                                    响应状态的描述，比如 "Not Found" 或 "OK"
    request	                                    返回请求此响应的请求对象
    status_code	                                返回 http 的状态码，比如 404 和 200（200 是 OK，404 是 Not Found）
    text	                                    返回响应的内容，unicode 类型数据
    url	                                        返回响应的 URL
"""
print('------------所有请求方式------------------')
"""
get(url, params, args)	        发送 GET 请求到指定 url
post(url, data, json, args)	    发送 POST 请求到指定 url
head(url, args)	                发送 HEAD 请求到指定 url
patch(url, data, args)	        发送 PATCH 请求到指定 url
delete(url, args)	            发送 DELETE 请求到指定 url
put(url, data, args)	        发送 PUT 请求到指定 url
request(method, url, args)	    向指定的 url 发送指定的请求方法
"""

print('-------------------get请求-------------')
"""
requests.get() 方法是 Python requests 库中的函数，用于发送 HTTP GET 请求。以下是该方法可以接受的一些主要参数：
url (必需)：
    类型：字符串
    描述：请求的完整URL。
params (可选)：
    类型：字典、列表元组或字节
    描述：作为查询字符串附加到URL上的键值对。例如，{'key1': 'value1', 'key2': 'value2'} 将转换为 ?key1=value1&key2=value2 并添加到URL末尾。
headers (可选)：
    类型：字典
    描述：HTTP头部信息，如用户代理、认证凭据等。
data (可选)：
    类型：字典、字符串、字节或其他可迭代对象
    描述：通常GET请求不会携带请求体数据，但如果需要通过query string传递大量数据（虽然不推荐），也可以使用此参数。
json (可选)：
    类型：任何可JSON序列化的Python对象
    描述：如果提供了这个参数，它会被转换成JSON格式，并设置请求内容类型为 application/json。注意GET请求通常不需要提供json数据，而是用于POST、PUT等方法中。
cookies (可选)：
    类型：字典或CookieJar对象
    描述：要随请求发送的cookies。
    
    cookies_dict = {'session_id': '123456', 'user_token': 'abcdef'}
    response = requests.get('https://example.com/path', cookies=cookies_dict)
    
    CookieJar对象：requests库也支持使用 requests.cookies.RequestsCookieJar 对象来管理cookies。
        这个类类似于浏览器中的cookie容器，可以保存多个cookies，并且处理过期和其他复杂情况。创建或加载此类对象后，也可以将其传递给cookies参数。
    通过设置cookies参数，可以实现保持用户会话状态、复用身份验证令牌等功能，从而在一系列请求之间维持一致的行为。
        对于爬虫程序而言，这尤其有用，因为它可以帮助模拟用户登录后的浏览行为。
    
allow_redirects (可选，默认为True)：
    类型：布尔值
    描述：是否允许重定向。如果设为False，则不会自动跟随重定向响应。
timeout (可选，默认为None)：
    类型：数字或 (connect_timeout, read_timeout) 元组
    描述：设置请求超时时间（以秒为单位）。
proxies (可选)：
    类型：字典
    描述：代理服务器设置，如需通过代理发送请求。
verify (可选，默认为True)：
    类型：布尔值或字符串路径
    描述：验证SSL证书，若设为False则不验证。如果是字符串，则指向CA_BUNDLE文件或目录。
stream (可选，默认为False)：
    类型：布尔值
    描述：是否立即下载响应体。设为True可以延迟下载以便流式处理。
cert (可选)：
    类型：(cert, key) 元组
    描述：本地SSL证书用于客户端身份验证。
"""
# 定义要访问的URL
url = 'https://www.runoob.com/'
# 发送一个GET请求
response = requests.get(url)

# 检查响应状态码，确保请求成功（200表示成功）
if response.status_code == 200:
    print(response.status_code)
    print(response.reason)  # 响应状态的描述
    print('cookies:', response.cookies)
    print(response.url)
    # 获取并打印响应内容
    # data = response.json()  # 如果返回的是JSON格式的数据
    # print(data)

    # 或者，如果返回的是文本内容
    # text_content = response.text
    # print(text_content)
else:
    print(f"请求失败，状态码：{response.status_code}")

# 可以获取其他响应信息，如头部信息
headers = response.headers
print("响应头部信息：", headers)

# 添加请求头或参数的例子：
headers = {'User-Agent': 'My Custom User Agent'}
params = {'key1': 'value1', 'key2': 'value2'}

# 使用自定义请求头和参数发送GET请求
response_with_headers_and_params = requests.get(url, headers=headers, params=params)
"""在上述代码中：
requests.get(url) 向指定的URL发送一个HTTP GET请求。
response 是对服务器响应的一个封装，包含了所有关于此次HTTP请求的信息，如状态码、响应体、头部等。
    response.status_code：HTTP响应状态码，例如200（成功）、404（未找到）、500（服务器内部错误）等。
    response.headers：一个字典对象，包含HTTP响应头部的所有信息，如Content-Type、Content-Length、Server、Date、Set-Cookie等。
    response.text：以文本形式返回的内容。这个属性获取的是解码后的响应体数据，默认编码根据HTTP头部的'Content-Type'字段自动确定，
        如果无法自动确定，则会尝试猜测。
    response.content：原始的二进制形式的响应内容，适用于需要处理非文本类型的数据，如图片、音频、视频等。
    response.json()：如果响应内容是JSON格式，可以调用此方法将其解析为Python字典或列表。如果响应内容不是有效的JSON格式，该方法将抛出异常。
    response.url：实际发出请求后的完整URL，可能与最初提供的URL不同，因为可能会有重定向。
    response.history：对于发生了重定向的情况，这个属性是一个包含所有中间历史响应的对象列表。
    response.cookies：一个RequestsCookieJar对象，包含从服务器接收的cookies。

params 参数用于向URL添加查询参数（query parameters）。在实际请求的URL中，这些参数将以“？”分隔，并以“&”连接不同的键值对。
其他属性和方法：还包括了elapsed（请求所花费的时间）、encoding（响应内容的编码方式）、raise_for_status（检查HTTP状态码并根据需要抛出异常）等。
"""


reponse_json = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
print(reponse_json.json())
print('-----------------------------')

kw = {'s': 'python 教程'}
# 设置请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

from fake_useragent import UserAgent  # 伪装浏览器库

ua = UserAgent(browsers=['edge', 'chrome'])
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要 urlencode()
response = requests.get("https://www.runoob.com/", params=kw, headers=ua.random)

# 查看响应状态码
print(response.status_code)

# 查看响应头部字符编码
print(response.encoding)

# 查看完整url地址
print(response.url)  # https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)

"""
定义要访问的URL
url = 'https://api.example.com/data'
# 定义GET请求的参数
params = {'key1': 'value1', 'key2': 'value2'}
# 发送带有参数的GET请求
response = requests.get(url, params=params)
# 检查响应状态码并处理响应内容
if response.status_code == 200:
    # 获取并打印响应的内容
    print(response.json())  # 如果返回的是JSON格式的数据
else:
    print(f"请求失败，状态码：{response.status_code}")

# 请求URL会自动附加参数，例如：
# 实际发出的请求可能是：https://api.example.com/data?key1=value1&key2=value2
"""

print('------------post请求-----------------')
"""
requests.post() 方法是 Python requests 库中的函数，用于发送 HTTP POST 请求。以下是该方法可以接受的一些主要参数：
url (必需)：
    类型：字符串
    描述：请求的完整URL。
data (可选)：
    类型：字典、列表元组、字符串或字节
    描述：要作为POST请求主体的数据。对于表单数据（如键值对），通常以字典形式提供；如果需要发送JSON数据，则应先将其转换为字符串格式（例如使用 json.dumps()）。
json (可选)：
    类型：任何可JSON序列化的Python对象
    描述：如果提供了这个参数，它会被自动转换成JSON格式，并设置请求内容类型为 application/json。优先级高于 data 参数，即二者不能同时使用。
params (可选)：
    类型：字典、列表元组或字节
    描述：作为查询字符串附加到URL上的键值对。虽然POST请求的主要数据通常放在请求体中，但有时也会在URL上携带额外的查询参数。
headers (可选)：
    类型：字典
    描述：HTTP头部信息，包括但不限于Content-Type、Authorization等。
cookies (可选)：
    类型：字典或CookieJar对象
    描述：要随请求发送的cookies。
files (可选)：
    类型：字典
    描述：用于上传文件时使用，键是上传文件字段名，值可以是打开的文件对象、二进制内容、或者包含 filename 和 content 的元组。
data 或 files 与 multipart/form-data:
    当同时需要发送普通表单数据和文件时，通常需要设置 headers['Content-Type'] = 'multipart/form-data'，此时 requests 库会自动处理相关编码工作。
allow_redirects (可选，默认为True)：
    类型：布尔值
    描述：是否允许重定向。
timeout (可选，默认为None)：
    类型：数字或 (connect_timeout, read_timeout) 元组
    描述：设置请求超时时间（以秒为单位）。
proxies (可选)：
    类型：字典
    描述：代理服务器设置，如需通过代理发送请求。
verify (可选，默认为True)：
    类型：布尔值或字符串路径
    描述：验证SSL证书，若设为False则不验证。如果是字符串，则指向CA_BUNDLE文件或目录。
cert (可选)：
    类型：(cert, key) 元组
    描述：本地SSL证书用于客户端身份验证。
"""

# 定义要访问的URL
url = 'https://www.runoob.com/try/ajax/demo_post2.php'

# 定义需要发送的数据，可以是字典形式（适用于表单数据）或json字符串（适用于JSON格式）
data = {'fname': 'RUNOOB', 'lname': 'Boy'}

# 发送POST请求
response = requests.post(url, data=data)

# 检查响应状态码，确保请求成功
if response.status_code == 200:
    # 如果服务器返回的是JSON内容，则解析为字典
    if 'application/json' in response.headers.get('Content-Type'):
        result = response.json()
        print("Response JSON content:", result)
    else:
        # 如果不是JSON内容，则获取并打印文本内容
        text_content = response.text
        print("Response text content:", text_content)
else:
    print(f"请求失败，状态码：{response.status_code}")

# 获取URL
print(response.url)
# 获取响应码
print(response.status_code)
# 可以获取其他响应信息，如头部信息
headers = response.headers
print("响应头部信息：", headers)

"""
# 添加请求头、文件上传等更复杂操作的例子：
headers = {'Authorization': 'Bearer your_token'}
files = {'file': open('path_to_your_file', 'rb')}  # 用于上传文件

# 使用自定义请求头和文件上传发送POST请求
response_with_headers_and_files = requests.post(url, headers=headers, data=data, files=files)
"""

print('-------------------head请求-----------------------')
"""
requests.head() 方法是 Python requests 库中的函数，用于发送 HTTP HEAD 请求。HEAD 请求与 GET 请求类似，
但服务器只返回响应头信息，而不返回实际的响应体内容。以下是该方法可以接受的一些主要参数：
url (必需)：
    类型：字符串
    描述：请求的完整URL。
params (可选)：
    类型：字典、列表元组或字节
    描述：作为查询字符串附加到URL上的键值对。
headers (可选)：
    类型：字典
    描述：HTTP头部信息，如用户代理、认证凭据等。
allow_redirects (可选，默认为True)：
    类型：布尔值
    描述：是否允许重定向。
cookies (可选)：
    类型：字典或CookieJar对象
    描述：要随请求发送的cookies。
timeout (可选，默认为None)：
    类型：数字或 (connect_timeout, read_timeout) 元组
    描述：设置请求超时时间（以秒为单位）。
proxies (可选)：
    类型：字典
    描述：代理服务器设置，如需通过代理发送请求。
verify (可选，默认为True)：
    类型：布尔值或字符串路径
    描述：验证SSL证书，若设为False则不验证。如果是字符串，则指向CA_BUNDLE文件或目录。
cert (可选)：
    类型：(cert, key) 元组
    描述：本地SSL证书用于客户端身份验证。
    
由于HEAD请求通常不携带实体数据，所以 data 和 json 参数在 requests.head() 方法中通常是不必要的。
    HEAD请求主要用于获取资源的元信息，例如查看网页的最后修改时间、文件大小等。
"""

print('-------------------patch请求-----------------------')
"""requests.patch() 方法是 Python requests 库中的函数，用于发送 HTTP PATCH 请求。PATCH 请求通常用于更新资源的部分内容。
以下是该方法可以接受的一些主要参数：
url (必需)：
    类型：字符串
    描述：请求的完整URL。
data (可选)：
    类型：字典、列表元组、字符串或字节
    描述：要作为PATCH请求主体的数据，通常用于传输需要更新的部分资源内容。对于表单数据（如键值对），通常以字典形式提供；如果需要发送JSON数据，则应先将其转换为字符串格式（例如使用 json.dumps()）。
json (可选)：
    类型：任何可JSON序列化的Python对象
    描述：如果提供了这个参数，它会被自动转换成JSON格式，并设置请求内容类型为 application/json。优先级高于 data 参数，即二者不能同时使用。
headers (可选)：
    类型：字典
    描述：HTTP头部信息，包括但不限于Content-Type、Authorization等，比如在发送JSON数据时，应确保设置正确的Content-Type，如 'Content-Type': 'application/json'。
params (可选)：
    类型：字典、列表元组或字节
    描述：作为查询字符串附加到URL上的键值对。
cookies (可选)：
    类型：字典或CookieJar对象
    描述：要随请求发送的cookies。
timeout (可选，默认为None)：
    类型：数字或 (connect_timeout, read_timeout) 元组
    描述：设置请求超时时间（以秒为单位）。
allow_redirects (可选，默认为True)：
    类型：布尔值
    描述：是否允许重定向。
proxies (可选)：
    类型：字典
    描述：代理服务器设置，如需通过代理发送请求。
verify (可选，默认为True)：
    类型：布尔值或字符串路径
    描述：验证SSL证书，若设为False则不验证。如果是字符串，则指向CA_BUNDLE文件或目录。
cert (可选)：
    类型：(cert, key) 元组
    描述：本地SSL证书用于客户端身份验证。
"""

print('-------------------delete请求-----------------------')
"""
requests.delete() 方法是 Python requests 库中的函数，用于发送 HTTP DELETE 请求。DELETE 请求通常用于删除指定资源。以下是该方法可以接受的一些主要参数：
url (必需)：
    类型：字符串
    描述：请求的完整URL，即要删除的资源的地址。
data (可选)：
    类型：字典、列表元组、字符串或字节
    描述：虽然HTTP规范中DELETE方法通常不携带实体数据（请求体），但某些API可能允许在DELETE请求中传递额外的数据。如果需要这样做，请以适当格式提供数据。
json (可选)：
    类型：任何可JSON序列化的Python对象
    描述：与 data 类似，用于发送JSON格式的数据作为请求体，尽管这不是DELETE方法的标准用法。
headers (可选)：
    类型：字典
    描述：HTTP头部信息，如认证凭据、自定义请求头等。
params (可选)：
    类型：字典、列表元组或字节
    描述：作为查询字符串附加到URL上的键值对。
cookies (可选)：
    类型：字典或CookieJar对象
    描述：要随请求发送的cookies。
timeout (可选，默认为None)：
    类型：数字或 (connect_timeout, read_timeout) 元组
    描述：设置请求超时时间（以秒为单位）。
allow_redirects (可选，默认为True)：
    类型：布尔值
    描述：是否允许重定向。
proxies (可选)：
    类型：字典
    描述：代理服务器设置，如需通过代理发送请求。
verify (可选，默认为True)：
    类型：布尔值或字符串路径
    描述：验证SSL证书，若设为False则不验证。如果是字符串，则指向CA_BUNDLE文件或目录。
cert (可选)：
    类型：(cert, key) 元组
    描述：本地SSL证书用于客户端身份验证。
"""
print('-------------------put请求-----------------------')
"""
requests.put() 方法是 Python requests 库中的函数，用于发送 HTTP PUT 请求。PUT 请求通常用于替换目标资源的所有内容或创建新的资源（如果服务器支持）。
以下是该方法可以接受的一些主要参数：
url (必需)：
    类型：字符串
    描述：请求的完整URL，即要更新或创建资源的位置。
data (可选)：
    类型：字典、列表元组、字符串或字节
    描述：作为PUT请求主体的数据，通常用于传输整个资源的新内容。对于表单数据（如键值对），通常以字典形式提供；如果需要发送JSON数据，则应先将其转换为字符串格式（例如使用 json.dumps()）。
json (可选)：
    类型：任何可JSON序列化的Python对象
    描述：如果提供了这个参数，它会被自动转换成JSON格式，并设置请求内容类型为 application/json。优先级高于 data 参数，即二者不能同时使用。
headers (可选)：
    类型：字典
    描述：HTTP头部信息，包括但不限于Content-Type、Authorization等。例如，在发送JSON数据时，应确保设置正确的Content-Type，如 'Content-Type': 'application/json'。
params (可选)：
    类型：字典、列表元组或字节
    描述：作为查询字符串附加到URL上的键值对。
cookies (可选)：
    类型：字典或CookieJar对象
    描述：要随请求发送的cookies。
timeout (可选，默认为None)：
    类型：数字或 (connect_timeout, read_timeout) 元组
    描述：设置请求超时时间（以秒为单位）。
allow_redirects (可选，默认为True)：
    类型：布尔值
    描述：是否允许重定向。
proxies (可选)：
    类型：字典
    描述：代理服务器设置，如需通过代理发送请求。
verify (可选，默认为True)：
    类型：布尔值或字符串路径
    描述：验证SSL证书，若设为False则不验证。如果是字符串，则指向CA_BUNDLE文件或目录。
cert (可选)：
    类型：(cert, key) 元组
    描述：本地SSL证书用于客户端身份验证。
"""
print('-------------------request请求-----------------------')
"""
requests.request() 方法是 Python requests 库中的通用请求方法，它可以用于发送任何类型的HTTP请求。以下是该方法可以接受的一些主要参数：
method (必需)：
    类型：字符串
    描述：要执行的HTTP方法，如 'GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS' 等。
url (必需)：
    类型：字符串
    描述：请求的目标URL。
params (可选)：
    类型：字典、列表元组或字节
    描述：作为查询字符串附加到URL上的键值对。
data (可选)：
    类型：字典、列表元组、字符串或字节
    描述：要作为请求主体的数据，适用于POST、PUT等需要传输数据的方法。
json (可选)：
    类型：任何可JSON序列化的Python对象
    描述：如果提供了这个参数，它会被自动转换成JSON格式，并设置请求内容类型为 application/json。优先级高于 data 参数，即二者不能同时使用。
headers (可选)：
    类型：字典
    描述：HTTP头部信息，包括但不限于Content-Type、Authorization、User-Agent等。
cookies (可选)：
    类型：字典或CookieJar对象
    描述：要随请求发送的cookies。
files (可选)：
    类型：字典
    描述：当需要上传文件时使用，包含文件名和打开的文件对象或其他有效数据。
timeout (可选，默认为None)：
    类型：数字或 (connect_timeout, read_timeout) 元组
    描述：设置请求超时时间（以秒为单位）。
allow_redirects (可选，默认根据方法不同而不同)：
    类型：布尔值
    描述：是否允许重定向。
proxies (可选)：
    类型：字典
    描述：代理服务器设置，如需通过代理发送请求。
verify (可选，默认为True)：
    类型：布尔值或字符串路径
    描述：验证SSL证书，若设为False则不验证。如果是字符串，则指向CA_BUNDLE文件或目录。
cert (可选)：
    类型：(cert, key) 元组
    描述：本地SSL证书用于客户端身份验证。
stream (可选，默认为False)：
    类型：布尔值
    描述：是否立即下载响应体。设为True可以延迟下载以便流式处理。
"""
