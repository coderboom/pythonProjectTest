"""3w 访问"""
import requests

"""网站访问的基本原理涉及多个步骤，从用户在浏览器中输入网址到最终网页内容呈现在屏幕上。以下是该过程的详细描述：
域名解析：
    当用户在浏览器地址栏中输入一个网址（例如：www.example.com）后，首先需要将这个域名转换成对应的IP地址。
    这是因为互联网上的设备是通过IP地址进行通信的。这一过程通常由DNS（Domain Name System，域名系统）完成，即DNS查询。
TCP/IP三次握手：
    获取了目标服务器的IP地址后，浏览器会与服务器建立TCP连接，这涉及到TCP/IP协议中的“三次握手”过程： 
    a. 客户端发送一个带有SYN标志的数据包给服务器，请求建立连接。 
    b. 服务器收到SYN后，回应一个带有SYN和ACK标志的数据包，表示确认并希望也建立连接。
    c. 客户端再发送一个带有ACK标志的数据包，确认连接建立成功。
HTTP请求：
    建立好TCP连接后，客户端（浏览器）构造一个HTTP请求报文，并通过已建立的连接将其发送给服务器。
    请求报文中包含诸如请求方法（GET、POST等）、请求URL、HTTP版本、头部信息（如User-Agent、Accept-Language、Cookie等）以及可能的请求体数据。
服务器处理请求：
    服务器接收到HTTP请求后，根据请求的内容来执行相应的操作，比如读取文件、执行脚本、查询数据库等，并生成HTTP响应内容。
HTTP响应：
    服务器完成请求处理后，将生成的响应内容打包成HTTP响应报文，其中包括状态码（如200 OK、404 Not Found等）、
    响应头部信息（如Content-Type、Set-Cookie等）以及响应主体（网页HTML、JSON数据或其他类型的内容）。
数据传输与渲染：
    浏览器接收HTTP响应报文，并根据其中的状态码判断请求是否成功。
    如果成功，则开始下载响应主体中的数据，如果是HTML文档，浏览器会对文档进行解析，构建DOM树结构，并根据CSS样式和JavaScript脚本进一步渲染页面内容。
资源加载：
    HTML文档中可能会引用其他资源（如图片、CSS样式表、JavaScript文件等），浏览器还会针对这些资源发起额外的HTTP请求，并加载、解析及应用它们。
断开连接：
    在完成数据交换之后，为了释放系统资源，TCP连接通常会在完成任务后关闭，这涉及到了TCP四次挥手的过程。
整个流程确保了用户能够顺利访问到互联网上的各种网站资源。
"""
print('------------------域名解析：----------------')
"""
域名解析（DNS Resolution）是一种将人类可读的域名（例如：www.example.com）转换为计算机可以识别的IP地址（如192.0.2.1）的过程。
IP地址：IP地址（Internet Protocol Address）是互联网协议中用于唯一标识网络中设备的数字标签。
    它是一个逻辑地址，确保在互联网上或本地网络中的不同设备能够相互定位和通信。
    每个连接到互联网的设备（如计算机、智能手机、服务器、路由器等）都需要分配一个唯一的IP地址。
    
    IP地址通常采用32位或128位二进制格式表示，但在日常使用中为了方便阅读和记忆，通常会将其转换成点分十进制形式，
    例如IPv4地址常见的格式为 xxx.xxx.xxx.xxx，其中每个“xxx”代表0到255之间的一个十进制数。例如：192.0.2.1 是一个合法的IPv4地址。
    
    IPv6地址则由8组4个十六进制数字组成，每组之间用冒号分隔，例如：2001:0db8:85a3:0000:0000:8a2e:0370:7334。
        IPv4：传统的IP地址版本，总共有大约42亿个不同的地址（2^32），随着互联网设备数量的增长，IPv4地址资源逐渐耗尽。
        IPv6：下一代的IP地址版本，提供了远超IPv4的大规模地址空间，理论上可以支持几乎无限多的设备连接到互联网（2^128个地址）。
        
    IP地址的主要功能包括：
        网络寻址：通过IP地址，数据包可以在互联网上传输至正确的目标设备。
        路由选择：路由器根据IP地址来决定如何转发数据包以到达目的地。
        网络隔离：不同网段之间的设备可以通过子网掩码和IP地址进行逻辑隔离。
        
在实际操作中，这个过程涉及到以下步骤：
    用户请求： 
        当用户在浏览器或其他应用中输入一个域名并请求访问时，应用程序会发起一个域名解析请求。
    本地DNS缓存查询： 
        计算机首先会在本地DNS缓存中查找该域名对应的IP地址。如果之前已经成功解析过此域名并且缓存未过期，则直接返回IP地址。
    系统DNS缓存查询： 
        如果本地缓存没有找到结果，则操作系统会查询自身的DNS缓存（对于大多数现代操作系统而言）。
    本地DNS服务器查询： 
        若系统缓存也无记录，请求会被发送到用户的本地DNS服务器（通常是ISP提供的）。本地DNS服务器负责与互联网上的其他DNS服务器交互以获取答案。
    递归查询： 
        本地DNS服务器执行递归查询过程，它会依次向根域名服务器、顶级域名服务器（TLD，如.com、.org等）、二级域名服务器（如example.com）询问，
        直到找到权威DNS服务器，该服务器负责提供确切的IP地址。
    迭代查询： 
        在某些情况下，DNS服务器之间也可能进行迭代查询，即每个DNS服务器只告诉下一个应查询哪个服务器，而不是直接提供答案。
    响应和缓存： 
        当权威DNS服务器提供了域名对应IP地址后，这一信息通过链路逐级返回给本地DNS服务器，并最终到达用户计算机。
        同时，这些信息会在各个层次的DNS服务器上缓存一定时间，以便后续更快地响应相同或相关域名的查询请求。
    建立连接： 
        用户计算机获得了域名对应的IP地址后，使用这个IP地址建立与目标网站服务器之间的TCP/IP连接，从而完成网页或者其他网络资源的访问。
        
在Python中，虽然不直接涉及上述复杂的域名解析流程，但可以通过第三方库如socket或dnspython等来模拟和控制域名解析的操作。例如，socket.gethostbyname()函数可以用于将域名转换成IP地址。
"""

