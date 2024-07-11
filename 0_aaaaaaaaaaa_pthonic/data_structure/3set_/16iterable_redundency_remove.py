"""通过集合高效去重"""

list_of_fruit = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "grape", "pineapple", "pear",
                 "watermelon" "banana", "cherry", "orange", "kiwi", "mango"]


def get_unique_of_fruit(firuts):
    unique_of_fruit = []
    for fruit in firuts:
        if fruit not in unique_of_fruit:
            unique_of_fruit.append(fruit)

    return unique_of_fruit


def get_unique_of_fruits_with_set(firuts):
    return set(firuts)


print(get_unique_of_fruit(list_of_fruit))
print(get_unique_of_fruits_with_set(list_of_fruit))

"""使用集合方式去重能提升性能
有重复数据：有性能提升，相差3倍多
全部不重复的数据：极端情况下性能相差非常大，1000+倍
全部是重复数据：相差2.6倍
"""
