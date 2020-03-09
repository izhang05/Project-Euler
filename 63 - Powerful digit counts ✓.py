count = 0
for num in range(1, 10):
    power = 1
    num_length = len(str(num ** power))
    while num_length >= power:
        if num_length == power:
            count += 1
            print(num, power, num ** power, )
        power += 1
        num_length = len(str(num ** power))
print(count)