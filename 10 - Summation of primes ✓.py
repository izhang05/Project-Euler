"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
solution = 0
num = 1
while num < 2000000:
	for i in range (2, int(num**0.5)+1):
		if num % i == 0 :
			num +=2
			break
	else:
		solution += num
		num += 2
print(solution+1)
