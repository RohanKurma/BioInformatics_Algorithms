
def reverseCompliment(dna):
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev_comp = ''.join(complement[base] for base in reversed(dna))
    return rev_comp

if __name__ == "__main__":

    with open("dataset_30273_2.txt", "r") as file:
        dna = file.read().strip()
        result = reverseCompliment(dna)
        print(result)