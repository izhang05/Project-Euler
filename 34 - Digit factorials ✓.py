"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""
solution = 0
def factorial(x):
    product = 1
    for i in range(1, x+1):
        product *= i
    return product
for i in range (3, 100000):
    sum = 0
    for j in str(i):
        j = int(j)
        sum += factorial(j)
    if sum == i:
        solution += i
print(solution)
