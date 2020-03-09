import itertools

def divisible(x, y):
	if x % y == 0:
		return True
	else:
		return False
def combine(x, y, z):
	return (100 * x + 10 * y + z)

upper_limit = 10
numbers = list(itertools.permutations(list(range(upper_limit))))
solution = 0
primes = [0, 2, 3, 5, 7, 11, 13, 17]
for i in numbers:
	for j in range(1, upper_limit - 2):
		if not divisible(combine(i[j], i[j + 1], i[j + 2]), primes[j]):
			break
	else:
		number = ""
		for k in i:
			number = number + str(k)
		solution += int(number)
print(solution)