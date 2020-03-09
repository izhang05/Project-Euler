"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also is_prime.

What is the largest n-digit pandigital is_prime that exists?"""


def is_prime(num):
    if num == 1 or num % 2 == 0:
        return False
    if num == 2:
        return True
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        else:
            return True


prime_num = []
for i in range(2143, 987654322):
    if is_prime(i):
        prime_num.append(i)


def pandigital(a):
    a = str(a)
    panlist = []
    for i in a:
        i = int(i)
        if i not in panlist:
            panlist.append(i)
    for j in range(1, len(a) + 1):
        if j not in panlist:
            return False
    else:
        return True


solution = 0
for i in prime_num:
    if pandigital(i):
        solution = i
print(solution)
