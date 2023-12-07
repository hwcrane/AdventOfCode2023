from collections import Counter
import sys

value = dict(zip('23456789TJQKA', range(13)))


def score(card):
    return sorted(Counter(card[0]).values(), reverse=True), [
        value[c] for c in card[0]
    ]


with open(sys.argv[1]) as f:
    input = [line.strip().split() for line in f.readlines()]

print(
    sum(
        int(bid) * (i + 1)
        for i, (_, bid) in enumerate(sorted(input, key=score))
    )
)
