# https://en.wikipedia.org/wiki/Greatest_common_divisor#greatest_common_denominator
def gcd(a,b):
    if a % b == 0:
        if a > b:
            return b
        if b > a:
            return a
    r = a % b
    gcd(b,r)
    return r

a = int(input())
b = int(input())

print(gcd(a,b))
