def lengthOfLongestSubstring(s: str) -> int:
    all_longest = 0
    for i in range(len(s)):
        current_longest = 0
        letters = []
        j = i
        while j < len(s) and s[j] not in letters:
            letters.append(s[j])
            current_longest += 1
            j += 1
        if current_longest > all_longest:
            all_longest = current_longest
    return all_longest

print(lengthOfLongestSubstring("cailbau"))