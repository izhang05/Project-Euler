"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""
solution = 0
for i in range(100, 10000):
	for j in range(100, 10000):
		num = str(i*j)
		if len(num) == 8:
			if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
				if int(num) > solution:
					solution = int(num)
print(solution)