import random

# ---------------- Helper Functions ----------------

def hamming_distance(p, q):
    """Compute the Hamming distance between two strings."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(p, q))

def score(motifs):
    """Compute the total score of motifs (lower = better)."""
    k = len(motifs[0])
    total_score = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(base) for base in "ACGT")
        total_score += len(motifs) - max_count
    return total_score

def profile_with_pseudocounts(motifs):
    """Build a profile matrix with pseudocounts (+1)."""
    k = len(motifs[0])
    profile = {b: [1]*k for b in "ACGT"}  # initialize with pseudocounts
    for motif in motifs:
        for i, base in enumerate(motif):
            profile[base][i] += 1
    # Normalize
    for i in range(k):
        total = sum(profile[b][i] for b in "ACGT")
        for b in "ACGT":
            profile[b][i] /= total
    return profile

def profile_most_probable_kmer(text, k, profile):
    """Find the k-mer in text that has the highest probability given a profile."""
    max_prob = -1
    best_kmer = text[0:k]
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j, base in enumerate(kmer):
            prob *= profile[base][j]
        if prob > max_prob:
            max_prob = prob
            best_kmer = kmer
    return best_kmer

def random_motifs(Dna, k):
    """Select a random k-mer from each DNA string."""
    motifs = []
    for seq in Dna:
        start = random.randint(0, len(seq) - k)
        motifs.append(seq[start:start + k])
    return motifs

# ---------------- Core Algorithm ----------------

def randomized_motif_search(Dna, k, t):
    """Run one iteration of the Randomized Motif Search algorithm."""
    motifs = random_motifs(Dna, k)
    best_motifs = motifs[:]
    while True:
        profile = profile_with_pseudocounts(motifs)
        motifs = [profile_most_probable_kmer(seq, k, profile) for seq in Dna]
        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]
        else:
            return best_motifs

def repeated_randomized_motif_search(Dna, k, t, n_runs=1000):
    """Run RandomizedMotifSearch multiple times and return the best motifs found."""
    best_motifs = randomized_motif_search(Dna, k, t)
    best_score = score(best_motifs)
    for i in range(n_runs - 1):
        motifs = randomized_motif_search(Dna, k, t)
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
    return best_motifs

