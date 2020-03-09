solution = 0
for a in range(1, 100):
    for b in range(1, 100):
        num = sum(int(i) for i in str(a ** b))
        if num > solution:
            solution = num
print(solution)
