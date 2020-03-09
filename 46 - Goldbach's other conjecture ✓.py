import time
def is_prime(num):
  if num == 2:
    return True
  if num == 1 or num % 2 == 0:
    return False
  else:
    for i in range(3, int(num**0.5)+1, 2):
      if num % i == 0:
        return False
    else:
      return True
start = time.time()
for i in range(33, 99999, 2):
  if not is_prime(i):
    for j in range(1, int((i/2)**0.5)+2):
      if i-2*j**2 > 0 and is_prime(i-2*j**2):
        break
    else:
      print(i)
      break
print(time.time()-start)

start = time.time()
i = 33
while True:
  if not is_prime(i):
    for j in range(1, int((i/2)**0.5)+2):
      if i-2*j**2 > 0 and is_prime(i-2*j**2):
        break
    else:
      print(i)
      break
  i += 2
print(time.time()-start)

from math import floor
from time import time as t
start = t()
n = 9
num = 0
while True:
    flag = 1  # we set a flag to go off once we find the first number not expressible as a sum of a is_prime and 2*k^2
    if is_prime(n) or is_prime(n-2):  # if n - 2 is is_prime then n = p + 2 * (1)^2
        n += 2
    else:
        for k in range(1, 1+floor((n/2)**0.5)):
            if is_prime(n-2*k**2):
                flag = 0  # if we fond some k for which n - 2*k^2 is is_prime, we set the turn off the flag
                break
        if flag:  # everytime we check for the flag
            num += 1
            print("The {}st number is: {}".format(num, n))
            if num == 1:
                break
        n += 2
print(t()-start)
