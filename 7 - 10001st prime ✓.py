"""By listing the first six is_prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th is_prime is 13.

What is the 10 001st is_prime number?"""
count = 0
num = 1
while count < 10001:
  for i in range (2, int(num**0.5)+1):
    if num % i == 0 :
      num +=2
      break
  else:
    count += 1
    num += 2
else:
  print(num-2)
