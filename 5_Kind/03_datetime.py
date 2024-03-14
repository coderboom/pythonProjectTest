"""时间对象类型"""
from datetime import date, datetime, timedelta
from datetime import time as Ti

"""datetime 是Python标准库中一个强大的模块，用于处理日期和时间。它提供了多个类来表示日期、时间、日期时间以及它们之间的间隔，并支持时区操作

主要属性：
year, month, day: 分别获取年份、月份和日期。
hour, minute, second, microsecond: 分别获取小时、分钟、秒和微秒。
tzinfo: 如果已知时区信息，则返回时区对象。
方法：
strftime(format): 将日期时间转换为格式化的字符串。
strptime(datetime_str,format)： 根据format解析出datetime_str中的时间，返回一个datetime对象。

timestamp(): 返回自 Unix 纪元（1970年1月1日0点）以来的秒数（浮点数）。
date(): 返回只包含日期部分的 datetime.date 对象。
time(): 返回只包含时间部分的 datetime.time 对象。

datetime.date 类
只包含年、月、日信息的类，不涉及时间部分。
创建方法：datetime.date(year, month, day)。

datetime.time 类
表示一天中的时间点，不包括日期信息，由小时、分钟、秒和微秒组成。
创建方法：datetime.time(hour, minute, second, microsecond)。

datetime.timedelta 类
表示两个日期或时间之间的时间差，通常用来表示一段时间间隔。
创建方法：datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)。

时区支持
datetime 模块提供对时区的支持，但不是直接在 datetime.datetime 类内部实现的。
    从 Python 3.2 开始引入了 pytz 库或者内置的 zoneinfo 模块（Python 3.9+）来处理时区相关操作。
使用时区时，通常会与 datetime 类配合使用，例如将本地时间转换为UTC时间，或者反之。
"""
print(date(year=2020, month=12, day=1), type(date(year=2020, month=12, day=1)))  # 2020-12-01 <class 'datetime.date'>
print(date.today(), type(date.today()))
print(date.fromtimestamp(1319932312), type(date.fromtimestamp(1319932312)))
print(date.fromordinal(2022), type(date.fromordinal(2022)))  # 0006-07-15 <class 'datetime.date'>

# 根据标准字符串返回日期类型
print(date.fromisoformat('2022-01-01'))
# 逆操作，将日期对象转换为符合ISO 8601标准的字符串格式。输出：2020-01-01 <class 'str'>
print(date.isoformat(date(2020, 1, 1)), type(date.isoformat(date(2020, 1, 1))))

# 指定年第几周的第几天是哪天。
print(date.fromisocalendar(2020, 1, 1), type(date.fromisocalendar(2020, 1, 1)))  # 2020-01-01 <class 'datetime.date'>
# 上述方法的逆操作
print(date.isocalendar(date(2020, 3, 1)))  # datetime.IsoCalendarDate(year=2020, week=9, weekday=7)

d = date(2024, 3, 10)
print(d.year, d.month, d.day)
print(d.ctime())  # 将时间转换为字符串格式 <class 'str'>
# isoweekday() :返回星期几，星期一为1，星期天为7
# weekday(): 返回星期几，星期一为0，星期天为6
# isocalendar(): 日历元组，返回元组(year, week, weekday（星期一为1，星期天为7）)
print(d.weekday(), d.isoweekday(), d.isocalendar())  # 6 7 datetime.IsoCalendarDate(year=2024, week=10, weekday=7)
d.replace(month=10)  # 替换年月日，不是原地操作
print(d, '\n', d.replace(month=10))
print(d.strftime('%Y年-%m月-%d日'), '\n', d.strftime('%Y'))

# 返回一个time.struct_time 对象，包含日期时间信息。
print(d.timetuple())
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=70, tm_isdst=-1)

print(d.toordinal())  # 各列高利历序号  ：  738321

print('-----------------------------')

"""  time 时间对象
一个time对象代表某日的本地时间，独立于任何特定日期，可通过tzinfo对象来调整可感知的时间类型
"""
from datetime import time, timezone

# 标准格式化字符串转时间类型
print(time.fromisoformat('14:15:06'), '\n', type(time.fromisoformat('14:15:06')))  # 14:15:06  <class 'datetime.time'>

# fold: 0表示正向调整，1表示反向调整; 0:早于此时间，用于在重复的时间段中清除边界时间歧义
t = time(hour=23, minute=9, second=34, microsecond=123456, tzinfo=timezone.utc, fold=0)
print(t, type(t))
print(t.hour, t.minute, t.second, t.microsecond, t.tzinfo, t.fold)  # 23 9 34 123456 UTC 0

