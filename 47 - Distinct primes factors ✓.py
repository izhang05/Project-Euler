"""The first two consecutive numbers to have two distinct is_prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct is_prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct is_prime factors each. What is the first of these numbers?"""
def is_prime(num):
	if num == 2: return True
	if num == 1 or num % 2 == 0: return False
	for i in range(3, int(num**0.5)+1, 2):
		if num % i == 0:
			return False
	else:
		return True
def prime_factor(x):  # returns a set of is_prime factors
	factors = set()
	if is_prime(x):
		factors.add(x)
		x = 1
	i = 3
	while x % 2 == 0:
		x /= 2
		factors.add(2)
	while x > 1:
		if is_prime(i):
			while x % i == 0:
				x /= i
				factors.add(i)
		i += 2
	return factors
def diff(x, y, z):
	if (x - y == x) & (y - x == y):# & (z - x == z):
		return True
	else:
		return False

num_integers = 4

num_consecutive = 0
i = 1
while num_consecutive != num_integers:
	if len(prime_factor(i)) == num_integers:
		num_consecutive += 1
	else:
		num_consecutive = 0
	i += 1
print(i - num_integers)
