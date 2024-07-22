def is_bigger_as(rom1 = str, rom2 = str) -> bool:
    both = [rom1, rom2]
    for i in range(len(both)):
        if both[i] == "I":
            both[i] = 1
        elif both[i] == "V":
            both[i] = 2
        elif both[i] == "X":
            both[i] = 3
        elif both[i] == "L":
            both[i] = 4
        elif both[i] == "C":
            both[i] = 5
        elif i == "D":
            both[i] = 6
        elif i == "M":
            both[i] = 7
    if both[0] > both[1]:
        return True
    else:
        return False
def add_to_sum(rom) -> int:
    sum = 0
    if rom == "I":
        sum += 1
    elif rom == "V":
        sum += 5
    elif rom == "X":
        sum += 10
    elif rom == "L":
        sum += 50
    elif rom == "C":
        sum += 100
    elif rom == "D":
        sum += 500
    elif rom == "M":
        sum += 1000
    return sum

def int_to_roman(num = int) -> str:
    ans = []
    textnum = str(num)
    a = []
    for i in textnum:
        a.append(int(i))
    a.reverse()
    for i in range(len(a)):
        if i == 0:
            b = "I"
            c = "V"
            d = "X"
        elif i == 1:
            b = "X"
            c = "L"
            d = "C"
        elif i == 2:
            b = "C"
            c = "D"
            d = "M"
        if a[i] == 1:
            ans.append(b)
        elif a[i] == 2:
            ans.append(b + b)
        elif a[i] == 3:
            ans.append(b + b + b)
        elif a[i] == 4:
            ans.append(b + c)
        elif a[i] == 5:
            ans.append(c)
        elif a[i] == 6:
            ans.append(c + b)
        elif a[i] == 7:
            ans.append(c + b + b)
        elif a[i] == 8:
            ans.append(c + b + b + b)
        elif a[i] == 9:
            ans.append(b + d)
    ans.reverse()
    a = ""
    for i in ans:
        a += i
    return a


def roman_to_int(rom = str) -> int:
    a = []
    for i in rom:
        a.append(i)
    a.reverse()
    print(a)
    sum = 0
    jumper = 0
    for i in range(len(a)):
        i = i + jumper
        if i < len(a) - 1:
            if is_bigger_as(a[i], a[i + 1]):
                sum += add_to_sum(a[i]) - add_to_sum(a[i + 1])
                jumper += 1
            else:
                sum += add_to_sum(a[i])
                print("n")
        elif i < len(a):
            sum += add_to_sum(a[i])
            print("n")

    return sum
print(roman_to_int("MMXCVII"))
