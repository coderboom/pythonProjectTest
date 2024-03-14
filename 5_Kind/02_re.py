"""正则表达式是一组由字母和符号组成的特殊文本，它可以用来从文本中找出满足你想要的格式的句子"""
"""
一个正则表达式是一种从左到右匹配主体字符串的模式。 “Regular expression”这个词比较拗口，我们常使用缩写的术语“regex”或“regexp”。 
    正则表达式可以从一个基础字符串中根据一定的匹配模式替换文本中的字符串、验证表单、提取字符串等等。

正则表达式的元字符是具有特殊含义的字符，它们不是用于匹配自身字面意义，而是用来指示某种模式、位置或重复次数。
    以下是一些常见的正则表达式元字符及其含义：
    \d：匹配一个数字（等同于 [0-9]）。
    \D：匹配任何非数字字符（等同于 [^0-9]）。
    \w：匹配字母、数字或下划线（等同于 [a-zA-Z0-9_]）。
    \W：匹配任何非字母数字和下划线的字符（等同于 [^a-zA-Z0-9_]）。
    \s：匹配任意空白字符（包括空格、制表符、换行符等）。
    \S：匹配任何非空白字符。
    .：匹配除换行符外的任意单个字符。
    ^：当出现在字符串开始时，表示匹配字符串的开头；在字符类中，表示取反（如 [^abc] 匹配除了 a、b 和 c 之外的字符）。
    $：匹配字符串的结尾。
    \b：匹配单词边界，即单词与空格或其他非单词字符之间的位置。
    \A: 匹配字符串绝对开始位置（类似于 Python 中的 re.match() 而不是 re.search()）。
    \Z: 匹配字符串绝对结束位置或者可能存在的换行符之前的结束位置。
    *：前面的元素可以重复零次或多次。
    +：前面的元素至少重复一次(连续多个)。
    ?：前面的元素可选，出现零次或一次。
    {m,n}：前面的元素可以重复 m 到 n 次。
    []：字符集，匹配括号内任何一个字符，如 [abc] 匹配 'a'、'b' 或 'c'。
    [^]: 字符集，不匹配字符集中的任何一个字符，如 [^abc] 匹配除了 a、b 和 c 之外的字符。
    -：在字符集中用于定义范围，如 [a-z] 表示所有小写字母。
    |：管道符号，表示“或”，如 cat|dog 匹配 'cat' 或 'dog'。
注意，在使用这些元字符时，如果要匹配它们自身的字面意思，通常需要在它们前面加上反斜杠进行转义，例如 \. 表示匹配点字符本身。

分组与引用：
   () 用于分组，可以捕获匹配的内容，并且可以通过\数字反向引用。
   (?:...) 非捕获组，不保存匹配内容。
re模块函数：
   re.match(pattern, string, flags=0)：从字符串开始位置尝试匹配。 
   re.search(pattern, string)：在整个字符串中搜索第一个匹配项。
   re.findall(pattern, string)：返回所有非重叠匹配项组成的列表。
   re.sub(pattern, repl, string[, count])：将字符串中所有匹配到的子串替换为另一个字符串。
   re.compile(pattern)：编译正则表达式，提高后续多次使用的效率。
   
group() :
group() 是正则表达式 re 模块中的方法，它是在成功执行匹配操作后，用来获取匹配对象中捕获组内容的方法。
   当你使用 re.compile() 编译了一个正则表达式，并通过诸如 .match() 或 .search() 方法找到了一个匹配项时，返回的对象是一个 Match 对象。
这个 Match 对象具有多个 group() 方法：
group() 或者等价地 group(0)：返回整个匹配到的字符串。

group(n)，其中 n 是非负整数：返回第 n 个括号（捕获组）内匹配的内容。例如，如果你的正则表达式中有 (.*?) 这样的捕获组结构，则 group(1) 将返回第一个括号内的匹配部分。
groups()：返回一个包含所有捕获组匹配内容的元组，顺序与它们在正则表达式中出现的顺序一致。
"""
import re

print('--------------------- re.search-------------------')
"""   re.search(pattern, string, flags=0)
   
re.search() 在整个字符串中搜索第一个与 pattern 匹配的内容，只要在 string 中找到 pattern 至少有一次出现，就会返回一个 match 对象。
    即使匹配内容不在字符串的起始位置，也能成功匹配。
    
区别于 re.match()：
    re.match() 只匹配字符串的开始位置，如果模式没有在字符串的开头匹配，则返回 None。
    re.search() 则会在整个字符串中搜索直到找到第一个匹配项为止。
"""
# \d - 匹配一个数字：
text = "The number is 123."
pattern = r"\d+"
match = re.search(pattern, text)
print(match.group())  # 输出：'123'

