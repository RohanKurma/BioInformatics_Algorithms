def read_dataset(filename):
    with open(filename) as f:
        parts = f.read().split()
        k = int(parts[0])
        t = int(parts[1])
        Dna = parts[2:]  # the rest are the 25 DNA strings
    return k, t, Dna




def profile_most_probable_kmer(text, k, profile):

    nucleotides = {'A', 'C', 'G', 'T'}

    max_probability = -1.0

    most_probable_kmer = ""

 

    for i in range(len(text) - k + 1):

        kmer = text[i:i+k]

        probability = 1.0

 

        for j, nucleotide in enumerate(kmer):

            probability *= profile[nucleotide][j]

 

        if probability > max_probability:

            max_probability = probability

            most_probable_kmer = kmer

 

    return most_probable_kmer

 

def form_profile(motifs):

    k = len(motifs[0])

    profile = {nucleotide: [0] * k for nucleotide in 'ACGT'}

    t = len(motifs)

 

    for i in range(k):

        column = [motif[i] for motif in motifs]

        for nucleotide in 'ACGT':

            count = column.count(nucleotide)

            profile[nucleotide][i] = count / t

 

    return profile

 

def score_motifs(motifs):

    k = len(motifs[0])

    t = len(motifs)

    score = 0

 

    for i in range(k):

        column = [motif[i] for motif in motifs]

        max_count = max(column.count(nucleotide) for nucleotide in 'ACGT')

        score += t - max_count

 

    return score

 

def greedy_motif_search(dna, k, t):

    best_motifs = [seq[:k] for seq in dna]

    for i in range(len(dna[0]) - k + 1):

        motif1 = dna[0][i:i+k]

        motifs = [motif1]

 

        for j in range(1, t):

            profile = form_profile(motifs)

            most_probable_kmer = profile_most_probable_kmer(dna[j], k, profile)

            motifs.append(most_probable_kmer)

 

        if score_motifs(motifs) < score_motifs(best_motifs):

            best_motifs = motifs

 

    return best_motifs
def form_profile_with_pseudocounts(motifs):
    k = len(motifs[0])
    profile = {nuc: [1] * k for nuc in 'ACGT'}  # initialize with pseudocounts (1)
    t = len(motifs)
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            profile[nucleotide][i] += 1
    # normalize
    for nuc in 'ACGT':
        profile[nuc] = [val / (t + 4) for val in profile[nuc]]
    return profile


def greedy_motif_search_with_pseudocounts(Dna, k, t):

    BestMotifs = [dna[:k] for dna in Dna]

    first_dna = Dna[0]
    
    for i in range(len(first_dna) - k + 1):

        motifs = [first_dna[i:i+k]]

        for j in range(1, t):
            profile = form_profile_with_pseudocounts(motifs)

            next_motif = profile_most_probable_kmer(Dna[j], k, profile)

            motifs.append(next_motif)

        if score_motifs(motifs) < score_motifs(BestMotifs):

            BestMotifs = motifs
            
    return BestMotifs


 


# === RUN ON YOUR DATASET ===
k, t, Dna = read_dataset("dataset_30306_9.txt")
print(f"k={k}, t={t}, number of DNA strings={len(Dna)}")
result = greedy_motif_search(Dna, k, t)
print("*********************************************************************")

# Print motifs space separated
print(" ".join(result))
print("*********************************************************************")
result_with_pseudocounts = greedy_motif_search_with_pseudocounts(Dna, k, t)
print(" ".join(result_with_pseudocounts))