from functools import cmp_to_key

filename = "input7.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def hand_strength(hand) -> int:
    # initializing stuff
    hand_dict= {}
    for card in hand:
        if card not in hand_dict: hand_dict.update({card: 1})
        else: hand_dict[card] += 1
    max_card_count = max(hand_dict.values())
    
    # determining hand strength
    num_unique = len(hand_dict)
    if num_unique == 5: return 1 # high card
    elif num_unique == 4: return 2 # one pair
    elif num_unique == 3: # two pair or set
        if max_card_count == 2: return 3 # two pair
        elif max_card_count == 3: return 4 # set
    elif num_unique == 2: # quads, boat
        if max_card_count == 3: return 5 # boat
        elif max_card_count == 4: return 6 # quads
    elif num_unique == 1: return 7 # five of a kind

    return 0

def cmp_hands(hand1: tuple[str, int], hand2: tuple[str, int]) -> int:
    hand_1 = [card for card in hand1[0]]
    hand_2 = [card for card in hand2[0]]
    cards = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
            }

    strength1 = hand_strength(hand_1)
    strength2 = hand_strength(hand_2)
    if strength1 > strength2: return 1
    elif strength2 > strength1: return -1
    else:
        for i in range(len(hand_1)):
            if cards[hand_1[i]] > cards[hand_2[i]]: 
                return 1
            elif cards[hand_2[i]] > cards[hand_1[i]]:
                return -1
    return 0

def part1():
    hands = []
    for line in lines:
        hand = line.split()
        hands.append((hand[0], int(hand[1])))
    hands.sort(key=cmp_to_key(cmp_hands))

    sum = 0
    for i,hand in reversed(list(enumerate(hands))):
        sum += (i + 1) * hand[1]
    print(sum)


def part2():
    return

part1()