# . - 匹配除换行符外的任意单个字符：
text = "abc123def"
pattern = r"a.b.c"
match = re.search(pattern, text)
print(match)  # 输出：'abc123'

print('--------------------- re.findall-------------------')
"""   re.findall(pattern, string, flags=0)
   
re.findall() 会在给定的 string 中搜索与 pattern 匹配的所有子串，并返回包含所有匹配结果（非重叠）的列表。每个匹配结果都是一个单独的字符串。

注意：
    返回的列表中的每个元素都是正则表达式中括号内捕获组的内容，如果没有定义捕获组，则整个匹配内容将被返回。如果没有找到任何匹配项，re.findall() 将返回一个空列表
"""
# \w - 匹配字母、数字或下划线：
text = "username_123"
pattern = r"\w+"
match = re.findall(pattern, text)
print(match)  # 输出：['username', '123']

print('--------------------- re.match-------------------')

"""   re.match(pattern, string, flags=0)

pattern: 这是一个字符串形式的正则表达式模式，表示要查找的匹配规则。
    string: 这是要搜索的原始字符串。
    flags（可选）: 用于指定匹配模式的标志，如忽略大小写（re.IGNORECASE）、多行模式（re.MULTILINE）等。
    
功能： re.match() 只会匹配字符串的开始位置，如果 pattern 在 string 的起始位置就能找到匹配，则返回一个 match 对象；否则返回 None。
"""
# ^ - 匹配字符串开头：
text = "This is a test."
pattern = r"^This"
match = re.match(pattern, text)
if match:
    print("Match found at the beginning of the string.")
print(match)

# 匹配以 "Hello" 开头的字符串
match_obj = re.match(r'Hello', 'Hello, world!')
if match_obj:
    print("Match found:", match_obj.group(0))  # 输出: Match found: Hello
else:
    print("No match")

# 匹配失败的例子
match_obj = re.match(r'Hello', 'world, Hello!')
if match_obj:
    print("Match found")
else:
    print("No match")  # 输出: No match

print('--------------------- re.sub-------------------')
"""   re.sub(pattern, repl, string, count=0, flags=0)

pattern: 这是一个正则表达式模式，用于定义要查找和替换的内容。
repl: 这是可以是字符串、函数或者方法的替换内容。如果 repl 是字符串，则可以包含反向引用 \number 或 \g<name> 来引用捕获组。
    如果 repl 是函数，该函数将在每次匹配时被调用，并传入匹配对象作为参数，返回值将作为替换内容。
string: 需要在其中执行替换操作的原始字符串。
count（可选）: 表示最多替换次数，默认为 0，表示无限制，即替换所有匹配项。
flags（可选）: 正则表达式的匹配标志，例如 re.IGNORECASE 等。
"""

# 将字符串中的所有数字替换为 "NUMBER"
text = "The numbers are: 123, 456 and 789."
replaced_text = re.sub(r'\d+', 'NUMBER', text)
print(replaced_text)  # 输出: The numbers are: NUMBER, NUMBER and NUMBER.


# 使用函数作为替换内容，将大写字母转换为小写
def to_lowercase(match):
    return match.group(0).lower()


text = "Hello World! This Is A Test Sentence."
replaced_text = re.sub(r'[A-Z]', to_lowercase, text)
print(replaced_text)  # 输出: hello world! this is a test sentence.

print('--------------------- re.compile----------------------')
"""   re.compile(pattern, flags=0)
   
pattern: 这是一个字符串形式的正则表达式模式。
flags（可选）: 正则表达式的匹配标志，可以是单个标志或多个标志的组合。例如，re.IGNORECASE 用于忽略大小写，re.MULTILINE 使 ^ 和 $ 能够匹配每一行的开始和结束等。
功能：
编译正则表达式：将给定的正则表达式模式编译成一个预编译的正则表达式对象。
提高性能：对于需要多次使用的正则表达式，预先编译可以提高执行效率，因为Python不需要在每次调用时都解析和编译这个正则表达式。
"""

# 编译一个正则表达式
pattern = re.compile(r'\d+')

# 使用编译后的正则表达式进行匹配
text = "The numbers are: 123, 456 and 789."
matches = pattern.findall(text)
print(matches)  # 输出: ['123', '456', '789']

# 同样可以使用方法match、search、sub等
replaced_text = pattern.sub('NUMBER', text)
print(replaced_text)  # 输出: The numbers are: NUMBER, NUMBER and NUMBER.

"""返回一个 Pattern 对象，该对象提供了如 match(), search(), findall(), finditer(), sub(), split() 等多种方法，可以在后续操作中复用此预编译的正则表达式。"""

