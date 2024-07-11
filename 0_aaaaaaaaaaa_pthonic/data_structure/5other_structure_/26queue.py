import time
from queue import Queue

"""Queue(队列)  Queue（队列）是一种特殊的线性数据结构，遵循先进先出（FIFO, First In First Out）原则，
    即最先添加到队列中的元素也将是最先被移除的元素。

队列有两个主要操作：
    入队（Enqueue）：在队列的末端添加一个元素。
    出队（Dequeue）：从队列的前端移除一个元素。
    队列常用于需要处理一系列任务，且这些任务的执行顺序很重要，如打印任务队列、处理器调度等场景。
    
    在Python中，标准库提供了queue模块，它实现了线程安全的队列，主要有以下几种队列类型：
    queue.Queue：基本的FIFO队列。
    queue.LifoQueue：后进先出（LIFO）队列，也称为堆栈。
    queue.PriorityQueue：优先级队列，元素带有优先级，出队顺序由优先级决定，而不是按照入队顺序。
    使用队列可以简化并发编程和多线程间的通信，确保数据的同步访问，防止数据竞争和条件竞争问题。
    
    Queue 模块提供 FIFO 实现，适合多线程编程。
    它可用于在生产者和消费者线程之间安全地传递消息或其他数据。锁定机制为调用者使用同一个 Queue 实例在多个的线程中使用。
    队列的大小（元素数量）是可控的，以限制内存使用。
"""

simpleq = Queue()
simpleq.put('cat')
simpleq.put(123)
simpleq.put('doge')
print(simpleq)

print(simpleq.get())

import threading, queue


def worker(q):
    while True:
        item = q.get()
        print(f'working on {item}')
        print(f"finished {item}")
        q.task_done()


q = queue.Queue()
threading.Thread(target=worker, args=(q,), daemon=True).start()
for item in range(10):
    q.put(item)
q.join()
print(f"All work done.")

print('___________________通过线程池使用Queue________________________')
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


def worker(q, idx):
    print('Executing Job-------')
    data = q.get()
    time.sleep(3)
    print('Done', idx)
    return f"{data}"


q = Queue()
start_time = datetime.now()
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {
        executor.submit(worker, q, idx): idx for idx in range(12)
    }
    # 生产者制造数据
    for i in range(1, 13):
        q.put(i)

    # 归并结果
    for f in as_completed(futures):
        print('REsult:', f.result())

end_time = datetime.now()
elapsed = end_time - start_time
print(f"elansed{elapsed}")
