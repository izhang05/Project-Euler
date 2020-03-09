"""In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def find_possible_coins(current_value):  # returns all coins less than the required amount to get 2$
    max_value = goal - current_value
    return ([i for i in coins if i <= max_value])


def find_solution(current_amt, current_coin):
    global solution
    if current_amt == goal:
        # print(current_coin)
        solution += 1
    possible_coins = find_possible_coins(current_amt)
    # print(possible_coins, "original")
    if current_coin in possible_coins:
        possible_coins = possible_coins[possible_coins.index(current_coin):]
    else:
        possible_coins = []
    # print(current_amt, possible_coins, current_coin)
    for i in possible_coins:
        current_amt += i
        find_solution(current_amt, i)
        current_amt -= i


goal = 200
solution = 0
find_solution(0, 1)
print(solution)
