import time
start = time.time()
def pandigital(a, b, c):
	a = str(a)
	b = str(b)
	c = str(c)
	if len(a)+len(b)+len(c) != 9:
		return False
	else:
		panlist = []
		for i in a:
			i = int(i)
			if i not in panlist:
				panlist.append(i)
			else:
				return False
				break
		else:
			for i in b:
				i = int(i)
				if i not in panlist:
					panlist.append(i)
				else:
					return False
					break
			else:
				for i in c:
					i = int(i)
					if i not in panlist:
						panlist.append(i)
					else:
						return False
						break
				else:
					for i in range(1, 10):
						if i not in panlist:
							return False
					else:
						return True
solution = set()
for a in range(1, 50):
	for b in range(1, 2000):
		c = a*b
		if pandigital(a, b, c):
			solution.add(c)
print(sum(solution))
print(time.time()-start)