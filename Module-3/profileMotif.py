def profile_most_probable_kmer(text, k, profile):
    max_prob = -1
    most_probable_kmer = text[0:k]  # Default to first k-mer if all equal
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j, base in enumerate(kmer):
            if base == 'A':
                prob *= profile['A'][j]
            elif base == 'C':
                prob *= profile['C'][j]
            elif base == 'G':
                prob *= profile['G'][j]
            elif base == 'T':
                prob *= profile['T'][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer

    return most_probable_kmer

text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = {
    'A': [0.2, 0.2, 0.3, 0.2, 0.3],
    'C': [0.4, 0.3, 0.1, 0.5, 0.1],
    'G': [0.3, 0.3, 0.5, 0.2, 0.4],
    'T': [0.1, 0.2, 0.1, 0.1, 0.2]
}

result = profile_most_probable_kmer(text, k, profile)
print("Profile-most probable k-mer:", result)

with open('dataset_30305_3.txt', 'r') as file:
    lines = file.readlines()
    text = lines[0].strip()
    k = int(lines[1].strip())
    profile = {
        'A': list(map(float, lines[2].strip().split())),
        'C': list(map(float, lines[3].strip().split())),
        'G': list(map(float, lines[4].strip().split())),
        'T': list(map(float, lines[5].strip().split()))
    }
result = profile_most_probable_kmer(text, k, profile)
print("Profile-most probable k-mer from file:", result)