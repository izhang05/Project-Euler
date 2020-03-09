"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
def prime_fact(num):
	factorization = {}
	while num % 2 == 0:
		if 2 not in factorization:
			factorization[2] = 1
		else:
			factorization[2] += 1
		num /= 2
	divisor = 3
	while num > 1:
		if num % divisor == 0:
			num /= divisor
			if divisor not in factorization:
				factorization[divisor] = 1
			else:
				factorization[divisor] += 1
		else:
			divisor += 2
	return factorization
prime_factors = {}
for i in range(1, 21):
	i_fact = prime_fact(i)
	for j in i_fact:
		if j not in prime_factors:
			prime_factors[j] = 1
		elif i_fact[j] > prime_factors[j]:
			prime_factors[j] = i_fact[j]
solution = 1
for key, value in prime_factors.items():
	solution *= key**value
print(solution)