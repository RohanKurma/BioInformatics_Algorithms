from itertools import product

def hamming_distance(p, q):
    """Compute Hamming distance between two strings."""
    return sum(pi != qi for pi, qi in zip(p, q))

def neighbors(pattern, d):
    """
    Generate all k-mers within d mismatches of the given pattern.
    """
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}
    
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in "ACGT":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def motif_enumeration(Dna, k, d):
    """
    Find all (k,d)-motifs in a collection of DNA strings.
    
    Args:
        Dna (list): List of DNA sequences.
        k (int): Length of motifs.
        d (int): Max allowed mismatches.
        
    Returns:
        set: All (k,d)-motifs found in every string of Dna.
    """
    Patterns = set()
    
    # Loop over each sequence in Dna
    for dna in Dna:
        for i in range(len(dna) - k + 1):
            kmer = dna[i:i+k]
            # Generate all neighbors of this kmer
            for neighbor in neighbors(kmer, d):
                # Check if neighbor appears in ALL sequences
                found = True
                for other_dna in Dna:
                    # Check if neighbor appears with ≤ d mismatches
                    if not any(hamming_distance(neighbor, other_dna[j:j+k]) <= d
                               for j in range(len(other_dna) - k + 1)):
                        found = False
                        break
                if found:
                    Patterns.add(neighbor)
    return Patterns

# Dna = [
#     "ATTTGGC",
#     "TGCCTTA",
#     "CGGTATC",
#     "GAAAATT"
# ]
# k = 3
# d = 1

# print(motif_enumeration(Dna, k, d))

with open('dataset_30302_8.txt', 'r') as f:
    k, d = map(int, f.readline().strip().split())
    Dna = [line.strip() for line in f.readlines()]

print(' '.join(motif_enumeration(Dna, k, d)))