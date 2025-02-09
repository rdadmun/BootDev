# Polynomial vs. Exponential
# Broadly speaking, algorithms can be classified into two categories:
# “Polynomial time”
# “Exponential time”

# Back in the 1970s, some computer scientist researchers wanted to come up with a good, descriptive name for the set of polynomial time algorithms. After much deliberation, they settled on the letter P (naming things is hard).
# The hand-wavy takeaway is that:
# Problems that fall into class P are practical to solve on computers.
# Problems that don’t fall into P are hard, slow, and impractical.

# Fibonacci Sequence Function in exponential time
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Fibonacci Sequence Function in polynomial time
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    grandparent = 0
    parent = 1
    for _ in range(n-1):
        current = grandparent + parent
        grandparent = parent
        parent = current
    return current

# Power Set in Exponential Time
def power_set(input_set):
    if not input_set:
        return [[]]
    power_list = []
    first = input_set[0]
    rest_subset = power_set(input_set[1:])
    for subset in rest_subset:
        power_list.append(subset)
        power_list.append([first] + subset)

    return power_list
    
# Exponential Growth Sequences
def exponential_growth(n, factor, days):
    growth_sequence = []
    for i in range(days + 1):
        result = n * (factor ** i)
        growth_sequence.append(result)
    return growth_sequence

# Travel Time Limit
def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1
    while time_left >= time_in_country:
        time_left -= time_in_country
        count += 1
        time_in_country *= factor
    return count
