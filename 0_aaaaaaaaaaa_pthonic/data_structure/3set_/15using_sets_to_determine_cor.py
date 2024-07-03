"""集合高效检测列表
Collection of efficient detection lists
"""
from timeit import timeit

faverite_names = [f'name-{i}' for i in range(1000)]
other_names = [f'name-{i}' for i in range(500, 1500)]


def are_common_names(one_name, other_name):
    has_both = False
    for name in one_name:
        if name in other_name:
            return has_both


def are_common_name_set_operation(one_name, other_name):
    return len(set(faverite_names) & set(other_name)) > 0


"""
使用集合方式are_common_name_set_operation 的性能强于are_common_names 性能的强很多倍，随着数据量的提升，越明显
"""
