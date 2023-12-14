import sys

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f.readlines()]


def transpose(m):
    return map(''.join, zip(*m))


def shift(m):
    for _ in range(100):
        m = map(lambda l: l.replace('.O', 'O.'), m)
    return list(m)


def count_load(m):
    return sum(
        sum(c == 'O' for c in row) * (len(input) - i)
        for i, row in enumerate(m)
    )

print(count_load(transpose(shift(transpose(input)))))
