"""
1.将目标值与列表中间的值相比
2.如果目标值大于列表中间的值则取列表右半部分的数据
3.如果目标值小于列表中间的值则取列表左半部分的数据
4.如果与列表中间的值相等，则找到目标值
"""


def binary_search(target_num, num_list):
    print(num_list)
    if len(num_list) == 0:
        print('您找的值不存在')
        return
    mid_value = len(num_list) // 2
    if target_num > num_list[mid_value]:
        num_list = num_list[mid_value + 1:]
        binary_search(target_num, num_list)
    elif target_num < num_list[mid_value]:
        num_list = num_list[:mid_value]
        binary_search(target_num, num_list)
    else:
        print('find it')


l = [-2, 3, 7, 9, 28, 30, 35, 46, 58, 69, 73, 88, 100]
find_num = 88

binary_search(find_num, l)
