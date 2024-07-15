def mergeofsortedlists(l1: list, l2: list) -> list:
    l1 = (l1 + l2).sort()
    return l1