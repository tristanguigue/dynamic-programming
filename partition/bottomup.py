# The partition string problem retrieving the original string whose spaces
# were removed.
# We are given a list of words belonging to a dictionary
#
# Input: carlosthinksthattheweatherisnice
# Output: carlos thinks that the weather is nice

# The dictionary of available words
dictionary = {
    "thinks": True,
    "that": True,
    "the": True,
    "weather": True,
    "is": True,
    "nice": True
}


def cost(word):
    """Evaluate the cost of a given word. 0 if the word is in the dictionary,
    the number of characters otherwise

    Args:
        word (string): a string whose cost need to be evaluated

    Returns:
        The cost of the word (int)
    """
    if word in dictionary:
        return 0
    else:
        return len(word)


def split(s):
    # this is the array of partial solutions
    m = {}

    # we initialize our boundary condition
    m[len(s)] = ('', 0)

    # we build our partial solution backward
    for i in range(len(s) - 1, -1, -1):

        min_cost = None
        min_string = None

        for k in range(i, len(s)):
            substring = s[i:k + 1]
            # we use the already calculated cost of the substring starting at
            # k + 1
            current_cost = cost(substring) + m[k + 1][1]

            if min_cost is None or current_cost < min_cost:
                # if the two parts are not empty join them with space
                if substring and m[k + 1][0]:
                    min_string = substring + ' ' + m[k + 1][0]
                    min_cost = current_cost + 1
                else:
                    min_string = substring + m[k + 1][0]
                    min_cost = current_cost

        m[i] = min_string, min_cost

    return m[0]


print split("carlosthinksthattheweatherisnice")
# print ('carlos thinks that the weather is nice', 12)
