def frequentKmers(text, k):
    """Returns a list of the most frequent k-mers in a given text.

    Args:
        text (str): The input text.
        k (int): The length of the k-mers to find.

    Returns:
        list: A list of the most frequent k-mers in the text.
    """
    from collections import defaultdict

    kmer_counts = defaultdict(int)

    # Count occurrences of each k-mer
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        kmer_counts[kmer] += 1

    # Find the maximum count
    max_count = max(kmer_counts.values())

    # Collect all k-mers with the maximum count
    most_frequent_kmers = [kmer for kmer, count in kmer_counts.items() if count == max_count]

    return most_frequent_kmers


if __name__ == "__main__":

    # with open("dataset_30272_13.txt", "r") as file:
    #     lines = file.readlines()
    #     text = ''.join(lines[:-1]).replace('\n', '').strip()
    #     k = int(lines[-1].strip())
    #     result = frequentKmers(text, k)
    #     print(' '.join(result))
    # Evaluating frequent kmers in Vibrio_cholerae.txt
    with open("Vibrio_cholerae.txt", "r") as file:
        text = file.readlines()
        text = ''.join(text).replace('\n', '').strip()
        k = 9
        result = frequentKmers(text, k) 
        print(' '.join(result))