"""A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?"""
import time
start_time = time.time()
solution = 0
for i in range(1, 10**7):
  new_num = i
  while True:
    original_num = new_num
    new_num = 0
    for j in range(1, len(str(original_num))+1):
      n = int(str(original_num)[j-1])
      new_num += n**2
    if new_num == 89:
      solution += 1
      break
    if new_num == 1:
      break
print(solution)
print(time.time()-start_time)

import time
start_time = time.time()
solution = 0
yes = [89]
no = [1]
for i in range(1, 10**7):
    new_num = i
    while True:
        original_num = new_num
        new_num = 0
        for j in range(1, len(str(original_num))+1):
          n = int(str(original_num)[j-1])
          new_num += n**2
        if new_num in yes:
          solution += 1
          if i <568 and i not in yes:
              yes.append(i)
          break
        if new_num in no:
          if i <568:
              no.append(i)
          break
print(solution)
print(time.time()-start_time)
