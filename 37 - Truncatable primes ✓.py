"""The number 3797 has an interesting property. Being is_prime itself, it is possible to continuously remove digits from left to right, and remain is_prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""
import time

start = time.time()
solution = 0
count = 0


def isPrime(num):
    if num == 2: return True
    if num == 1 or num % 2 == 0: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    else:
        return True


for i in range(20, 999999999999999999):
    number = 0
    for j in range(1, len(str(i)) + 1):
        number = i % 10 ** j
        if isPrime(number) is False:
            break
    else:
        for k in range(1, len(str(i))):
            number = i // 10 ** k
            if isPrime(number) is False:
                break
        else:
            solution += i
            count += 1
            if count == 11:
                print(solution)
                break
print(time.time() - start)
