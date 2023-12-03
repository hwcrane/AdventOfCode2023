import sys
from typing import DefaultDict

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f.readlines()]

parts = []


def checks(line, index):
    return [
        (line, index - 1),
        (line, index + 1),
        (line - 1, index - 1),
        (line - 1, index),
        (line - 1, index + 1),
        (line + 1, index - 1),
        (line + 1, index),
        (line + 1, index + 1),
    ]


def get_gears(line, start, index):

    gears = set()
    for i in range(start, index):
        [
            gears.add((i, j))
            for i, j in checks(line, i)
            if i < len(input)
            and i > 0
            and j < len(input[0])
            and j > 0
            and input[i][j] == '*'
        ]

    return gears


gears = DefaultDict(lambda: [])
total = 0
for i, line in enumerate(input):
    index = 0
    while index < len(line):
        if line[index].isnumeric():
            start = index
            while (index := index + 1) < len(line) and line[index].isnumeric():
                pass
            adjacent = get_gears(i, start, index)
            for a in adjacent:
                gears[a].append(int(line[start:index]))

        else:
            index += 1


print(sum([g[0] * g[1] for g in gears.values() if len(g) == 2]))