print(t.replace(hour=20))  # 20:09:34.123456+00:00
print(t.isoformat())
print(t.isoformat(timespec='hours'))  # 23+00:00
print(t.isoformat(timespec='minutes'))  # 23:09+00:00
print(t.isoformat(timespec='seconds'))  # 23:09:34+00:00

"""在Python中，datetime 对象有一个 isoformat() 方法，用于将日期和时间转换为ISO 8601格式的--字符串--。当调用 isoformat() 方法时，你可以指定一个可选参数 timespec 来控制输出的时间精度。
在这个例子中：
t.isoformat(timespec='hours') 表示将 t 这个 datetime 对象以小时为最小单位进行格式化输出。结果字符串 "23+00:00" 意味着时间是UTC时区的23点整，不包含分钟和秒的信息。
t.isoformat(timespec='minutes') 表示将 t 这个 datetime 对象以分钟为最小单位进行格式化输出。结果字符串 "23:09+00:00" 意味着时间是UTC时区的23点9分，不包含秒的信息。

这里的 "+00:00" 是指零时区偏移量，即 UTC 时间。如果该 datetime 对象不是 UTC 时区，那么这里会显示相应的时区偏移量。例如，如果是美国东部标准时间（EST），可能会显示类似 "-05:00" 的时区偏移量。
"""
print(t.strftime('%H:%M:%S'), t.__format__('%H:%M:%S'))

# 返回与UTC时区的时区偏移量
print(t.utcoffset())  # 0:00:00
# 返回时区名称
print(t.tzname())  # UTC
# 夏令营时(DST): 无
print(t.dst())

print('------------time--------------')
import time

"""
datetime.fromtimestamp() 是一个函数，用于从 Unix 时间戳（以秒为单位）创建一个 datetime 对象
time.time() 函数是 Python 内置 time 模块提供的方法，它返回当前时间的时间戳，即自1970年1月1日以来经过的秒数（包括小数部分，精确到毫秒或微秒，取决于操作系统和Python版本）
"""
print(datetime.fromtimestamp(time.time()))  # 2024-03-10 15:50:11.974883
print(datetime.utcfromtimestamp(time.time()))  # 用(UTC时间)构建一个datetime对象

print(datetime.utcnow())  # 返回UTC时间的datetime对象
# 建议创建感知型当前时间
print('----', datetime.now(timezone.utc))

# 通过时间戳返回datetime对象
print(datetime.fromtimestamp(123123123))  # 本地时区
print(datetime.fromtimestamp(123123123, timezone.utc))  # UTC时区
print(datetime.utcfromtimestamp(123123123))  # UTC时区

# 日期和时间合并成一个datetime对象
dt_now = datetime.combine(date(2020, 1, 1), Ti(23, 59, 59), tzinfo=timezone.utc)  # 2020-01-01 23:59:59+00:00
dt_now1 = datetime.combine(date(2020, 1, 1), Ti(23, 59, 59))  # 2020-01-01 23:59:59+00:00
print(dt_now)
print(dt_now1)

# 从标准字符串创建一个datetime对象
print(datetime.fromisoformat('1973-11-26 00:52:03'))  # 不带时区
print(datetime.fromisoformat('2020-01-01T04:52:03+04:00'))  # 带时区
print(type(datetime.fromisoformat('2020-01-01T04:52:03+04:00')))

# 用于格式化日期时间对象为字符串。这个方法将日期和时间按照指定的格式输出为字符串
print(datetime.utcnow().strftime("%Y年-%m月-%d日 %H时:%M分:%S秒"))

# 已知格式，从字符串中解析（提取）出时间，---关键点是占位符---  ———— strptime
print(datetime.strptime('2020年11月12日的14点', '%Y年%m月%d日的%H点'))

