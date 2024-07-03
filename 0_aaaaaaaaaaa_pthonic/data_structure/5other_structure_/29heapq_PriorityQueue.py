import heapq
import queue

"""
PriorityQueue 是一种特殊类型的队列，其中的元素根据优先级排序，而不是按照它们进入队列的顺序。
在 Python 中，标准库并没有直接提供名为 PriorityQueue 的类，
    但你可以使用 heapq 模块或者 queue.PriorityQueue（针对线程安全的需求）来实现优先队列的功能。

heapq 模块提供了堆队列算法的实现，最小值堆默认优先级最高（即最小的元素会被最先弹出）
    堆是二叉树，每个父节点的值都小于或等于其任何子节点。
    此实现对所有 k 使用 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2] 的数组，从零开始计算元素。
    为了比较，不存在的元素被认为是无限的。堆（实际上是 minheap）的一个有趣属性是它的最小元素始终是根，heap[0]。
"""
items = []
heapq.heappush(items, (5, 'tiger'))
heapq.heappush(items, (2, 'doge'))
heapq.heappush(items, (1, 'cat'))

print(items)
while items:
    next_things = heapq.heappop(items)
    print(next_things)

print('___________________通过线程池使用PriorityQueue________________________')
import threading


def worker(q):
    while True:
        item = q.get()
        print(f'working on {item}')
        print(f"finished {item}")
        q.task_done()


q = queue.PriorityQueue()
threading.Thread(target=worker, args=(q,), daemon=True).start()
for item in range(10):
    q.put(10 - item)
q.join()
print(f"All work done.")

print('___________________通过线程池使用PriorityQueue________________________')
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED
import random, time
from queue import PriorityQueue


def worker(imput_queue: PriorityQueue, output_queue: PriorityQueue, idx):
    print('Executing Job-------')
    data = imput_queue.get()
    time.sleep(3)
    print('Done', idx)
    output_queue.put(data)


input_queue = PriorityQueue()
output_queue = PriorityQueue()
start_time = datetime.now()
with ThreadPoolExecutor(max_workers=12) as executor:
    futures = {
        executor.submit(worker, input_queue, output_queue, idx): idx for idx in range(12)
    }
    # 生产者制造数据
    raw_data = list(range(1, 13))
    random.shuffle(raw_data)
    print('origrn data:', raw_data)
    for i in raw_data:
        input_queue.put(i * i)

    # 归并结果
    wait(futures, return_when=ALL_COMPLETED)
    result = [output_queue.get() for _ in range(len(raw_data))]
    print('RESULT: ', result)

end_time = datetime.now()
elapsed = end_time - start_time
print(f"elansed{elapsed}")

"""
优先级高的工作先做，保证了按照编排的规划去走。
"""
