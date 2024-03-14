"""OS"""
import os, time

"""模块介绍：
    os 是 Operation System（操作系统）的缩写。
    它是 Python 内置的标准库之一，不需要单独安装即可直接使用。
    os 模块封装了一系列与操作系统交互的函数，使得在编写 Python 代码时可以方便地进行跨平台的操作，包括文件和目录管理、环境变量操作、进程管理等。
文件和目录操作：
    获取状态信息：os.stat(path) 可以获取指定路径下文件或目录的状态信息，返回一个包含多个属性如大小、修改时间、权限等的元组。
    创建目录：os.mkdir(path) 创建单级目录；os.makedirs(path, exist_ok=True) 可递归创建多级目录并设置如果目标目录已存在则不引发异常。
    删除目录：os.rmdir(path) 删除空目录；os.removedirs(path) 递归删除空的父目录。
    重命名或移动文件/目录：os.rename(src, dst)。
    删除文件：os.remove(path)。
    获取当前工作目录：os.getcwd() 返回当前工作目录的绝对路径。
    切换工作目录：os.chdir(path) 更改当前工作目录至指定路径。
    列出目录内容：os.listdir(directory) 返回指定目录下的所有文件和子目录名列表。
路径处理：
    绝对路径和相对路径的转换与解析。
    使用 os.path 子模块提供了一系列处理路径的方法，例如：
    os.path.abspath(path) 获取绝对路径。
    os.path.join(a, b, ...) 将路径片段连接成一个完整的路径字符串。
    os.path.dirname(path) 提取路径中的目录部分。
    os.path.basename(path) 提取路径中的基本文件名。
    os.path.exists(path) 判断路径是否存在。
系统相关信息：
    获取操作系统类型：os.name 返回操作系统名，如 'posix' 表示类 Unix 系统，'nt' 表示 Windows 系统。
    获取环境变量：os.environ.get('VARIABLE_NAME') 获取环境变量值。
进程管理：
    虽然不是 os 模块的核心功能，但可以通过其提供的接口与其他模块配合，实现一些简单的进程管理，例如执行外部命令可使用 os.system(command) 或者 subprocess 模块。
    其他实用方法：
    查找特定目录树下的文件：可以结合 os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) 方法遍历目录及其子目录。
    处理文件权限和所有权等高级文件系统操作，如 os.chmod() 修改文件权限。
总之，os 模块在自动化脚本编写、文件系统管理、以及与操作系统底层交互方面具有广泛的应用价值。开发者通过熟练掌握该模块，能够更好地适应不同操作系统环境下的编程需求。
"""
# # 重命名文件（假设当前目录下存在文件 "old_file.txt"）
# old_file_name = "old_file.txt"
# new_file_name = "new_file.txt"
#
# # 执行重命名操作
# os.rename(old_file_name, new_file_name)
#
# # 如果文件不在当前工作目录，需要提供完整路径
# os.rename("/path/to/old_file.txt", "/path/to/new_file.txt")
#
# # 使用 os.remove() 函数可以删除指定的文件
#
# # 要删除的文件名
# file_to_delete = "file_to_remove.txt"
#
# # 执行删除操作
# os.remove(file_to_delete)
#
# # 同样，如果文件不在当前工作目录，需要提供完整路径
# os.remove("/path/to/file_to_remove.txt")

"""在执行这些操作之前，请确保你有权限访问和修改这些文件。
如果尝试删除或重命名的文件不存在，或者由于权限问题无法进行操作，上述函数将会抛出异常（如 FileNotFoundError 或 PermissionError）。
对于目录（文件夹），若要重命名或删除，应使用 os.rename() 和 shutil.rmtree()（删除整个目录及其内容）或 os.rmdir()（仅删除空目录）。
"""
print('---------------mkdir------------------')

"""创建新的目录"""
# 要创建的新目录路径
new_directory_path = "new_directory"

# 创建新目录
# os.mkdir(new_directory_path)

# 如果需要在多个层级上创建目录（例如，创建多级子目录），可以使用 `os.makedirs()` 函数
new_nested_directory_path = "path/to/new/nested/directory"
os.makedirs(new_nested_directory_path, exist_ok=True)  # 使用 `exist_ok=True` 可以避免在目录已存在时抛出异常

"""
os.mkdir()用于创建单个级别的目录。

os.makedirs()用于递归地创建多级目录。参数exist_ok=True是一个可选参数，当设置为True时，如果目标目录已经存在，
    那么不会引发错误（在Python 3.2版本及更高版本中引入此参数，默认情况下在目录已存在时会引发FileExistsError异常）
"""

