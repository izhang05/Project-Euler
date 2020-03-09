import math
from fractions import Fraction


def cancels(numer, denom):
    num = Fraction(numer, denom)
    numer = str(numer)
    denom = str(denom)
    for i in range(2):
        for j in range(2):
            if numer[i] == denom[j] and Fraction(int(numer[1 - i]), int(denom[1 - j])) == num:
                return True
    return False


solution = 1
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        if numerator % 10 != 0 and denominator % 10 != 0 and numerator % 11 != 0 and denominator % 11 != 0 and cancels(numerator, denominator):
            solution *= Fraction(numerator, denominator)
print(solution.denominator)