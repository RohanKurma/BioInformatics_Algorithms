def frequentWordswithMissmatches(Text, k, d):
    from collections import defaultdict

    def hammingDistance(p, q):
        """Compute the Hamming distance between two strings."""
        return sum(pc != qc for pc, qc in zip(p, q))

    def neighbors(pattern, d):
        """Generate the d-neighborhood of a pattern."""
        if d == 0:
            return {pattern}
        if len(pattern) == 0:
            return {""}
        
        neighborhood = set()
        suffix_neighbors = neighbors(pattern[1:], d)
        for text in suffix_neighbors:
            if hammingDistance(pattern[1:], text) < d:
                for nucleotide in "ACGT":
                    neighborhood.add(nucleotide + text)
            else:
                neighborhood.add(pattern[0] + text)
        return neighborhood

    frequency_map = defaultdict(int)
    n = len(Text)

    for i in range(n - k + 1):
        pattern = Text[i:i + k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            frequency_map[neighbor] += 1

    max_count = max(frequency_map.values())
    frequent_patterns = [pattern for pattern, count in frequency_map.items() if count == max_count]

    return frequent_patterns



with open('dataset_30278_9.txt','r') as f:
    lines = f.readlines()
    Text = lines[0].strip()
    k, d = map(int, lines[1].strip().split())
    result = frequentWordswithMissmatches(Text, k, d)
    print(' '.join(result))