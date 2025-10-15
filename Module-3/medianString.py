def MedianString(Dna, k):
    from itertools import product

    def HammingDistance(p, q):
        return sum(pc != qc for pc, qc in zip(p, q))

    def DistanceBetweenPatternAndStrings(Pattern, Dna):
        return sum(min(HammingDistance(Pattern, text[i:i+len(Pattern)]) for i in range(len(text) - len(Pattern) + 1)) for text in Dna)

    patterns = [''.join(p) for p in product('ACGT', repeat=k)]
    median = min(patterns, key=lambda pattern: DistanceBetweenPatternAndStrings(pattern, Dna))
    
    return median

dna = "AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTTCGGGACAG".split()
k = 3
print(MedianString(dna, k))

with open("dataset_30304_9.txt") as f:
    lines = f.read().strip().splitlines()
    k = int(lines[0])
    dna = lines[1:]
    print(dna)
    print(MedianString(dna, k))