"""改变当前工作目录
os.chdir() 是 Python 中 os 模块提供的一个函数，用于改变当前工作目录（Current Working Directory, CWD）。
    该函数允许程序动态地切换到文件系统中的其他目录。

注意事项：
提供的路径必须是存在的有效目录。
这个更改会影响当前运行的 Python 程序及其子进程。当程序退出后，终端或系统的当前工作目录不受影响。
如果路径错误或没有权限访问该目录，os.chdir() 会抛出 FileNotFoundError 或 PermissionError 异常。
"""

# 将当前工作目录更改为指定路径
# os.chdir('new_directory')

# 示例：将当前工作目录更改为/home/user/documents
# os.chdir('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/new_directory')

print('---------------getcwd------------------')
"""显示给出的当前目录"""
print(os.getcwd())  # /Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test

print('---------------rmdir------------------')
"""删除目录，删除目录前所有内容应该先被清除"""
# time.sleep(10)
# 删除单个目录
print(os.rmdir('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/path/to/new/nested/directory'))

# time.sleep(10)
# 递归删除空的父目录。
# print(os.removedirs('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/path'))

import shutil

"""这个函数会递归地删除指定目录下的所有内容，包括子目录和文件："""
del_directory_path = '/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/path'
# 删除目录树
shutil.rmtree(del_directory_path)
"""shutil.rmtree() 在删除前不会询问确认，因此请确保你提供的路径是正确的，并且你有权限删除该目录及其所有内容。
如果尝试删除的目录不存在或由于权限问题无法删除，该函数将抛出异常。例如，FileNotFoundError 表示目录不存在，
    而 PermissionError 表示没有足够的权限来执行删除操作。
"""

print('---------------os.getcwd()------------------')
# 返回当前工作目录的绝对路径。
print(os.getcwd())

print('---------------os.listdir(directory) ------------------')
# 返回指定目录下的所有文件和子目录名列表
print(os.listdir('/Users/chenhao/PycharmProjects/pythonProjectTest'))
print(os.listdir('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test'))

"""路径处理：
    绝对路径和相对路径的转换与解析。
    使用 os.path 子模块提供了一系列处理路径的方法，例如：
    os.path.abspath(path) 获取绝对路径。
    os.path.join(a, b, ...) 将路径片段连接成一个完整的路径字符串。
    os.path.dirname(path) 提取路径中的目录部分。
    os.path.basename(path) 提取路径中的基本文件名。
    os.path.exists(path) 判断路径是否存在。
"""
print('---------------os.path.abspath(path)------------------')
"""os.path.abspath(path) 是 Python os.path 模块中的一个函数，它的作用是将给定的路径转换成绝对路径。
参数：path（字符串类型），可以是一个相对路径或一个以 / （在 Unix 系统中）或 \\ （在 Windows 系统中）开始的绝对路径，
    也可以不包含任何斜杠，即仅仅是一个文件或目录名。

功能：
    如果 path 是一个相对路径，该函数会将其相对于当前工作目录（可以通过 os.getcwd() 获取）进行扩展，得到一个完整的绝对路径。
    如果 path 已经是一个绝对路径，则函数直接返回该路径不变。
    返回值：返回一个字符串，表示转换后的绝对路径。
例如，在Python程序中调用：
"""
relative_path = 'new_directory'
absolute_path = os.path.abspath(relative_path)  # 将给定的路径转换成绝对路径。
print(absolute_path)

print(os.path.abspath(
    '2_contral_flow_tools'))  # /Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/2_contral_flow_tools

"""os.path.abspath('2_contral_flow_tools') 将返回 '2_contral_flow_tools' 相对于当前执行该Python脚本的文件所在的绝对路径。
    根据注释所示，2_contral_flow_tools 和 /3_Module_test 是同一个父目录下的同级子目录。
因此，如果当前执行脚本的目录是 /Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test，
    并且 2_contral_flow_tools 也是这个目录下的一个目录，则 os.path.abspath('2_contral_flow_tools') 返回的结果将会是

结果： /Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/2_contral_flow_tools
"""

print('---------------os.path.join(a, b, ...)------------------')
"""os.path.join(a, b, ...) 是 Python 标准库 os.path 模块中的一个函数，用于将一个或多个路径名称组合成一个完整的、规范化的（在当前操作系统下）路径。
参数：接受任意数量的字符串作为参数，这些字符串代表了要拼接的路径部分，如目录名和文件名。
功能：
    将各个路径片段连接起来，并根据操作系统的路径分隔符进行正确连接。例如，在 Unix 系统中使用 /，而在 Windows 系统中使用 \ 或者 /。
    如果某个路径片段已经是绝对路径（以 / 或 \\ 开头），则后续的路径片段将基于这个绝对路径拼接。
    返回值：返回一个表示组合后完整路径的字符串。
示例：
"""

# 在 Unix/Linux 系统中
path = os.path.join('home', 'user', 'documents', 'file.txt')
# 输出结果为 'home/user/documents/file.txt'
print(path)

