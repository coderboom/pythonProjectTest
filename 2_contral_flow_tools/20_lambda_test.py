"""lambda"""

"""lambda表达式是一种简洁定义小型匿名函数的方法。它们常用于一次性操作或简单函数的场合，尤其在需要将函数作为参数传递给其他高阶函数（如 map(), filter(), sorted() 等）时非常有用
   
lambda arguments: expression
   arguments: 是一个逗号分隔的参数列表，可以没有参数、单个参数或多参数
   expression: 是一个单一的表达式，该表达式的结果将作为lambda函数的返回值。

"""


def add(x, y): return x + y


print(add(1, 2))

add_lambda = lambda x, y: x + y
print(add_lambda(1, 2))


def quadratic(a, b, c):
    # 这个函数接收系数 a、b 和 c，然后返回一个匿名函数（lambda 函数）。这个 lambda 函数接受一个变量 x，计算并返回对应的二次多项式的值。
    return lambda x: x ** 2 + b * x + c


f = quadratic(1, -1, 2)
print(f(5))
print(quadratic(1, -1, 2)(5))  # 直接调用匿名函数
"""
1、调用 quadratic 函数：
    quadratic(1, -1, 2)
   这一步将参数 a=1、b=-1 和 c=2 传递给 quadratic 函数。
   由于 quadratic 函数返回一个 lambda 函数（即 lambda x: x ** 2 + a * x + b），所以这一步的结果会得到一个表示二次多项式 ( x^2 + x - 1 ) 的函数对象。
2、对返回的 lambda 函数进行调用
    (5)
    在得到的 lambda 函数后面紧接着一对括号和数字 5，这意味着立即对该 lambda 函数进行调用，并将 5 作为参数 x 传入。因此，实际执行的操作是计算二次多项式 ( f(x) = x^2 + 1x - 1 ) 在 ( x=5 ) 时的值。
    
综上所述，quadratic(1, -1, 2)(5) 实际上是先通过 quadratic 函数创建了一个二次多项式的匿名函数，然后立刻使用 5 来求解该二次多项式的函数值
"""

print('------------------------')
"""filter()函数是Python内置的一个高阶函数，用于对序列（如列表、元组或字符串）进行过滤操作，返回一个迭代器，其中包含满足特定条件的元素
filter(function, iterable)  -->返回迭代器

function: 这是一个接收单个参数并返回布尔值的函数，它决定了哪些元素会被保留下来。这个函数通常被称为“筛选函数”或者“谓词”。
        作用于iterable的每个元素上，满足条件会被保留到返回的迭代器对象中。
iterable: 这是你想要过滤的可迭代对象，例如列表、元组、字符串或其他任何可迭代对象。
"""
numbers = [1, 2, 3, 4, 5]
# 使用lambda表达式配合filter函数筛选出所有偶数
even_numbers = filter(lambda x: x % 2 == 0, numbers)  # numbers中满足条件的元素被保留到返回的迭代器对象中
print(list(even_numbers))  # 输出：[2, 4]

"""map()函数是Python内置的高阶函数之一，用于对序列（如列表、元组等可迭代对象）中的每个元素应用指定的函数，并返回一个包含结果的新迭代器。

map(function, iterable1, iterable2, ...)   -->返回迭代器
function: 这是一个接受单个或多个参数并返回值的函数，它将被应用于每个可迭代对象的元素上。
iterable1, iterable2, ...: 一个或多个可迭代对象。如果提供了多个可迭代对象，则function会以这些对象的对应元素作为参数进行调用
"""
# 使用lambda表达式配合map函数对列表中的每个元素进行平方运算
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # 输出：[1, 4, 9, 16, 25]

list1 = [10, 20, 30]
list2 = [5, 15, 25]
sum_pairs = map(lambda x, y: x + y, list1, list2)  # ，lambda x, y: x + y 函数接收两个参数（来自不同列表的对应元素）
print(list(sum_pairs))  # 输出：[15, 35, 55]

"""sorted() 是 Python 内置的排序函数，用于对任何可迭代对象进行排序，并返回一个新的已排序的列表。
sorted(iterable, *, key=None, reverse=False)

iterable: 这是必需的参数，它接受一个可迭代对象（如列表、元组、字符串或自定义迭代器）。`sorted()` 函数将遍历这个对象的所有元素进行排序。
key: 这是一个可选参数，默认值为 `None`。如果提供了 `key` 参数，则应该是一个函数，该函数会被应用于 iterable 中的每个元素上。
    在排序过程中，实际比较的是经过 `key` 函数处理后的结果，而不是原始元素本身。
reverse: 这也是一个可选参数，默认值为 `False`，表示升序排序。如果设置为 `True`，则会按照降序排列元素。

注：它不会改变原有序列，而是返回一个新的已排序序列。
- 如果需要对原序列进行就地排序，可以使用列表对象的 `sort()` 方法。
"""
# 使用lambda表达式配合sorted函数对列表排序，按字符串长度排序
words = ['apple', 'banana', 'cat']
sorted_words_by_length = sorted(words, key=lambda word: len(word))
print(sorted_words_by_length)  # 输出：['cat', 'apple', 'banana']
"""
sorted() 函数接收一个可迭代对象（这里是 words 列表）作为第一个参数，并可以接受一个可选参数 key。key 参数用于指定一个函数，这个函数会被应用到列表中的每个元素上，返回值将被用作排序依据。
在这里，我们提供了 lambda 表达式作为 key 参数的值: lambda word: len(word)
这个匿名函数没有名称，它接受一个参数 word，并返回 word 的长度（即字符串中字符的数量）。在对 words 列表进行排序时，对于列表中的每一个字符串元素，都会调用此 lambda 函数计算其长度，然后根据长度值对整个列表进行排序。
输出排序后的结果： print(sorted_words_by_length)  # 输出：['cat', 'apple', 'banana']

经过 sorted() 函数处理后，新列表 sorted_words_by_length 中的元素按照字符串长度从小到大进行了排序。因此，输出结果是 ['cat', 'apple', 'banana']，这是因为字符串 'cat' 长度最短（为 3），其次是 'apple'（长度为 5），最后是 'banana'（长度为 6）。

重点：在使用 sorted(words, key=lambda word: len(word)) 这种方式时，Python 的 sorted() 函数会一边计算元素的长度（通过调用 lambda 函数），一边进行排序。
具体过程如下：
对于列表中的每个元素 word，sorted() 函数都会调用 lambda word: len(word) 来计算该元素的长度。
根据计算出的长度值，sorted() 函数构建一个临时排序依据的序列，并根据这些长度值对原始列表进行排序。
整个排序过程中，对于不同元素的长度计算是逐步进行的，而非一次性计算所有元素的长度后才开始排序。
因此，可以理解为“一边求长度一边排序”的机制。

"""
