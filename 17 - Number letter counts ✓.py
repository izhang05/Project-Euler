"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use o8and" when writing out numbers is in compliance with British usage."""
import time

words ={1:"one", 2:"two", 3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine", 10:"ten", 11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
solution = 0
start = time.time()
for i in range(1, 1000):
	word_num = ""
	if i % 100 == 0: # divisible by 100
		word_num = word_num + words[i//100] + "hundred"
		i = 0
	elif i >= 100: 
		word_num = word_num + words[i//100] + "hundredand"
		i %= 100
	if i > 0:
		if i <= 20 or i % 10 == 0:
			word_num = word_num + words[i]
		elif i > 20:
			word_num = word_num + words[i-i%10] + words[i%10]
	solution += len(word_num)
solution += len("onethousand")
print(solution, (time.time()-start)*1000000)