print('------------------TCP/IP三次握手：----------------')
"""
TCP/IP（Transmission Control Protocol/Internet Protocol）三次握手是建立TCP连接时必须经过的步骤，
    用于在客户端和服务器之间同步序列号和确认应答，确保数据传输的可靠性。以下是三次握手的具体过程：
第一次握手：
    客户端（Client）想要与服务器（Server）建立TCP连接，首先向服务器发送一个SYN (Synchronize Sequence Numbers) 数据包，
    这个数据包中包含一个随机产生的序列号 seq = x，表示客户端初始序号。
    客户端进入SYN_SENT状态，等待服务器确认。
第二次握手：
    服务器接收到客户端的SYN请求后，如果同意建立连接，则会回复一个数据包，该数据包同时包含对客户端SYN的确认信息ACK (Acknowledgment) 和一个新的SYN请求。
    具体来说，服务器设置自己的序列号 seq = y，并将确认号 ack = x + 1 发送给客户端，表示它已经收到了客户端的SYN，并准备进行连接。
    服务器此时也进入了SYN_RECEIVED状态。
第三次握手：
    客户端收到服务器的SYN+ACK后，需要再次回应一个确认数据包给服务器，其中包含确认号 ack = y + 1，以确认已收到服务器的SYN，同时也表明自己已准备好开始数据传输。
    此时，客户端的状态变为ESTABLISHED。
    当服务器收到客户端发来的确认信息后，也会进入ESTABLISHED状态。
    至此，双方均确认了彼此的接收和发送能力，以及对方的初始序列号，TCP连接建立成功，接下来就可以在这一可靠的连接上进行双向的数据交换了。
    
三次握手的主要目的是为了防止旧的重复连接请求被服务器误认为是新的连接请求，通过这种机制可以确保每次连接都是全新的、可靠的
"""
import socket, threading

