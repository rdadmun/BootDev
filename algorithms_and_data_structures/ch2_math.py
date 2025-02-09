#A logarithm is the inverse of an exponent.
#24 = 16
#log216 = 4

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

import math


def get_influencer_score(num_followers, average_engagement_percentage):
    score = average_engagement_percentage * math.log(num_followers,2)
    return score


#Factorial Function
def num_possible_orders(num_posts):
    answer = 1
    for post in range(1, num_posts + 1):
        answer *= post
    return answer

#Exponential Decay
def decayed_followers(intl_followers, fraction_lost_daily, days):
    retention_rate = 1 - fraction_lost_daily
    remaining = intl_followers * (retention_rate ** days)
    return remaining

# Logarithmic Scale
import math

def log_scale(data, base):
    log_data = []
    for d in data:
        calc = math.log(d, base)
        log_data.append(calc)
    return log_data

