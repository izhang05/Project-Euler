"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""
solution = set([])
def divisors(i, amicableNum2):
    for j in range(1, (i//2)+1):
        if i % j == 0:
            amicableNum2 += j
    return amicableNum2
for i in range(1, 1000):
    amicableNum = 0
    count = 1
    for j in range(1, (i//2)+1):
        if i % j == 0:
            amicableNum += j
    else:
        if i != amicableNum and i == divisors(amicableNum, 0):
            solution.add(i)
            if amicableNum < 1000:
                solution.add(amicableNum)
print(sum(solution))
