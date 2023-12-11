import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f.readlines()]

empty_rows = [r for r in range(len(input)) if all(x == '.' for x in input[r])]
empty_cols = [
    c for c in range(len(input[0])) if all(x[c] == '.' for x in input)
]

galaxies = [
    (x, y)
    for y, row in enumerate(input)
    for x, col in enumerate(row)
    if col == '#'
]

new_galaxies = []
y = 0
for idy, row in enumerate(input):
    x = 0
    for idx, col in enumerate(row):
        if col == '#':
            new_galaxies.append((x, y))
        if idx in empty_cols:
            x += 2
        else:
            x += 1
    if idy in empty_rows:
        y += 2
    else:
        y += 1

print(sum((abs(b[0] - a[0]) + abs(b[1] - a[1])) for a, b in combinations(new_galaxies, 2)))
