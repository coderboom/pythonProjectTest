"""
与 Queue 的标准 FIFO 实现相比，LifoQueue 使用后进先出的顺序（通常与堆栈数据结构相关联）。它提供锁定语义来支持多个并发的生产者和消费者。
"""
from queue import LifoQueue

"""
LifoQueue 是 Python 中 queue 模块的一部分，它实现了一个后进先出（LIFO）的数据结构，类似于日常生活中的堆栈。
    在 LIFO 队列中，最后一个插入的元素（顶元素）将首先被删除，这与传统的先进先出（FIFO）队列如 Queue 相反。
    LifoQueue 在多线程编程中特别有用，因为它提供了线程安全的方法来处理数据，确保在并发环境中正确地执行操作。
    
以下是 LifoQueue 的主要特点和方法：
初始化：
    queue.LifoQueue([maxsize])：创建一个 LIFO 队列。可选参数 maxsize 限制了队列的大小，如果设置为 None 或不设置，则队列大小无限制。

主要方法：
    qsize()：返回队列中的元素数量。
    empty()：如果队列为空，返回 True，否则返回 False。
    full()：如果队列已满（如果设置了 maxsize），返回 True，否则返回 False。
    put(item, block=True, timeout=None)：将 item 插入到队列的尾部。如果队列已满且 block 为 True，则会阻塞直到有足够的空间。
        如果提供了 timeout 参数，它会等待指定的秒数，然后抛出 Full 异常。
    put_nowait(item)：非阻塞版本的 put，如果队列已满则抛出 Full 异常。
    get(block=True, timeout=None)：从队列头部取出并返回一个元素。如果队列为空且 block 为 True，则会阻塞直到有元素可用。
        如果提供了 timeout 参数，它会等待指定的秒数，然后抛出 Empty 异常。
    get_nowait()：非阻塞版本的 get，如果队列为空则抛出 Empty 异常。
    
线程安全：
    LifoQueue 内部实现了锁机制，保证了在多线程环境下的线程安全。这意味着不同线程可以同时读写队列而不会导致数据混乱。
    
实例：
"""
q = LifoQueue()
q.put('11')
q.put('22')
print(q.qsize())
print(q.get())  # 22 后进先出

"""总结来说，LifoQueue 是一种高效且线程安全的实现 LIFO 原则的数据结构，适用于需要快速访问最近添加数据的场景，比如回退操作或函数调用栈。
"""
