import time
start = time.time()
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
num = 1
num_prime = 0
non_prime = 1
i = 2
while True:
	for j in range(4):
		num += i
		if is_prime(num):
			num_prime += 1
		else:
			non_prime += 1
	if num_prime/(num_prime+non_prime) < 0.1 :
		solution = i+1
		break
	i += 2
print(solution)
print(time.time()-start)