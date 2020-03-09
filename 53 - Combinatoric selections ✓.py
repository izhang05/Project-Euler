import time
start = time.time()
solution = 0
def fac(x):
	solution = 1
	for i in range(2, x+1):
		solution *= i
	return solution
def comb(n, r):
	return int(fac(n)/(fac(r)*fac(n-r)))
for n in range(1, 101):
	for r in range(1, n):
		if comb(n, r) > 10**6:
			solution += 1
print(solution)
print(time.time()-start)