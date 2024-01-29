import re
from collections import Counter

with open("./Day 7/input-test.txt", "r") as f:
    input = f.read()

card_types = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hand_types = ["5OK", "4OK", "FH", "3OK", "2P", "1P", "HC"]
hand_labels = ["Five of a Kind", "Four of a Kind", "Full House", "Three of a Kind", "Two Pairs", "One Pair", "High Card"]

def extract_hands(input):
    hands = input.strip().split("\n")
    hands = [hand.split(" ") for hand in hands]
    hands = [hand[0] for hand in hands]
    return hands


def find_hand_type(hands):
    hand_types = []

    for hand in hands:
        counts = Counter(hand)
        if 5 in counts.values():
            kind = '5OK'
        elif 4 in counts.values():
            kind = '4OK'
        elif 3 in counts.values() and 2 in counts.values():
            kind = 'FH'
        elif 3 in counts.values():
            kind = '3OK'
        elif list(counts.values()).count(2) == 2:
            kind = '2P'
        elif 2 in counts.values():
            kind = '1P'
        else:
            kind = 'HC'

        hand_types.append((hand, kind))

    hand_types.sort(key=lambda x: x[1])
    return hand_types

def extract_bids(input):
    bids = input.strip().split("\n")
    bids = [bid.split(" ") for bid in bids]
    bids = [bid[1] for bid in bids]
    return bids


def part1(input):
    
    hand= extract_hands(input)
    bids = extract_bids(input)
    hand_type = find_hand_type(hand)
    # print(hand)
    # print(bids)
    print('Types:', hand_type)

    return 0

    





print('Winnings', part1(input))
