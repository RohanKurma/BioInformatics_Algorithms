
def hamming_distance(seq1, seq2):   

    """Calculate the Hamming distance between two sequences.

    The Hamming distance is defined as the number of positions at which
    the corresponding symbols are different. It is only defined for sequences
    of equal length.

    Args:
        seq1 (str): The first sequence.
        seq2 (str): The second sequence.
    Returns:
        int: The Hamming distance between the two sequences.
    Raises:
        ValueError: If the sequences are of different lengths.
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length")

    distance = sum(el1 != el2 for el1, el2 in zip(seq1, seq2))
    return distance


if __name__ == "__main__":
    with open('dataset_30278_3.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()
        print(seq1)
        print(seq2)

        print(hamming_distance(seq1, seq2))
        # try:
        #     result = hamming_distance(seq1, seq2)
        #     print(result)
        # except ValueError as e:
        #     print(e)