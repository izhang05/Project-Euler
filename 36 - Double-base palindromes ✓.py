"""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""
solution = 0
def palindrome(x):
  for i in range(1,len(str(x//2))+1):
    i = int(i)
    if str(x)[i-1] != str(x)[-i]:
      return False
  else:
    return True
for i in range(1, 1000000):
  if palindrome(i):
    binary = bin(i)[2:]
    binary = int(binary)
    if palindrome(binary):
      solution += i
else:
  print(solution)