"""date_string (必需)：这是一个包含日期和/或时间信息的字符串，需要根据提供的格式进行解析。
format (必需)：是一个格式化字符串，用来描述 date_string 中各个部分（如年份、月份、日期、小时、分钟、秒等）的布局和格式。其中包含一些特殊的占位符，它们对应于日期和时间的不同组成部分。
格式化符号示例及含义：
%Y：四位数的完整年份（例如：2024）
%m：月份，以01到12的形式（例如：03表示三月）
%d：月份中的日，以01到31的形式
%H：24小时制小时数（例如：15表示下午3点）
%I：12小时制小时数（例如：03表示凌晨3点）
%M：分钟数（00到59）
%S：秒数（00到59）
%p：AM 或 PM 前缀（仅在使用 %I 时有效）
%y：两位数的年份（例如：24表示2024年）
%b：简写的月份名（例如：Mar）
%B：完整的月份名（例如：March）
%a：简写的星期名（例如：Sun）
%A：完整的星期名（例如：Sunday）
%j：一年中的第几天（001到366）
%w：星期几（0表示周一，6表示周日）
%z 或 %Z：时区名称或偏移量
"""
print('------------datetime--------------')
"""datetime 是 date 的子类，除了包含日期时间信息外，还包含时区信息。"""
import pytz

dt = datetime.today()
print(dt, type(dt))

dt = datetime(year=2022, month=12, day=12, hour=8, minute=29, second=34, microsecond=123123)
#  部分时间
print(dt.date(), '---', dt.time())

# 替换部分日期或者（和）时间
print(dt.replace(year=2024, day=29))

""" 转换时区，返回一个指定时区的 datetime 对象
dt.astimezone(tz)
    dt: 这是一个具有时区信息的 datetime 对象。
    tz: 这是目标时区对象，它可以是 timezone 实例或者如 pytz 库中的时区对象。
"""
print(dt.astimezone(timezone.utc))  # 2022-12-12 08:29:34.123123+00:00
print(dt.astimezone(pytz.timezone('US/Eastern')))  # 2022-12-11 19:29:34.123123-05:00

"""utcoffset() 是在 Python datetime 模块中与时区相关的 tzinfo 类的一个方法。
当一个 datetime 对象关联了具有时区信息的 tzinfo 对象时，
可以调用其 utcoffset() 方法来获取当前时间相对于协调世界时（UTC）的偏移量。
示例
"""
print(dt.astimezone(timezone.utc).utcoffset())
dt1 = datetime.now(timezone.utc)
offset = dt1.utcoffset()
print(offset)  # 在上述示例中，由于 dt 是基于 UTC 的，所以它的 utcoffset() 返回的是零偏移量，即 timedelta(0)。

# 夏令营时间
print(dt.dst())

# 返回时区名称
print(dt.tzname())

# 返回struct_time结构体,可迭代
print(
    dt.timetuple())  # time.struct_time(tm_year=2022, tm_mon=12, tm_mday=12, tm_hour=8, tm_min=29, tm_sec=34, tm_wday=0, tm_yday=346, tm_isdst=-1)
print(type(dt.timetuple()))  # <class 'time.struct_time'>
print([i for i in dt.timetuple()])
"""dt.timetuple() 是 Python datetime 对象的一个方法，
用于将 datetime 对象转换为一个标准的 time.struct_time 对象。
这个 struct_time 对象包含九个元素，分别是：
年份（四位数）
月份（1-12）
日期（1-31）
小时（0-23）
分钟（0-59）
秒（0-59）
星期（0-6，其中0代表周一）
一年中的第几天（1-366）
是否为夏令时（非零值表示是夏令时，但Python中通常用-1、0或1来表示不确定性、非夏令时和夏令时）
"""

# 返回时间戳
print(dt.timestamp())

# isoweekday() :返回星期几，星期一为1，星期天为7
print(dt.isoweekday())
# weekday(): 返回星期几，星期一为0，星期天为6
print(dt.weekday())
# isocalendar(): 日历元组，返回元组(year, week, weekday（星期一为1，星期天为7）)
print(x := dt.isocalendar(), '---',
      type(x))  # datetime.IsoCalendarDate(year=2022, week=50, weekday=1) --- <class 'datetime.IsoCalendarDate'>

# 返回标准格式
print(dt.isoformat())
print(dt.isoformat('B'))  # 2022-12-12B08:29:34.123123
print(dt.isoformat('T', 'hours'))  # 2022-12-12T08
"""isoformat() 返回的字符串包括年、月、日、时、分、秒，并且可能会有毫秒或微秒部分（取决于精度）
# 只获取日期部分的 ISO 格式
date_string = dt.date().isoformat()

返回根据 ISO 格式化的时间。
         完整格式类似于“YYYY-MM-DD HH:MM:SS.mmmmmm”。
         默认情况下，如果 self.microsecond == 0，则省略小数部分。

         如果 self.tzinfo 不是 None，则还会附加 UTC 偏移量，给出
         给出完整格式“YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM”。

         可选参数 sep 指定日期和时间之间的分隔符
         时间，默认“T”。

         可选参数 timespec 指定附加的数量
         时间条款包括在内。 有效选项为“自动”、“小时”、
         “分钟”、“秒”、“毫秒”和“微秒”
"""

