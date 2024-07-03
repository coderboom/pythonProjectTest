"""合并字典"""
"""
冲突点：有相同的键
"""
fruit_price_map_gz = {'apple': 10.5, 'orange': 8.8}
fruit_price_map_sh = {'banana': 3.2, 'orange': 5.8}
fruit_price_map_bj = {'watermelon': 3.2, 'orange': 78.8}

merged_price_map = {}
merged_price_map.update(fruit_price_map_gz)
merged_price_map.update(fruit_price_map_sh)
merged_price_map.update(fruit_price_map_bj)

print('--------------------------覆盖先加入字典的相同键的值----------------------------')
"""覆盖冲突的键的值
后加入的字典的键与之前字典的键存在冲突，会用后者的值覆盖前者的值，而不是后加入的键值对覆盖之前的键值对
"""
print(merged_price_map)  # {'apple': 10.5, 'orange': 78.8, 'banana': 3.2, 'watermelon': 3.2}

"""
** ： 解包操作性能更好，推荐使用
"""
merged_dict = {**fruit_price_map_gz, **fruit_price_map_sh, **fruit_price_map_bj}
print(merged_dict)  # 与update效果一样，
