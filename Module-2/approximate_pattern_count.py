def approximate_pattern_count(text, pattern, max_mismatches):
    """
    Count the number of times the pattern appears in the text with at most max_mismatches mismatches.

    Args:
        text (str): The text to search within.
        pattern (str): The pattern to search for.
        max_mismatches (int): The maximum number of mismatches allowed.

    Returns:
        int: The count of occurrences of the pattern in the text with at most max_mismatches mismatches.
    """
    count = 0
    pattern_length = len(pattern)
    text_length = len(text)

    for i in range(text_length - pattern_length + 1):
        substring = text[i:i + pattern_length]
        mismatches = sum(1 for a, b in zip(substring, pattern) if a != b)
        if mismatches <= max_mismatches:
            count += 1

    return count


if __name__ == "__main__":
    with open('dataset_30278_6.txt', 'r') as file:
        pattern = file.readline().strip()
        text = file.readline().strip()
        max_mismatches = int(file.readline().strip())

        result = approximate_pattern_count(text, pattern, max_mismatches)
        print(result)