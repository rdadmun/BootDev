def sum_nested_list(lst):
    sum_so_far = 0
    for item in lst:
        if isinstance(item, list) == True:
            sum_so_far += sum_nested_list(item)
        else:
            sum_so_far += item
    return sum_so_far