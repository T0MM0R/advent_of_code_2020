def number_in_list(list_of_nums, num):
    try:
        list.index(num)
        return True
    except:
        return False


def number_in_list(list_of_nums, num):
    try:
        list.index(num)
        return num
    except:
        return False


def solve_for_2020(list_of_nums):
    for num in list_of_nums:
        target_num = 2020 - num
        if number_in_list(list_of_nums, target_num):
            return [num, number_in_list(list_of_nums, target_num)]

def string_to_list_of_ints(string):
    list_of_nums = string.split('\n')
    return [int(num) for num in list_of_nums]
