with open("54 - poker_hands_data.txt", "r") as fin:
    fin = fin.readlines()
    player1 = [i.split()[:5] for i in fin]
    player2 = [i.split()[5:] for i in fin]


def determine_hand(hand):  # returns XYYZZ. ZZ = highest card, X = rank, YY = highest card of rank
    hand_nums = [i[0] for i in hand]
    for i in range(5):
        card = hand_nums[i]
        if card == "T":
            hand_nums[i] = 10
        elif card == "J":
            hand_nums[i] = 11
        elif card == "Q":
            hand_nums[i] = 12
        elif card == "K":
            hand_nums[i] = 13
        elif card == "A":
            hand_nums[i] = 14
        else:
            hand_nums[i] = int(card)
    hand_nums = sorted(hand_nums)

    max_card = hand_nums[-1]
    flush = False
    straight = True
    previous = hand_nums[0]
    for i in range(1, 5):
        if hand_nums[i] != previous + 1:
            straight = False
            break
        previous = hand_nums[i]

    suit = hand[0][1]
    for i in hand[1:]:
        if i[1] != suit:
            break
    else:
        flush = True

    if straight and flush and max_card == 14:  # Royal Flush
        return max_card + 91400
    elif straight and flush:  # Straight Flush
        return max_card + max_card * 100 + 8 * 10 ** 4
    for i in [1, 0]:  # Four of a Kind
        if hand_nums[i] == hand_nums[i + 3]:
            return hand_nums[i - 1] + hand_nums[i] * 100 + 7 * 10 ** 4
    for i in [3, 2]:  # Full House
        if hand_nums[i] == max_card and hand_nums[i - 1] == hand_nums[0]:
            high_card = hand_nums[-1] if i == 3 else hand_nums[0]
            return high_card + hand_nums[2] * 100 + 6 * 10 ** 4
    if flush:  # Flush
        return max_card + max_card * 100 + 5 * 10 ** 4
    if straight:  # Straight
        return max_card + max_card * 100 + 4 * 10 ** 4
    for i in [2, 1, 0]:  # Three of a Kind
        if hand_nums[i] == hand_nums[i + 2]:
            return hand_nums[i - 1] + hand_nums[i] * 100 + 3 * 10 ** 4

    pair = 0
    for i in [3, 2, 1, 0]:  # Two Pairs
        if hand_nums[i] == hand_nums[i + 1]:
            if pair == 0:
                pair = hand_nums[i]
            else:
                num = hand_nums[i]
                hand_nums = [i for i in hand_nums if i != pair and i != num]
                return hand_nums[0] + pair * 100 + 2 * 10 ** 4
    if pair != 0:  # Pair
        hand_nums = [i for i in hand_nums if i != pair]
        return hand_nums[-1] + pair * 100 + 10 ** 4
    return max_card + max_card * 100

solution = 0
for i in range(len(player1)):
    # print(determine_hand(player1[i]), determine_hand(player2[i]))
    if determine_hand(player1[i]) > determine_hand(player2[i]):
        solution += 1
print(solution)
