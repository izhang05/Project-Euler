"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
import time 
import math

abundant_nums =[]
abundant_num_sums = set()

def divisors_sum(num):
	divisors = 1
	for i in range(2 , int(math.sqrt(num))+ 1):
		if num % i == 0:
			divisors += i
			if i ** 2 != num:
				divisors += num // i
	return divisors

start = time.time()

for i in range(2, 28124, 2):
	if divisors_sum(i)>i:
		abundant_nums.append(i)
for i in range(945, 28124, 10):
	if divisors_sum(i)>i:
		abundant_nums.append(i)

for i in abundant_nums:
	for j in abundant_nums:
		if i + j > 28123:
			# print(i, j)
			break
		abundant_num_sums.add(i + j)
solution =sum(set(range(1, 28124)) - abundant_num_sums)
print(solution)

print(time.time()-start)