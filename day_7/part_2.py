from collections import Counter
import sys

value = dict(zip('J23456789TQKA', range(13)))


def score(card):
    if card[0] == 'JJJJJ':
        hand_rank = [
            5,
        ]
    else:
        c = Counter(card[0])
        jokers = c.pop('J', 0)
        hand_rank = sorted(c.values(), reverse=True)
        hand_rank[0] += jokers

    return hand_rank, [value[c] for c in card[0]]


with open(sys.argv[1]) as f:
    input = [line.strip().split() for line in f.readlines()]

print(
    sum(
        int(bid) * (i + 1)
        for i, (_, bid) in enumerate(sorted(input, key=score))
    )
)
