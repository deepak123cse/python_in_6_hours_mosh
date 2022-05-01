def find_max(num_list):
    max_value = num_list[0]
    for num_item in num_list:
        if num_item > max_value:
            max_value = num_item
    return max_value


