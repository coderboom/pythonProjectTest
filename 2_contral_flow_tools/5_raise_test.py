"""raise"""
"""
，raise 语句用于抛出一个异常。这允许程序员显式地触发异常处理机制，或者自定义异常情况。以下是 raise 的三种主要用法：
引发当前上下文中的异常： 如果在一个 except 块内使用不带参数的 raise，它会重新引发最近捕获到的异常。
"""
try:
    # 这里可能产生某种异常
    ...
except Exception as e:
    print("捕获到了异常:", e)
    raise  # 重新引发刚刚捕获的异常，不改变异常类型和信息

"""引发指定类型的异常： 可以通过提供一个异常类来创建并抛出该类型的异常，默认情况下没有附带消息。"""
raise ValueError  # 引发一个ValueError异常，不包含任何详细信息

# 或者带有自定义错误信息
raise ValueError("输入不是一个有效的数字")

"""引发已存在的异常对象： 如果你已经有一个异常对象（可能是之前捕获并存储的），可以使用 raise 来再次引发这个异常"""
try:
    # 产生一个异常
    ...
except Exception as original_exception:
    # 存储异常以便稍后再次引发
    saved_exception = original_exception

# 在其他地方或条件满足时，再次引发该异常
if some_condition:
    raise saved_exception
