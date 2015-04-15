# Find the nth fibonacci number
#
# Input: 4
# Output: 3


def fibonacci(n):
    # boundary conditions:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print fibonacci(4)
# print 3
