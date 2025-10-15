
def approximate_pattern_matching(text, pattern, max_mismatches):

    """
    Find all starting positions where the pattern appears in the text with at most max_mismatches mismatches.

    Args:
        text (str): The text to search within.
        pattern (str): The pattern to search for.
        max_mismatches (int): The maximum number of mismatches allowed.

    Returns:
        list: A list of starting positions (0-based) where the pattern appears in the text with at most max_mismatches mismatches.
    """
    positions = []
    pattern_length = len(pattern)
    text_length = len(text)

    for i in range(text_length - pattern_length + 1):
        substring = text[i:i + pattern_length]
        mismatches = sum(1 for a, b in zip(substring, pattern) if a != b)
        if mismatches <= max_mismatches:
            positions.append(i)

    return positions


if __name__ == "__main__":
    # with open('dataset_30278_4.txt', 'r') as file:
    #     pattern = file.readline().strip()
    #     text = file.readline().strip()
    #     max_mismatches = int(file.readline().strip())

    #     result = approximate_pattern_matching(text, pattern, max_mismatches)
    #     print(" ".join(map(str, result)))

        text = "AACAAGCTGATAAACATTTAAAGAG"
        pattern = "AAAAA"
        max_mismatches = 2
        result = approximate_pattern_matching(text, pattern, max_mismatches)
        print(" ".join(map(str, result)))