print('----------------timedelta----------------')
"""两个时间点之间的间隔"""
# 构造一个时间间隔
dt = timedelta(days=100, hours=1, minutes=1, seconds=1, milliseconds=1, microseconds=1)
print(dt, type(dt))

dt1 = datetime.now()
dt2 = datetime(2024, 3, 8, 12, 12, 12, microsecond=23131)
print(x := (dt1 - dt2), type(x))  # 返回一个timedelta对象，<class 'datetime.timedelta'>
print(dt + dt1)
print(dt1 - dt)

print('---------------timezone----------------')
"""timezone继承自表示时区信息的抽象积累tzinfo，他们的每个实例都是由与UTC的固定偏移量定义的"""
from datetime import timezone

offset = timedelta(hours=8, minutes=0, seconds=0)
bjtz = timezone(offset, name='北京时间')
t = datetime.now(tz=timezone.utc)
print(t)
bj_t = t.astimezone(tz=bjtz)
print(bj_t)

print('---------------pytz----------------')

"""pytz： pytz 是一个非常流行的库，它提供了对 IANA 时区数据库的全面支持。通过这个库，你可以准确地处理世界各地复杂的时区转换和夏令时问题。
示例：
"""
import pytz

utc = pytz.UTC
# 时区列表在pytz的 common_timezones 中
eastern = pytz.timezone('US/Eastern')

utc_dt = datetime.now(utc)
eastern_dt = utc_dt.astimezone(eastern)

print(eastern_dt)

print('---------------datetime.timezone----------------')

"""datetime.timezone（Python 3.2+）： 自 Python 3.2 起，标准库中的 datetime 模块开始提供基本的时区支持。
    timezone 类可用于创建简单的时间区域对象，但其功能相比 pytz 更有限，尤其在处理夏令时方面可能不够完善。
"""

utc_tz = timezone.utc
est_tz = timezone(-timedelta(hours=5))  # 简化的美国东部时间

utc_dt = datetime.now(utc_tz)
est_dt = utc_dt.astimezone(est_tz)

print(est_dt)

print('---------------zoneinfo----------------')

"""zoneinfo（Python 3.9+）： Python 3.9 引入了内置的 zoneinfo 模块，这是一个基于 IANA 时区数据库的新模块，
    旨在替代 pytz 提供更现代化且原生的支持。由于它是Python标准库的一部分，因此不需要额外安装第三方库。
    
时区列表见：https://github.com/eggert/tz/blob/main/zonenow.tab
"""

from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")

eastern = ZoneInfo("America/New_York")

utc_dt = datetime.now(utc)
_dt = datetime.now()
print('utc_dt:', utc_dt, '\n', '_dt:', _dt)
eastern_dt = utc_dt.astimezone(eastern)

print(eastern_dt)

# 获取当前的UTC时间
utc_dt = datetime.now(ZoneInfo('UTC'))
# 将UTC时间转换成北京时间
bj_tz = ZoneInfo('Asia/Shanghai')  # 创建了一个表示北京时间的时区对象
bj_tz = utc_dt.astimezone(bj_tz)
print('北京时间：', bj_tz)
"""IANA（Internet Assigned Numbers Authority）时区数据库，也被称为 Olson 时区数据库或 tz database，
    是一个维护全球时区信息的权威数据库。
它为每个时区定义了一个唯一的标识符，这些标识符通常由地理区域名称组成，
例如：
America/New_York：美国纽约时区，包括东部时间（EST）和东部夏令时间（EDT）
Europe/London：英国伦敦时区，格林尼治标准时间（GMT）和英国夏令时间（BST）
Asia/Shanghai：中国上海时区，即中国标准时间（CST）
Australia/Sydney：澳大利亚悉尼时区
Africa/Cairo：埃及开罗时区

这些标识符能够准确地反映出各个地区复杂的时区规则，包括历史上的时区变更、夏令时的启用与停用等细节。在处理日期和时间相关的编程任务时，使用 IANA 时区数据库可以确保时区转换的准确性。在 Python 中，可以通过 pytz 库或从 Python 3.9 开始引入的标准库 zoneinfo 来利用这些标识符进行时区操作。
"""
import zoneinfo

# 获取所有的时区名称
# all_timezones = zoneinfo.available_timezones()
# for tz in all_timezones:
#     print(tz)
