def find_minimum(nums):
    minimum = float("inf")
    if not nums: 
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

def sum(nums):
    answer = 0
    if not nums:
        return answer
    for num in nums:
        answer += num
    return answer

def average_followers(nums):
    answer = 0
    sum = 0
    if not nums:
        return None
    for num in nums:
        sum += num
        answer = sum / len(nums)
    return answer


def median_followers(nums):
    if not nums:
        return None
    sorted_nums = sorted(nums)
    middle = len(sorted_nums) // 2
    
    if len(sorted_nums) % 2 == 0:
        return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2
    else:
        return sorted_nums[middle]
    
    
def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return 0
    sum_follows = sum(audiences_followers)
    avg = sum_follows / len(audiences_followers)
    answer = avg * (len(audiences_followers) ** 1.2)
    return answer

def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        multiplyer = 4
    elif influencer_type == "cosmetic":
        multiplyer = 3
    else:
        multiplyer = 2
    
    for i in range(num_months):
        follower_count *= multiplyer
        
    return follower_count