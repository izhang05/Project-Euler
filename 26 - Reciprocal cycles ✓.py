"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
solution = [0, 0] # solution[0] = number, solution[1] = length of recurring cycle
for i in range(1, 1000):
	remainders_list = []
	dividend = 10
	remainder = dividend % i
	while remainder != 0 and remainder not in remainders_list:
		remainders_list.append(remainder)
		dividend =  (dividend - ((dividend // i)*i)) * 10
		remainder = dividend % i
	current_length = len(remainders_list)
	if current_length > solution[1]:
		solution[0] = i
		solution[1] = current_length
	#print(remainders_list)
print(solution[0])