print('--------------------- re.split----------------------')
"""   re.split(pattern, string[, maxsplit=0, flags=0])
   
参数说明：
    pattern: 这是一个正则表达式模式，用于定义在何处进行字符串分割。
    string: 需要进行分割的原始字符串。
    maxsplit（可选）: 指定最大分割次数，默认值为 0，表示无限制，即尽可能多地进行分割。
    flags（可选）: 正则表达式的匹配标志，例如忽略大小写、多行模式等。
功能： re.split() 根据提供的正则表达式模式在字符串中查找匹配项，并在每个匹配的位置将字符串分割成多个子串。
    与常规的字符串 .split() 方法不同的是，它可以处理更复杂的分割规则，比如基于特殊字符序列或模式来分割字符串。
"""
# 使用逗号和空格作为分隔符分割字符串
textq = "The numbers are: 123, 456 and 789."
parts = re.split(r'[,\s]+', textq)
print(parts)  # 输出: ['The', 'numbers', 'are:', '123', '456', '789.']

# 分割但只执行一次
text = "a_b_c"
parts = re.split(r'_', text, maxsplit=1)
print(parts)  # 输出: ['a', 'b_c']

re_split = re.compile(r'[,\s]+')
parts1 = re_split.split(textq)
print(parts1)

print('----------------------------------------------')

# $ - 匹配字符串结尾：
text = "End of line."
pattern = r".*line.$"
match = re.search(pattern, text)
if match:
    print("Match found at the end of the string.")
print(match.group())

# \b - 匹配单词边界：
text = "I love regex and regexes."
pattern = r"\bregex\b"
matches = re.findall(pattern, text)
print(matches)  # 输出：['regex']

# * - 前面的元素可以重复零次或多次：
text = "haha"
pattern = r"h*a"
match = re.search(pattern, text)
print(match.group())  # 输出：'ha'
print(match)

# + - 前面的元素至少重复一次：
text = "12345"
pattern = r"\d+"
match = re.match(pattern, text)
print(match.group())  # 输出：'12345'

# ? - 前面的元素可选，出现零次或一次：
text = "colorful or color"
pattern = r"colou?rful"
match = re.search(pattern, text)
print(match)
print(match.group())  # 输出：'colorful'

# {m,n} - 前面的元素可以重复 m 到 n 次：
text = "apple, apples, applepie"
pattern = r"apples{1,2}"
match = re.search(pattern, text)
print(match.group())  # 输出：'apples'

# [ ] - 字符集，匹配括号内的任何一个字符：
text = "red, green, blue"
pattern = r"[rgb]reen"
match = re.search(pattern, text)
print(match.group())  # 输出：'green'

# - 在字符集中表示范围：
text = "a-z, A-Z, 0-9"
pattern = r"[a-zA-Z0-9]"
for char in text:
    if re.match(pattern, char):
        print(char, end=' ')
    # 输出：'a z , A Z , 0 - '
    # | - 管道符号，表示“或”：
    text = "cat dog parrot"
pattern = r"cat|dog"
matches = re.findall(pattern, text)
print(matches)  # 输出：['cat', 'dog']
print('----------------------')
"""
正则表达式中的括号 ( ) 用于创建捕获组（Capturing Group），它可以捕获匹配到的内容，
    并且可以在表达式内部或外部通过反向引用\数字来再次引用这个分组匹配到的值。
下面分别给出捕获组和非捕获组的例子：
"""

# 正则表达式包含一个捕获组
pattern = r'(\w+)\s+(\1)'
text = 'apple apple'
# """
# 正则表达式 r'(\w+)\s+(\1)'：
# \w+ 匹配一个或多个字母、数字或下划线（等同于 [a-zA-Z0-9_]），并将其作为一个捕获组，即第一个分组。
# \s+ 匹配一个或多个空白字符（包括空格、制表符等）。
# (\1) 是反向引用，它表示要匹配与第一个捕获组（\w+）相同的内容。
# 因此，整个模式会尝试查找这样的字符串：先是一个由字母数字组成的单词，后面跟着至少一个空格，然后是与前面相同的单词。
# """
# 使用re.match或re.search查找匹配项
match = re.search(pattern, text)
print(match)
if match:
    # 获取捕获组内容
    print(match.group(1))  # 输出：'apple'
    print(match.group(2))  # 输出：'apple'
    # 反向引用，这里\1代表第一个捕获组的内容
    print(match.group())  # 输出：'apple apple'

# 在此例子中，\w+\s+\1表示匹配两个相同的单词，它们之间由空格隔开。


# 正则表达式包含一个非捕获组
pattern = r'(?:\d{3})-(\d{2})-(\d{4})'
text = '123-45-6789'

