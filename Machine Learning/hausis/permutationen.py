def perm(s: str) -> list:
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    answer = []
    for i in range(len(s)):
        k = strWithoutIndex(s, i)
        allPermutatations = perm(k)
        c = addall(s[i], allPermutatations)
        answer.append(c)
    end = []
    for i in answer:
        end.extend(i)
    return end


def addall(s: str, l: list) -> list:
    answer = []
    for i in l:
        if type(i) is not str:
            for j in i:
                a = s + j
                answer.append(a)
        else:
            a = s + i
            answer.append(a)

    return answer

def strWithoutIndex(s: str, i: int) -> str:
    return s[:i] + s[i+1:]
print(perm("hallo"))
print(len(perm("abcd")))
