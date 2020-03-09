"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""
factorial = 1
x = 1
solution = 0
y = 0
while x<=100:
  factorial *= x
  x+=1
while y >= 0:
  y = len(str(factorial))-1
  solution += (factorial//10**y)
  factorial -= (factorial//10**y)*10**y
  y -= 1
print (solution)
