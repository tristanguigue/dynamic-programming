# Find the longest increasing sequence from an array
#
# Input: [1, 6, 7, 4, 6, 1, 3, 4, 6, 19, 12, 14, 35, 66]
# Output: [1, 3, 4, 6, 12, 14, 35, 66]


def longest_increasing_sequence(input_array):
    """Finds the longest increasing sequence for the array
    Args:
        input_array (array): the given array
    Returns:
        The longest increasing sequence of this array
    """
    if not input_array:
        return []

    # Initialize the max_sequence with first element
    max_seq = [input_array[0]]
    sequences = [max_seq]

    for i in range(1, len(input_array)):
        # Loop through all the previous sequences and add current element if
        # possible
        for i in range(len(sequences) - 1, -1, -1):
            seq = sequences[i]

            if seq[- 1] < input_array[i]:
                sequences.append(seq + [input_array[i]])

                # Update the longest sequence found so far
                if len(sequences[-1]) > len(max_seq):
                    max_seq = sequences[-1]
                break
        else:
            # Add a new sequence starting at i if we didn't append the element
            sequences.append([input_array[i]])

    return max_seq


print longest_increasing_sequence(
    [1, 6, 7, 4, 6, 1, 3, 4, 6, 19, 12, 14, 35, 66])
# [1, 3, 4, 6, 12, 14, 35, 66]
