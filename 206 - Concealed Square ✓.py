"""Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit."""
import time

start = time.time()

# def satisfies(num):
#     num = str(num)
#     for i in range(9):
#         if num[i *2] != str(i + 1):
#             return False
#     if num[18] == "0":
#         return True
#     return False
#
#
# for i in range(1010101010, 1389026624, 10):
#     if satisfies(i ** 2):
#         print(i)
#         print(time.time() - start)
#         break
#     if i % 1000000 == 0:
#         print(i, time.time() - start)

for i in range(int(1E8), int(1.4E8)):
    if (i % 10 != 3 and i % 10 != 7):
        continue
    if (i % 1000000 == 0):
        print(i)
    n = i * i
    s = True
    for j in range(9):
        if n % 10 != 9 - j:
            s = False
            break
        n = n // 100
    if s:
        print(str(i) + "0", time.time() - start)
        break
