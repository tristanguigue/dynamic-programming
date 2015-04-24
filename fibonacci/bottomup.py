# Find the nth fibonacci number
#
# Input: 4
# Output: 3


def fibonacci(n):

    fn_2 = 0
    fn_1 = 1

    for i in range(2, n + 1):
        fi = fn_1 + fn_2
        fn_1, fn_2 = fi, fn_1

    return fi

print fibonacci(10)
# print 55
