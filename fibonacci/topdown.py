# Find the nth fibonacci number
#
# Input: 4
# Output: 3

cache = {}


def fibonacci(n):

    if n in cache:
        return cache[n]

    # boundary conditions:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fn = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = fn
    return fn


print fibonacci(45)
# print 1134903170
