'''
命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。

命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
我们举一个计算机系统中的例子，一个文件夹(目录)中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同文件夹中的文件可以重名。

一般有三种命名空间：
内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

命名空间查找顺序:
假设我们要使用变量 runoob，则 Python 的查找顺序为：局部的命名空间 -> 全局命名空间 -> 内置命名空间。
如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常:


作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python 的作用域一共有4种，分别是：

有四种作用域：
L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
规则顺序： L –> E –> G –> B。
在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。

'''
print('1111111111111')
'''
在Python中，模块（Module）和命名空间（Namespace）是两个密切相关的概念，它们共同构成了Python程序的组织结构和作用域规则。
模块（Module）：
模块是Python中封装代码的基本单元，通常对应一个.py文件。模块可以包含变量、函数、类以及其他导入的子模块。
每个模块都有自己的全局命名空间，该命名空间包含了模块内部定义的所有顶级变量、函数和类的名字以及它们的引用。
通过 import 语句，可以将其他模块引入到当前模块的作用域中，并且这些导入的模块会拥有独立的命名空间。
命名空间（Namespace）：
命名空间是一个存储变量名称及其所指向对象映射关系的地方，它确保了相同名称的变量在不同的作用域内不会相互冲突。
Python中的命名空间主要有三种类型：内置命名空间（Built-in Namespace）、全局命名空间和局部命名空间。
内置命名空间包含所有内建的函数和异常等；
全局命名空间对应于每个模块，即模块级别的全局变量和函数；
局部命名空间是在函数或方法内部定义的变量所处的作用域。
模块与命名空间的关系：
每个模块都拥有其自身的全局命名空间，在这个命名空间内定义的所有标识符（变量、函数、类等）仅在这个模块内部可见，除非被显式地导出或者导入到其他模块。
当从一个模块导入另一个模块时，实际上是创建了一个对导入模块命名空间的引用，而不是复制其内容。
因此，如果模块在运行过程中被修改并重新加载（使用 importlib.reload() 或者旧版的 reload() 函数），
那些已经导入了该模块的其他模块并不会自动获取更新后的命名空间内容，除非再次导入该模块。
'''