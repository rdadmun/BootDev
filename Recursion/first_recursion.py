def factorial_r(x):
    if x <= 0:
        return 1
    result = x * factorial_r(x-1)
    return result
    
