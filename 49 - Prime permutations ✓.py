import itertools


def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in itertools.permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p


def is_prime(num):
    if num == 2: return True
    if num == 1 or num % 2 == 0: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    else:
        return True


def find_sequence(nums):
    for i in nums:
        for j in nums[(nums.index(i) + 1):]:
            for k in nums[(nums.index(j) + 1):]:
                if (k - j == j - i):
                    return [i, j, k]
    return None


for i in range(10 ** 3, 10 ** 4):
    numbers = list((int("".join(i)) for i in list(unique_permutations(str(i)))))  # all unique permutations of i
    primes = []
    for j in numbers:
        if is_prime(j):
            # num_prime += 1
            primes.append(j)
    sequence = find_sequence(primes)
    if sequence != None:
        if len(str(sequence[0])) == 4 and sequence[0] != 1487 and len(str(sequence[1])) == 4 and len(
                str(sequence[2])) == 4:
            print(str(sequence[0]) + str(sequence[1]) + str(sequence[2]))
            break
