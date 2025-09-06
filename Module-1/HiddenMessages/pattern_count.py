def pattern_count(text, pattern):
    count = 0
    pattern_length = len(pattern)
    text_length = len(text)
    
    for i in range(text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            count += 1
            
    return count


# Example usage:
# text = "GCGCG"
# pattern = "GCG"
# print(pattern_count(text, pattern))  # Output: 2

if __name__ == "__main__":
    with open("dataset_30272_6.txt", "r") as file:
        lines = file.readlines()
        text = ''.join(lines[:-1]).replace('\n', '').strip()
        pattern = lines[-1].strip()
        result = pattern_count(text, pattern)
        print(result)