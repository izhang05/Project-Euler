def is_prime(num):
    if num == 2: return True
    if num == 1 or num % 2 == 0: return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    else:
        return True
def prime_factor(x):  # returns a set of is_prime factors
    factors = set()
    if is_prime(x):
        factors.add(x)
        x = 1
    i = 3
    while x % 2 == 0:
        x /= 2
        factors.add(2)
    while x > 1:
        if is_prime(i):
            while x % i == 0:
                x /= i
                factors.add(i)
        i += 2
    return factors
solution = 2
num_prime = 0
i = 3
while num_prime < 500499:
    if is_prime(i):
        solution *= i
        num_prime += 1
    i += 2
    if num_prime % 10000 == 0:
        print(num_prime)
print(solution % 500500507)