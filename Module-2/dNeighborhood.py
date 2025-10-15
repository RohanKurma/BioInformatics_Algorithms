from hamming_distance import hamming_distance
def dNeighborhood(seq, k):
    """Generate the d-neighborhood of a sequence.

    Args:
        seq (str): The input sequence.
        k (int): The maximum number of mismatches allowed.
    Returns:
        set: A set containing all sequences in the d-neighborhood of the input sequence.
    """
    if k == 0:
        return {seq}
    if len(seq) == 0:
        return {""}

    neighborhood = set()
    suffix_neighbors = dNeighborhood(seq[1:], k)

    for text in suffix_neighbors:
        if hamming_distance(seq[1:], text) < k:
            for nucleotide in "ACGT":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(seq[0] + text)

    return neighborhood

# Example usage:
if __name__ == "__main__":
    with open('dataset_30282_4.txt', 'r') as file:
        lines = file.readlines()
        sequence = lines[0].strip()
        d = int(lines[1].strip())
        result = dNeighborhood(sequence, d)
        print(" ".join(sorted(result)))
