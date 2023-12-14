import sys

with open(sys.argv[1]) as f:
    input = [line.strip().split() for line in f.read().split('\n\n')]


def get_mirror(case):
    for i in range(len(case) - 1):
        pairs = [
            c1 == c2
            for r1, r2 in zip(case[i::-1], case[i + 1 :])
            for c1, c2 in zip(r1, r2)
        ]
        if sum(pairs) == len(pairs) - 1:
            return i + 1


def solve(case):
    row = get_mirror(case)
    if row:
        return row * 100
    case = list(zip(*case))
    return get_mirror(case)


total = 0
for case in input:
    total += solve(case)


print(total)
