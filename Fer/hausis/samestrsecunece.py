def gothrogheverysecuence(text: str) -> list:
    def givestruntil(text: str, end: int) -> str:
        ans = ""
        i = 0
        while i < end and i < len(text):
            ans += text[i]
            i += 1
        return ans
    
    def givestrafter(text:str, start: int) -> str:
        if start >= 0:
            ans = ""
            i = len(text) - 1
            while start <= i:
                ans += text[i]
                i -= 1
            return turnaroundstr(ans)
        return None
    
    def turnaroundstr(text:str) -> str:
        ans = ""
        for i in text:
            ans = i + ans
        return ans

    ans = []
    for i in range(len(text)):
        current = givestrafter(text, i)
        for j in range(len(text)):
            if current is not None:
                if j >= i:
                    curry = givestruntil(current, j)
                    if curry is not None:
                        ans.append(curry)
    checkans = []
    for i in ans:
        if i != "" and i not in checkans:
            checkans.append(i)
    checkans.append(text)
    return checkans

def samestrsecuence(text1:str, text2: str) -> str:
    ans = ""
    list1 = gothrogheverysecuence(text1)
    list2 = gothrogheverysecuence(text2)
    for i in list1:
        for j in list2:
            if i == j and len(i) > len(ans):
                ans = i
    return ans

print(samestrsecuence("lernen", "adler"))