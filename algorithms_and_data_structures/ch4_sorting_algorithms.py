# Sorted List 1
class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"
# dont touch above this line
def vanity(influencer):
    return (influencer.num_bio_links * 5) + influencer.num_selfies

def vanity_sort(influencers):
    sorted_list = sorted(influencers, key=vanity)
    return sorted_list

# Bubble Sort
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping is True:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums
                
# Merge Sort
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left,right)


def merge(first, second):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(first) and right_index < len(second):
        if first[left_index] < second[right_index]:
            result.append(first[left_index])
            left_index += 1
        else:
            result.append(second[right_index])
            right_index += 1

    result.extend(first[left_index:])
    result.extend(second[right_index:])

    return result
# We use merge sort for a fast algorithm where memory isn't an issue


# Insertion sort
# It’s much less efficient on large lists than merge sort because it’s O(n^2), 
# but it’s actually faster (not in Big O terms, but due to smaller constants) than merge sort on small lists.
def insertion_sort(nums):
    for i in range(1,len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums [j-1] = nums[j-1], nums[j]
            j -= 1
    return nums
# Complexity = O(n^2)


# Quick sort
# Quick sort is an efficient sorting algorithm that’s widely used in production sorting implementations. 
# Like merge sort, quick sort is a recursive divide and conquer algorithm.
def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i +1], nums[high] = nums[high], nums[i + 1]
    return i + 1

#Pros:
#Very fast: At least it is in the average case
#In-Place: Saves on memory, doesn’t need to do a lot of copying and allocating
#Cons:
#Typically unstable: changes the relative order of elements with equal keys
#Recursive: can incur a performance penalty in some implementations
#Pivot sensitivity: if the pivot is poorly chosen, it can lead to poor performance

# Selection sort
# Another sorting algorithm we never covered in-depth is called “selection sort”. 
# It’s similar to bubble sort in that it works by repeatedly swapping items in a list. 
# However, it’s slightly more efficient than bubble sort because it only makes one swap per iteration.

def selection_sort(nums):
    n = len(nums)
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums