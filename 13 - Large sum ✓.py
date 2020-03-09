solution = 0
with open("13 - input array", "r") as fin:
	for i in fin.readlines():
		solution += int(i[:11])
print(solution//10**(len(str(solution))-10))