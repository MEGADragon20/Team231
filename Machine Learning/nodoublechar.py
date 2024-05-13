def give_longest_str_in_str_without_repeating_char(text: str):
    currentbest = 0
    currentbestindex = None
    for i in range(len(text)):
        if go_till_end(givestringafter(text, i)) >= currentbest:
            currentbest = go_till_end(givestringafter(text, i))
            currentbestindex = i-1
    remember = []
    ans = ""
    print(currentbestindex)
    for i in givestringafter(text, currentbestindex):
        for j in remember:
            if j == i:
                return ans
        ans += i
    return ans

def go_till_end(text: str):
    remember = []
    for i in range(len(text)):
        for j in remember:
            if j == text[i-1]:
                return i
    return len(text) 

def givestringafter(text: str, index: int):
    t = []
    for i in text:
        t.append(i)
    for i in t:
        if i == index + 1:
            ans = ""
            for i in t:
                ans += i
            return ans
        t.pop(0)
    ans = ""
    for i in t:
        ans += i
    return ans

print(give_longest_str_in_str_without_repeating_char("abcdefgahjajajjhaha"))