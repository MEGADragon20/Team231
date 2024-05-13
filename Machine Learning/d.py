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

# Auf den 13.05.2024 als Hausaufgabe:


# Schreibe eine Funktion substring_suche_2(string1: str, string2: str) -> str, die den längsten gemeinsamen Substring der beiden übergebenen Strings sucht und zurückgibt.
# Schreibe die Funktion so effizient wie möglich.
# Beispiel: substring_suche_2("adler", "lernen") == "ler"

# TODO