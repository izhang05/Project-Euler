"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""
# names = open("22 names.txt")
# names = names.read()
# names = names.split(",")
names = ["MARY", "PATRICIA", "LINDA", "BARBARA", "ELIZABETH", "JENNIFER", "MARIA"]
names.sort()
solution = 0
for i in names:
	sum = 0
	for j in i:
		if j == "A":
			sum += 1
		if j == "B":
			sum += 2
		if j == "C":
			sum += 3
		if j == "D":
			sum += 4
		if j == "E":
			sum += 5
		if j == "F":
			sum += 6
		if j == "G":
			sum += 7
		if j == "H":
			sum += 8
		if j == "I":
			sum += 9
		if j == "J":
			sum += 10
		if j == "K":
			sum += 11
		if j == "L":
			sum += 12
		if j == "M":
			sum += 13
		if j == "N":
			sum += 14
		if j == "O":
			sum += 15
		if j == "P":
			sum += 16
		if j == "Q":
			sum += 17
		if j == "R":
			sum += 18
		if j == "S":
			sum += 19
		if j == "T":
			sum += 20
		if j == "U":
			sum += 21
		if j == "V":
			sum += 22
		if j == "W":
			sum += 23
		if j == "X":
			sum += 24
		if j == "Y":
			sum += 25
		if j == "Z":
			sum += 26
	solution += sum*(names.index(i)+1)
	print(solution, names.index(i))
print(solution)
