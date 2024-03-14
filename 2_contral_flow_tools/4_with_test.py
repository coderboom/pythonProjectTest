"""with"""
"""上下文管理器，with
获取资源（上文）、操作资源（操作）、释放资源（下文），都是基于IO的操作，这些资源往往是有限的，如果不及时关闭会造成浪费和错误。

实现一个上下文赶礼器，需要实现__enter__和__exit__方法，__enter__方法返回资源，__exit__方法释放资源。

实用场景：
打开一个文件，然后进行操作，操作完成后关闭文件资源
连接一个数据库，然后进行操作，操作完成后关闭连接
调用打开摄像头，然后拍照，操作完成后关闭
连接服务器，然后获取数据上传数据，操作完成关闭连接
使用其他外设
等等
"""


class SimpleContextManager:
    def __init__(self, resource_name):
        self.resource_name = resource_name

    def __enter__(self):
        print(f"Opening the resource: {self.resource_name}")
        # 这里可以替换为实际的资源获取操作，例如：file = open(self.resource_name, 'r')
        self.resource = open(self.resource_name)
        return self  # 返回一个可操作的对象（在这个例子中返回自身）

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing the resource: {self.resource_name}")
        # 在这里执行资源清理工作，如关闭文件：file.close()
        # 如果exc_type、exc_value和traceback都不为空，则异常发生并传播，除非返回True以抑制异常
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
            return False  # 默认情况下，不抑制异常，让异常继续向上抛出
        else:
            print("No exceptions were raised.")
        return True  # 如果希望在此处结束异常处理，可以返回True


# 使用上下文管理器
# with SimpleContextManager(
#         "/Users/chenhao/PycharmProjects/pythonProjectTest/2_contral_flow_tools/name_dddddd.txt") as cm:
#     print(f"Working with the resource...")
#     # 在此处进行对资源的操作
#
#     print(cm.resource_name)

"""当使用 with 语句时，程序会自动调用上下文管理器的 __enter__ 方法开始资源管理，并在 with 块结束后调用 __exit__ 方法来清理资源，即使在块内部发生了异常也是如此
1、自动调用 __enter__方法，获取资源
2、运行with块内部的代码
3、with块内部代码运行完成后，自动调用 __exit__ 方法来清理资源，即使在块内部发生了异常
"""
with open("/Users/chenhao/PycharmProjects/pythonProjectTest/2_contral_flow_tools/name_dddddd.txt", 'r') as f:
    print(f.read())


"""注意：在实际开发中，直接使用内置的open()函数作为上下文管理器通常更为简洁，因为它已经内建了对上下文管理协议的支持："""
