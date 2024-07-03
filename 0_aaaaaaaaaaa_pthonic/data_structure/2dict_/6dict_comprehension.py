"""通过字典推导来优化字典应用"""
"""
1 可读性增加
2 性能增加
"""
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str


list_of_users = [User('Bob', 'bob@local'), User('Jack', 'jack@local')]

# 一般方法构造字典
emails_of_user = {}
for user in list_of_users:
    if user.email:
        emails_of_user[user.name] = user.email

print(emails_of_user)

"""pythonic 方式构造dict

特别是在数据量很大（百万）的情况下
"""
emails_for_user = {user.name: user.email for user in list_of_users if user.email}
print(emails_for_user)
