import time


def func(n):
    for i in range(0, n):
        # yield相当于return，下一次循环从yield的下一行开始
        arg = yield i  # 执行到yield i 时停止，不执行arg = yield i这个赋值操作，下一次调用先执行这个赋值操作，再执行下一行代码
        print('func', arg)


if __name__ == '__main__':
    f = func(6)
    while True:
        print('main-next:', next(f))
        time.sleep(2)
        print('main-send:', f.send(100))  # send()函数传递的参数，先是作为yield表达式的值，再传递参数给arg。
        time.sleep(10)
