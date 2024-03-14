"""try"""
"""
try: 
    <逻辑代码>   # 正常运行的代码
except <错误类型1>:
    <逻辑代码>   #在try引发 <错误类型1> 时执行的代码
except <错误类型2>:
    <逻辑代码>   #在try引发 <错误类型2> 时执行的代码
.
.
.
except <错误类型n>:
    <逻辑代码>   #在try引发 <错误类型n> 时执行的代码
else: # else 是可选的
    <逻辑代码>   #如果没有异常发生时执行的代码
finally: # finally 是可选的
    <逻辑代码>   #无论如何都会执行的代码
"""
try:
    open('test.txt')
except IOError:
    print('文件读取错误')


def fn(x, y):
    try:
        return x / y
    except ZeroDivisionError as e1:
        print('除数不能为0')
    except TypeError as e2:
        print('参数类型错误', e2.args)
    else:
        print('正常运行')
    # finally:
    #     print('finally')


while True:
    # x, y = map(int, input('请输入两个整数：').split(','))
    x = int(input('请输入x的值：'))
    y = int(input('请输入y的值：'))
    print(fn(x, y))