# 创建服务器端Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))  # 绑定本地IP和端口
server_socket.listen(1)  # 开始监听连接请求

print("Server is listening...")


# 客户端与服务器建立连接的模拟
def simulate_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 是Python中创建客户端套接字对象的一行代码，
    # 用于进行TCP/IP协议的网络通信。该语句详解如下：
    # socket.socket()：
    # 这是Python内置socket模块提供的函数，用来创建一个套接字（socket）对象。套接字是计算机之间通信的一种端点，用于实现不同主机上的应用程序之间的数据交换。
    # 参数说明：
    # socket.AF_INET：
    #   它是一个常量，表示使用IPv4地址簇（Address Family）。这意味着我们将通过IPv4地址和端口号来标识网络中的主机和服务。
    # socket.SOCK_STREAM：
    #   这也是一个常量，表示选择流式套接字类型，即TCP（Transmission Control Protocol）。
    #   TCP提供的是面向连接、可靠的数据传输服务，它确保了数据包的顺序到达以及丢失或损坏数据包的重新发送。
    # 结果：
    # 通过调用 socket.socket(socket.AF_INET, socket.SOCK_STREAM) 创建了一个基于IPv4协议且使用TCP作为传输层协议的客户端套接字对象，即client_socket。
    # 使用这个套接字对象，我们可以进一步执行连接到服务器、发送和接收数据等操作。
    # 例如，调用 client_socket.connect((server_address, server_port)) 来连接到指定地址和端口的服务器，
    # 或者通过 client_socket.send(data) 和 client_socket.recv(buffer_size) 发送和接收数据。

    try:
        # 第一次握手：客户端发起SYN
        client_socket.connect(('localhost', 8000))
        print("Client: SYN sent.")

        # 接收服务器的SYN+ACK
        data = client_socket.recv(1024)
        if len(data) > 0:
            print(f"Client: Received SYN+ACK from server. Seq: {data}")

        # 第三次握手：客户端发送ACK
        # 在真实TCP协议栈中，这个ACK是包含在客户端对服务器SYN+ACK的回复中的
        # 这里简化表示为单独发送ACK
        # （实际上在connect()调用后，操作系统会自动完成整个握手流程）
        # ACK的数据在这里不重要，因为我们只是模拟
        # client_socket.sendall(b'ACK')  # 假设我们发送一个确认报文

        print("Client: ACK sent.")
        print("TCP connection established.")

        # 连接成功后的行为（例如传输数据、关闭连接等）
        # ...

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()


# 启动客户端模拟
simulate_client_thread = threading.Thread(target=simulate_client)
simulate_client_thread.start()

# 等待并接受客户端连接（服务器端）
client_connection, client_address = server_socket.accept()
print(f"Server: Accepted connection from {client_address}.")
print("TCP connection established on the server side.")

# 在这里服务器也会收到客户端的ACK，但通常无需显式处理
# 因为accept()之后连接已经建立好

# 连接建立后的其他操作...

# 最后清理资源
client_connection.close()
server_socket.close()

print('------------------HTTP请求：----------------')

# 发送一个GET请求到指定URL
response = requests.get('https://www.baidu.com')

# 检查响应状态码
if response.status_code == 200:
    # 如果状态码为200，表示请求成功
    print("Response successful, HTTP status code: ", response.status_code)

    # 获取并打印服务器返回的内容
    html_content = response.text
    print(html_content)
else:
    print(f"Request failed with status code: {response.status_code}")

# 可以获取更多响应信息，例如头部信息
headers = response.headers
print("Response headers:", headers)

# 对于POST请求，可以这样操作：
data = {'key1': 'value1', 'key2': 'value2'}
post_response = requests.post('https://www.example.com/api/endpoint', data=data)

# 同样检查POST请求的响应状态码和内容
