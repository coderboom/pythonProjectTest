from multiprocessing import Queue

"""multiprocessing 是一个支持生成进程的包，使用类似于 threading 模块的 API。
 multiprocessing 包提供本地和远程并发，通过使用子进程而不是线程来有效地回避全局解释器锁。
 因此，multiprocessing模块允许开发人员充分利用给定机器上的多个处理器。它可以在 Unix/Linux 和 Windows 上运行。

multiprocessing 模块还引入了在线程模块中没有的API。
一个典型的例子是 Pool 对象，它提供了一种方便的方法，可以跨多个输入值并行执行函数，跨进程分布输入数据（数据并行性）。
这是一个共享作业队列实现，它允许多个并发工作进程并行处理排队的项目。
基于进程的并行化在 CPython 中很流行，它可以避开全局解释器锁 (GIL) 阻止在单个解释器进程上进行的并行执行的问题。

multiprocessing.Queue作为一种特殊的队列实现，
用于在进程之间共享数据， 可以更轻松地跨多个进程分配工作，以解决 GIL 限制。这种类型的队列可以跨进程边界存储和传输可二进制序列化的对象。
"""
print('________________________特性与功能__________________________')
"""
multiprocessing.Queue 是 Python multiprocessing 模块提供的一个类，用于在多进程之间进行安全的数据交换。
它基于管道、锁定和序列化机制构建，确保了即使在不同进程中也能安全地传递消息。
multiprocessing.Queue 实现了先进先出（FIFO）原则，即最先放入队列的元素也将是最先被取出的元素。

下面是关于 multiprocessing.Queue 的详细说明：
特性与功能
    跨进程通信：multiprocessing.Queue 允许你在不同的 Python 进程间传递数据。
        它是线程和进程安全的，意味着在多线程或多进程环境下都能正确同步数据，避免了数据竞争和不一致的问题。
    自动序列化与反序列化：当你向队列中放入对象时，multiprocessing.Queue 会自动将对象序列化（使用 pickle 模块），
        而在另一端取出时会自动反序列化。这意味着你几乎可以放入任何可序列化的 Python 对象，但需要注意的是，某些对象如文件句柄不能被序列化。
    容量限制：可以通过构造函数的 maxsize 参数来设定队列的最大容量。当队列达到最大容量时，进一步的 put() 操作会阻塞，直到队列中有空间。
    
阻塞与非阻塞操作：
    put(item[, block=True[, timeout=None]])：将一个项目放入队列。如果队列已满并且 block 为 True，则会阻塞直到有空间可用；
        如果指定了 timeout 并且在超时时间内仍无空间，则抛出 Full 异常。
    put_nowait(item)：非阻塞版本的 put，如果队列满立即抛出 Full 异常。
    get([block=True[, timeout=None]])：从队列中取出一个项目。如果队列为空并且 block 为 True，则会阻塞直到有项目可用；
        如果指定了 timeout 并且在超时时间内仍无项目，则抛出 Empty 异常。
    get_nowait()：非阻塞版本的 get，如果队列空立即抛出 Empty 异常。
其他方法：
    qsize()：返回队列中的项目数量。注意，这个值可能不可靠，特别是在多线程或多进程中。
    empty()：如果队列为空，返回 True，否则返回 False。同样，此方法的结果可能不是绝对准确的。
    full()：如果队列已满，返回 True，否则返回 False。只有在设置了 maxsize 时才有意义。
"""
