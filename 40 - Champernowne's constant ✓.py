"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
count = 0
solution = 1
tens = 0
for i in range(1, 9999999999999999):
  for j in str(i):
    count+= 1
    if count == 10**tens:
      solution *= int(j)
      tens += 1
  if tens > 6:
    break
print(solution)