# 使用re.match或re.search查找匹配项
match = re.search(pattern, text)

if match:
    # 非捕获组不会被捕获，所以不能直接通过group编号获取其内容
    # 它们只为了在正则表达式内部结构化逻辑，但不影响结果的保存
    print(match.group(1))  # 输出：'45'
    print(match.group(2))  # 输出：'6789'

# 在此例子中，(?:\d{3})是一个非捕获组，它匹配三位数字，但是不会存储这部分匹配的内容，
# 而后面的(\d{2})和(\d{4})则是捕获组，用来捕获区号和四位数的年份部分。
print('-----=------------------------pattern对象----=-------------------')
""" re.compile(pattern,flags=0)：编译正则表达式，提高后续多次使用的效率。

 **参数说明：**
  - `pattern`（必需）：字符串类型，表示要编译的正则表达式模式。例如 `'^\d{3}-\d{2}-\d{4}$'` 可以用来匹配美国社保号格式。

  - `flags`（可选）：整数类型，默认值为0，表示匹配标志位。它可以是以下标志的组合（通过按位或 `|` 连接），来修改正则表达式的匹配行为：
    - `re.IGNORECASE` 或 `re.I`：忽略大小写。
    - `re.MULTILINE` 或 `re.M`：多行模式，使 `^` 和 `$` 分别匹配每一行的开始和结束（而不仅仅是整个字符串的开头和结尾）。
    - `re.DOTALL` 或 `re.S`：点（`.`）字符匹配包括换行符在内的所有字符。
    - 其他标志如 `re.VERBOSE` 或 `re.X` 用于编写更易读的正则表达式，允许在表达式中加入注释和空白。

- **返回值：**
  返回一个 `Pattern` 对象，该对象拥有如下方法（部分常用方法）：
    - `pattern.match(string)`：从字符串开始位置尝试匹配。
    - `pattern.search(string)`：在字符串中查找首次出现的匹配项。
    - `pattern.findall(string)`：在字符串中找到所有非重叠的匹配项，并以列表形式返回。
    - `pattern.finditer(string)`：返回一个迭代器，每次迭代返回一个包含匹配信息的 `MatchObject` 对象。
    - `pattern.sub(repl, string[, count])`：将字符串中所有匹配到的部分替换为另一个字符串或函数返回值。
"""
pattern = r'(?:\d{3})-(\d{2})-(\d{4})'
text = '123-45-6789'
obj_pattern = re.compile(pattern, flags=re.IGNORECASE)
match_result = obj_pattern.match(text)
if match_result:
    print(match_result)
    print(match_result.group())
    print(match_result.group(1))
    print(match_result.groups())

print(obj_pattern.groupindex)  # 输出：{} ,映射类型
print()

print('-----=------------------------match对象----=-------------------')
"""match 对象是当你使用 re.match() 或 re.search() 等函数成功匹配到一个模式时返回的对象。这个对象包含了关于匹配结果的所有信息。

match对象的主要方法和属性包括：
.group([group1, ...]): 返回被整个匹配或指定捕获组捕获的字符串。如果没有提供参数，默认返回整个匹配的文本。

.start([group]) 和 .end([group]): 分别返回匹配文本的起始和结束索引（基于字符串的原索引）。如果提供了捕获组编号，则返回该捕获组匹配部分的索引范围。

.span([group]): 返回一个包含 (start, end) 的元组，表示整个匹配或指定捕获组匹配文本的开始和结束索引。

.groups(): 返回一个元组，其中包含所有被捕获组捕获的文本。如果没有分组或者没有捕获任何内容，则返回空元组。

可以将 match 对象直接用于布尔上下文中，其作为 True 表示有匹配发生，False 则表示没有匹配：
"""
# group([group1, ...])
m = re.match(r'(\w+) (\w+)', 'Hello World')
print(m.group(0))  # 输出: Hello World
print(m.group(1))  # 输出: Hello
print(m.group(2))  # 输出: World

# start([group]) 和 .end([group])
m = re.match(r'(\w+) (\w+)', 'Hello World')
print(m.start())  # 输出: 0
print(m.end())  # 输出: 11
print(m.start(1))  # 输出: 0
print(m.end(1))  # 输出: 5

# span([group])
m = re.match(r'(\w+) (\w+)', 'Hello World')
print(m.span())  # 输出: (0, 11)
print(m.span(1))  # 输出: (0, 5)

# groups()
m = re.match(r'(\w+) (\w+)', 'Hello World')
print(m.groups())  # 输出: ('Hello', 'World')

# 将 match 对象直接用于布尔上下文中
m = re.match(r'\d+', 'abc123def')
if m:
    print('Match found:', m.group())
else:
    print('No match')
