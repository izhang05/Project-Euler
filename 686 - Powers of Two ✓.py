import time

num_to_find = 678910
n = 0
i = 0
second_power = 1
s_time = time.time()

while n < num_to_find:
    i += 1
    second_power = int(str(second_power * 2)[:20])
    # print(i, second_power)
    if str(second_power)[:3] == "123":
        n += 1
        if n % 10000 == 0:
            print(n, i, time.time()-s_time)
print(i)

# 10000 2844275 2.9715499877929688
# 20000 5687686 5.949262857437134
# 30000 8531097 8.946523904800415
# 40000 11374797 11.883785009384155

# 10000 2844275 3.0717999935150146
# 20000 5687005 6.095211029052734
# 30000 8531386 9.091562032699585
# 40000 11373827 12.073277235031128