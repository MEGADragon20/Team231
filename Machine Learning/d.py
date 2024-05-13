def give_longest_str_in_str_without_repeating_char(text: str):
    seen = {}
    start = 0
    max_len = 0
    max_substr = ""

    for i, char in enumerate(text):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_substr = text[start:i + 1]
        seen[char] = i

    return max_substr

print(give_longest_str_in_str_without_repeating_char("abcdefgahjajajjhaha"))  # Output: "abcdefg"