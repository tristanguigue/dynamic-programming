# Find the longest increasing sequence from an array
#
# Input: [1, 6, 7, 4, 6, 1, 3, 4, 6, 19, 12, 14, 35, 66]
# Output: [1, 3, 4, 6, 12, 14, 35, 66]


def longest_increasing_sequence(input_array, sequences, i):
    """Finds the longest increasing sequence ending at `i`
    Args:
        sequences (array): the list of sequences to be appended
        input_array (array): the initial sequence
        i (int): the position of the cursor
    Returns:
        The longest increasing sequence ending at `i`
    """

    # Once we reach the bottom of the array, append the first element
    if i == 0:
        sequences.append([input_array[0]])
        return sequences[0]

    # Recurse to find the longest increasing sequence ending at `i - 1`
    max_seq = longest_increasing_sequence(input_array, sequences, i - 1)

    # Loop through all the previous sequences and add current element if
    # possible
    for seq in sequences:

        if seq[- 1] < input_array[i]:
            sequences.append(seq + [input_array[i]])

            # Update the longest sequence found so far
            if len(sequences[-1]) > len(max_seq):
                max_seq = sequences[-1]

    sequences.append([input_array[i]])

    return max_seq


a = [1, 6, 7, 4, 6, 3, 4, 6, 19, 12, 14, 35, 66]

print longest_increasing_sequence(a, [], len(a) - 1)
# [1, 3, 4, 6, 12, 14, 35, 66]
