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


def split(input_string, start, number_of_partitions):
    """The recrusive function, it tries to split the substring starting at
    `start` into `number_of_partitions` words

    Args:
        input_string (string): the initial string that needs to be split
        start (int): we want to split the substring of input_string
            starting at that index
        number_of_partitions (int): the maximum number of partitions we can use
            to split this substring

    Returns:
        A tupple form of the partial solution and its cost
    """

    # the substring to split
    substring = input_string[start:]

    # Those are the boundary conditions
    # if we're out of partitions return the substring and its cost
    if not number_of_partitions:
        return substring, cost(substring)

    # if the substring is empty return an empty string with no cost
    if not len(substring):
        return '', 0

    min_cost = None
    min_string = None

    # we place our next partition somewhere between start and the end of the
    # input_string
    for i in range(0, len(substring) + 1):
        # we split the rest of the string recursively
        rest_string, rest_cost = split(input_string, start + i,
                                       number_of_partitions - 1)

        current_string = substring[:i]
        current_cost = cost(current_string) + rest_cost

        # update minum cost and string if it's the best so far
        if min_cost is None or current_cost < min_cost:
            min_cost = current_cost

            # if the two parts are not empty join them with space
            if current_string and rest_string:
                min_string = current_string + ' ' + rest_string
            else:
                min_string = current_string + rest_string

    return min_string, min_cost


input_string = "carlosisnice"

print split(input_string, 0, len(input_string) - 1)
# print ('carlos is nice', 6)
