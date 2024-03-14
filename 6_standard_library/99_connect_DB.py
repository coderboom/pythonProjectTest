import pymysql

# 定义连接参数
host = 'localhost'  # MySQL服务器地址，默认为本地主机
port = 3306  # MySQL服务端口，默认为3306
user = 'root'  # 数据库用户名
password = 'leaf102369'  # 数据库密码
database = 'studet'  # 要连接的数据库名

# 创建连接
connection = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             password=password,
                             db=database,
                             charset='utf8mb4')  # 设置字符集

try:
    with connection.cursor() as cursor:

        # 执行SQL查询语句，例如创建表、插入数据等
        sql = "SELECT * FROM class"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # 关闭数据库连接
    connection.close()
