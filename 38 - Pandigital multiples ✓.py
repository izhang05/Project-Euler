import time
start = time.time()
solution = 0
def pan(x):
	if set(x) == set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
		return True
	else:
		return False
for i in range(1, 10000):#The concatenated product of 10000 and (1,2) would be 10 digits which means that 9999 is the upper limit.
	multiple = str(i)
	for j in range(2, 10):
		multiple = multiple + str(j*i)
		if len(multiple)==9:
			if pan(multiple):
				if int(multiple) > solution:
					solution = int(multiple)
		if len(multiple)>9:
			break
print(solution)
print(time.time()-start)