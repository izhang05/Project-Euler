"""The is_prime factors of 13195 are 5, 7, 13 and 29.

What is the largest is_prime factor of the number 600851475143 ?"""
Num = 600851475143
solution = 2
while solution <= Num:
  if Num % solution != 0:
    solution +=1
  else:
    Num /= solution
print (solution)
