def reverse(self, x: int) -> int:
    if x < -2**31 or x > 2**31 - 1:
        return 0
    return int(str(x)[::-1]) if x >= 0 else -1*int(str(x*-1)[::-1])