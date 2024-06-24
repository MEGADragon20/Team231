def perm(s: str) -> str:
    a = ""
    for i in range(len(s)):
        a += (s[i] + perm(s.pop[i]))
    return a


def permutation(s: str) -> list:
    pass

print(perm("a"))