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
solution = 0
i = 2
while solution < 1000000:
	if is_prime(i):
		solution += i
	if solution > 1000000:
		solution -= i 
		break
	elif i == 2:
		i+= 1
	else:
		i+=2
i = 2
while True:
	if is_prime(solution):
		print(solution)
		break
	else:
		if is_prime(i):
			solution -= i
	if i == 2:
		i+= 1
	else:
		i+= 2