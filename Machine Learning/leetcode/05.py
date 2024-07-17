def longestPalindrome(s: str) -> str:
    all_ss = set()
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            all_ss.add(s[i:j])
    cl = ""
    for i in all_ss:
        if checkIfPal(i) and len(i) > len(cl):
            cl = i
    return cl

def checkIfPal(s: str) -> bool:
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return checkIfPal(s[1:-2])
    else:
        return False

longestPalindrome("babad")