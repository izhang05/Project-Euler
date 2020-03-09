import time

start_time = time.time()


def find_solution(current_sum, current_coin):
    global solution
    if current_sum == goal:
        solution += 1
    for i in range(current_coin, goal - current_sum + 1):  # starts from current_coin(no repeats!!)
        current_sum += i
        find_solution(current_sum, i)
        current_sum -= i


goal = 100
solution = 0
find_solution(0, 1)
solution -= 1
print(solution)
print(time.time() - start_time)
