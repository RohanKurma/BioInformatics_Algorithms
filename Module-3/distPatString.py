def hamming_distance(p, q):
    return sum(pi != qi for pi, qi in zip(p, q))
def distance_between_pattern_and_strings(pattern, Dna):
    k = len(pattern)
    total_distance = 0

    for text in Dna:
        min_distance = float('inf')
        # Slide a window of size k through the current DNA string
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            dist = hamming_distance(pattern, kmer)
            if dist < min_distance:
                min_distance = dist
        total_distance += min_distance

    return total_distance

pattern = "AAA"
Dna = [
    "TTACCTTAAC",
    "GATATCTGTC",
    "ACGGCGTTCG",
    "CCCTAAAGAG",
    "CGTCAGAGGT"
]

print(distance_between_pattern_and_strings(pattern, Dna))


with open('dataset_30312_1.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    pattern = lines[0]
    Dna = lines[1].split()
    result = distance_between_pattern_and_strings(pattern, Dna)
    print(result)