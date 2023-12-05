import sys
from functools import reduce

with open(sys.argv[1]) as f:
    seeds, *maps = f.read().strip().split('\n\n')

def reverse_match(n, maps):
    for r in maps:
        destination, source, step = r[0], r[1], r[2]
        if destination <= n < destination + step:
            return n - destination + source
    else:
        return n


seeds = list(map(int, seeds.split()[1::]))
maps = [[[int(i) for i in n.split()] for n in r.split('\n')[1::]] for r in maps]
position = 0
while True:
    seed = reduce(reverse_match, maps[::-1], position)
    if any(
        seeds[i] <= seed <= seeds[i] + seeds[i + 1]
        for i in range(0, len(seeds), 2)
    ):
        break
    position += 1

print(position)
