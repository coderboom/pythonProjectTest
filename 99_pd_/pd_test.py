import pandas as pd

"""
Created on
"""
print('hello world')
# 1. 导入unittest
import unittest


# 2. 创建类继承unittest.TestCase
class TestDemo(unittest.TestCase):
    # 3. 创建测试用例方法, 方法要以test开头
    # 执行顺序是根据case序号来的, 并非代码的顺序
    def test_add_01(self):
        print(3 + 2)
        assert 3 + 2 == 5

    def test_add_02(self):
        print(5 + 5)
        assert 5 + 5 == 10


if __name__ == '__main__':
    unittest.main()