print('---------------os.path.dirname(path)------------------')
"""os.path.dirname(path) 是 Python os.path 模块中的一个函数，用于获取指定路径的目录部分。
参数：path（字符串类型），表示一个文件或目录的路径。

功能：从给定的路径中提取并返回其包含的目录部分。也就是说，它会去掉路径的最后一部分（即文件名或最后一个子目录名）。
返回值：返回一个字符串，代表了不包括最后一级文件或目录名在内的路径。
"""
print(os.path.dirname('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/new_directory'))
# /Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test

print('---------------os.path.basename(path) -------------------')
"""os.path.basename(path) 是 Python os.path 模块中的一个函数，用于从给定的路径中提取基本文件名或最后一级目录名。
参数：path（字符串类型），表示一个文件或目录的完整路径。

功能：此函数返回路径的最后一部分，即文件名（对于文件路径）或最后一个子目录名（对于目录路径）。
返回值：返回一个字符串，代表了路径中除去目录部分后的基本文件名或子目录名。
"""
print(os.path.basename('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/new_directory'))  # new_directory

print('--------------- os.path.exists(path) -------------------')
"""os.path.exists(path) 是Python内置的os模块中的一个函数，用于判断给定的路径 path 是否存在。这个函数会返回一个布尔值：
    如果路径对应的文件或目录存在，则返回 True；
    如果路径不存在（无论是文件还是目录），则返回 False。
"""
print(os.path.exists('/Users/chenhao'))
print(os.path.exists(''))
print(os.path.exists('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/2_contral_flow_tools'))
print(os.path.exists('/Users/chenhao/PycharmProjects/pythonProjectTest/3_Module_test/'))

"""
系统相关信息：
    获取操作系统类型：os.name 返回操作系统名，如 'posix' 表示类 Unix 系统，'nt' 表示 Windows 系统。
    获取环境变量：os.environ.get('VARIABLE_NAME') 获取环境变量值。

os.environ.get('VARIABLE_NAME') 是在Python中从操作系统环境变量中获取指定变量值的方法。这里的 'VARIABLE_NAME' 应替换为实际要查询的环境变量名。
这个函数的工作方式如下：
os.environ 是一个包含所有当前进程环境变量的字典对象。
.get('VARIABLE_NAME') 方法会尝试从该字典中获取与 'VARIABLE_NAME' 关联的值。
如果环境变量存在，则返回其对应的值；如果不存在，则返回 None（默认行为）。
"""
print(os.name)  # posix
print(os.environ.get('HOME'))  # /Users/chenhao

print(os.environ.get('1231'))

"""
进程管理：
    虽然不是 os 模块的核心功能，但可以通过其提供的接口与其他模块配合，实现一些简单的进程管理，
        例如执行外部命令可使用 os.system(command) 或者 subprocess 模块。
    其他实用方法：
    查找特定目录树下的文件：可以结合 os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) 方法遍历目录及其子目录。
    处理文件权限和所有权等高级文件系统操作，如 os.chmod() 修改文件权限。

进程的概念：
进程是计算机系统中程序的一次执行过程，它包含了程序的代码、数据、堆栈以及当前状态等信息。
每个进程都有一个独立的地址空间，并且能够并发地运行。
进程的状态：
就绪态：进程已准备好，但CPU尚未分配给它执行。
执行态：进程正在CPU上执行。
阻塞态（等待态）：进程由于等待某个事件（如I/O操作完成、信号量释放或其他资源可用）而暂时无法继续执行。
终止态：进程执行完毕或异常终止。
进程控制块 (PCB, Process Control Block)：
操作系统为每个进程维护了一个 PCB，其中存储了进程的相关信息，如进程ID、状态、优先级、CPU寄存器值、内存管理信息（如页表基址）、I/O信息等。
进程调度：
根据不同的调度算法（如先来先服务FCFS、短作业优先SJF、优先级调度、时间片轮转RR等），操作系统决定哪个就绪态进程获得CPU执行权。
进程同步与互斥：
为了协调多个进程对共享资源的访问，OS提供了同步机制（如信号量、管程、条件变量等）以确保正确有序的执行。
进程通信：
进程之间可以通过直接通信（如管道、消息队列、套接字等）或者间接通信（通过共享存储区）等方式进行信息交换。
进程创建与终止：
父进程可以创建子进程，子进程继承父进程的部分属性，并分配新的独立资源。
当进程执行完毕或遇到错误时，通过系统调用可以结束进程，并释放其占用的系统资源。
多线程模型：
在一个进程中可以有多个执行流，即线程，它们共享相同的地址空间和其他资源，但也拥有独立的执行上下文，从而实现更高的并发度。
"""
