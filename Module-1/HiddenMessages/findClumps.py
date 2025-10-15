def findClumps(text, k, L, t):
    clumps = set()
    n = len(text)
    for i in range(n - L + 1):
        window = text[i:i + L]
        freq_map = {}
        for j in range(L - k + 1):
            pattern = window[j:j + k]
            if pattern in freq_map:
                freq_map[pattern] += 1
            else:
                freq_map[pattern] = 1
        for pattern, count in freq_map.items():
            if count >= t:
                clumps.add(pattern)
    return clumps

with open(r'E:\Coursera\BioInformatics\Module-1\HiddenMessages\dataset_30274_5.txt','r') as f:
    lines = [line.strip() for line in f.readlines()]
    genome = lines[0]
    k, L, t = map(int, lines[1].split())
    result = findClumps(genome, k, L, t)
    print(' '.join(result))