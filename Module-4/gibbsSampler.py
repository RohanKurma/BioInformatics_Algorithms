import random

# ---------- Helper Functions ----------

def hamming_distance(p, q):
    """Compute the Hamming distance between two strings."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(p, q))

def score(motifs):
    """Compute total motif score (lower is better)."""
    k = len(motifs[0])
    total = 0
    for i in range(k):
        col = [m[i] for m in motifs]
        max_count = max(col.count(b) for b in "ACGT")
        total += len(motifs) - max_count
    return total

def profile_with_pseudocounts(motifs):
    """Build profile matrix with pseudocounts."""
    k = len(motifs[0])
    profile = {b: [1]*k for b in "ACGT"}  # +1 pseudocount
    for motif in motifs:
        for i, base in enumerate(motif):
            profile[base][i] += 1
    for i in range(k):
        total = sum(profile[b][i] for b in "ACGT")
        for b in "ACGT":
            profile[b][i] /= total
    return profile

def profile_probability(kmer, profile):
    """Compute probability of a k-mer given a profile."""
    prob = 1
    for i, base in enumerate(kmer):
        prob *= profile[base][i]
    return prob

def weighted_random_choice(kmers, probs):
    """Choose one k-mer based on weighted probabilities."""
    total = sum(probs)
    probs = [p / total for p in probs]
    return random.choices(kmers, weights=probs, k=1)[0]

def random_motifs(Dna, k):
    """Randomly select one k-mer from each DNA string."""
    motifs = []
    for seq in Dna:
        start = random.randint(0, len(seq) - k)
        motifs.append(seq[start:start + k])
    return motifs

# ---------- Gibbs Sampler ----------

def gibbs_sampler(Dna, k, t, N):
    """Run one Gibbs Sampler instance."""
    motifs = random_motifs(Dna, k)
    best_motifs = motifs[:]

    for j in range(N):
        i = random.randint(0, t - 1)
        motifs_excluding_i = motifs[:i] + motifs[i+1:]
        profile = profile_with_pseudocounts(motifs_excluding_i)

        # Generate all possible k-mers for Dna[i]
        kmers = [Dna[i][x:x+k] for x in range(len(Dna[i]) - k + 1)]
        probs = [profile_probability(kmer, profile) for kmer in kmers]
        motifs[i] = weighted_random_choice(kmers, probs)

        # Update best motifs if score improves
        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]

    return best_motifs

def repeated_gibbs_sampler(Dna, k, t, N, runs=20):
    """Run GibbsSampler multiple times to avoid local optima."""
    best_motifs = gibbs_sampler(Dna, k, t, N)
    best_score = score(best_motifs)
    for _ in range(runs - 1):
        motifs = gibbs_sampler(Dna, k, t, N)
        s = score(motifs)
        if s < best_score:
            best_motifs = motifs
            best_score = s
    return best_motifs
