num_prime = 0
a_val = 0
b_val = 0
b_values = []
def prime(num):
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
for i in range(1, 1001):
	if prime(i):
		b_values.append(i)
for a in range(-999, 1000):
	for b in b_values:
		n = 0
		while True:
			n+=1
			quad = n**2 + a*n + b
			if quad<=0 or not prime(quad):
				if n - 1 > num_prime:
					num_prime = n
					a_val = a
					b_val = b
				break
#print(a_val)
#print(b_val)
print(a_val*b_val)
