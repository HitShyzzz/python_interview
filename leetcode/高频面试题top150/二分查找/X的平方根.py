from self import self


def mySqrt(self, x: int) -> int:
    l = 1
    r = x
    while l <= r:
        mid = (l + r) // 2
        if mid == l or mid * mid == x:
            return mid
        elif mid * mid < x:
            l = mid
        elif mid * mid > x:
            r = mid
    return 0


print(mySqrt(self, 16))
