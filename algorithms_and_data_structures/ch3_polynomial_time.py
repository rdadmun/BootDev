# O(n)
def find_max(nums):
    max = float('-inf')
    for num in nums:
        if num > max:
            max = num
    return max

# O(n^2)
def does_name_exist(first_names, last_names, full_name):
    full_name = full_name.strip().lower()
    for first in first_names:
        for last in last_names:
            full = (first + " " + last).strip().lower()
            if full == full_name:
                return True
    return False

#O(nm)
def get_avg_brand_followers(all_handles, brand_name):
    total_brand_followers = 0
    total_influencers = len(all_handles)

    if total_influencers == 0:
        return 0
    
    for handles in all_handles:
        total_brand_followers += sum(1 for handle in handles if brand_name in handle)

    return round(total_brand_followers / total_influencers, 2)

# O(1)
def find_last_name(names_dict, first_name):
    #for current_first_name, last_name in names_dict.items():
        #if current_first_name == first_name:
            #return last_name
    return names_dict.get(first_name)

#O(log(n))
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median -1    
    
    return False

# Name Count
def count_names(list_of_lists, target_name):
    total_target_names = 0
    length_lists = len(list_of_lists)

    if len(list_of_lists) == 0:
        return 0
    for names in list_of_lists:
        total_target_names += sum(1 for name in names if target_name in name)

    return total_target_names

# Remove Duplicates
def remove_duplicates(nums):
    seen = set()
    unique_nums = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            unique_nums.append(num)

    return unique_nums
