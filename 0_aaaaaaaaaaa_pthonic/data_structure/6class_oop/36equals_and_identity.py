"""Python类的约定 is 与 =="""

print('----------------')
"""Python的is代表着对象在内存的应用的比较，==代表着实现了__eq__魔术方法的值的比较。

Python对代码有优化的情况，对于整数，在-5~256区间的初始值，Python会默认划分一个缓存区来存贮，只要赋值这个区间的值，
    不会再重新在堆内存中再划分一个新区来存贮，而是用缓存的，这样就会大大提高效率。对于字符串，在<4097个字符的情况也一样。
    
另外，Python的解析器会有很多内部的优化机制，在编译代码为Bytecode的期间会预先扫描源代码，把可以优化的复制片段进行优化，这是值得称道的地方。
"""

a = [1, 2, 3]
b = a
c = a

print(b == a, c == a, b == c)  # True True True
print(b is a, c is a, b is c)  # True True True
print(id(a), id(b), id(c))  # 4351861504 4351861504 4351861504

a = [1, 2, 3]  # 重新赋值之后，a指向类新地址
print(b == a, c == a, b == c)  # True True True
print(b is a, c is a, b is c)  # False False True
print(id(a), id(b), id(c))  # 4839330688 4343472896 4343472896
print('----------------------')
"""Python对代码有优化的情况，对于整数，在-5~256区间的初始值，Python会默认划分一个缓存区来存贮，只要赋值这个区间的值，
    不会再重新在堆内存中再划分一个新区来存贮，而是用缓存的，这样就会大大提高效率。对于字符串，在<4097个字符的情况也一样。
"""
aa = -1
bb = aa
cc = bb
aa = -1
print(cc is bb, bb is aa, cc is aa)  # True True True
