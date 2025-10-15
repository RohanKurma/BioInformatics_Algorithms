
def minimum_skew(dna):
    """
    Finds the position(s) in the DNA string where the skew (the difference between
    the number of 'G's and 'C's) is minimized.

    Parameters:
    dna (str): A string representing the DNA sequence.

    Returns:
    list: A list of positions (0-based index) where the skew is minimized.
    """
    skew = 0
    min_skew = 0
    min_positions = [0]

    for i, nucleotide in enumerate(dna):
        if nucleotide == 'G':
            skew += 1
        elif nucleotide == 'C':
            skew -= 1

        if skew < min_skew:
            min_skew = skew
            min_positions = [i + 1]  # +1 to convert to 1-based index
        elif skew == min_skew:
            min_positions.append(i + 1)  # +1 to convert to 1-based index

    return min_positions

with open('dataset_30277_10.txt', 'r') as file:
    dna = file.read().strip()
    result = minimum_skew(dna)
    print(" ".join(map(str, result)))