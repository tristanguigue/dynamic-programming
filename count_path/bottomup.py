# number of possible paths from (x1, y1) to (x2, y2) moving right or down
# Input: (0, 0, 1, 1)
# Output : 2

cache = {}


def count_paths(x1, y1, x2, y2):

    # boundary conditions
    # at the destination, there is no more paths to consider
    cache[x2, y2] = 0

    # if we are on the border, the only path left is all the way right/down
    for i in range(0, x2):
        cache[i, y2] = 1

    for j in range(0, y2):
        cache[x2, j] = 1

    # move left / up and use the partial solutions at i + 1, j and i, j + 1
    for i in range(x2 - 1, -1, -1):
        for j in range(y2 - 1, -1, -1):
            cache[i, j] = cache[i + 1, j] + cache[i, j + 1]

    # the number of path from point 0, 0 to the destination
    return cache[0, 0]

print count_paths(0, 0, 1, 1)
