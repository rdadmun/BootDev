#Take a look at this imperative code that calculates the factorial of a number:

def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#Here's the same factorial function using reduce:

import functools

def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))