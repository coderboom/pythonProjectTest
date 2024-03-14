import time
import sys

"""
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
def print(
    *args: object,
    sep: str | None = ...,
    end: str | None = ...,
    file: SupportsWrite[str] | None = ...,
    flush: Literal[False] = ...,
) -> None: ...


它将值打印到流或 sys.stdout（默认）。其中 objects 是一个序列对象，语法表示中可见它可以被解包，其他可选的关键字参数有：

file: 类似文件的对象（流）；默认为当前系统的 sys.stdout
sep: 在输出的值之间插入（分隔）字符串，默认为空格
end: 最后一个值后追加的字符串，默认为换行符
flush: 是否强制刷新

以上四个参数必须以关键字参数的形式给出，所有非关键字参数都会被转换为字符串，就像是执行了 str() 一样，并会被写入到流，以 sep 且在末尾加上 end。
 sep 和 end 都必须为字符串；它们也可以为 None，这意味着使用默认值。 如果没有给出 objects，则 print() 将只写入 end。
 file 参数必须是一个具有 write(string) 方法的对象；如果参数不存在或为 None，则将使用 sys.stdout。
由于要打印的参数会被转换为文本字符串，因此 print() 不能用于二进制模式的文件对象。 对于这些对象，应改用 file.write(...)。
输出是否缓存通常取决于 file，但如果 flush 关键字（在 3.3 版新增）参数为 True，输出流会被强制刷新。
"""
print("Hello World")

"""如同 C 语言，print() 使用标准输出。这不过是操作系统中的“文件”，程序的文本输出在操作系统中发送，因此可以显示给用户。
默认情况下，stdout 是缓冲的。也就是说，在收到特殊换行代码 \n 之前，它会存储接收到的数据而不显示数据。
Python 的 print 函数会自动增加换行符给发送给它的任何字符串。但有时这种行为是不可取的，你想在同一行上显示多个东西。
在下例中，将使用 print 函数的 end 参数以换行符以外的字符（或空字符串）结束字符串，这样您就不会打印除所要求的内容之外的任何内容。
以下代码在同一行上打印几个点，每 0.5s 打印一个点（注意：在终端中执行，不要在 Notebook）："""

for _ in range(5):
    print('.', end='')
    time.sleep(0.5)
print('___Gairuo!')
"""使用 flush 强制立即显示结果，即使没有新行"""

for i in range(5):
    print('.', end='', flush=True)
    time.sleep(0.5)

print('___Gairuo!')

print(print.__doc__)  # 查看print函数的文档
