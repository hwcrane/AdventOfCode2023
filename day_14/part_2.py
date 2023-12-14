import sys
import tqdm
from functools import cache

with open(sys.argv[1]) as f:
    input = tuple(map(lambda l: l.strip(), f.readlines()))

@cache
def t(m):
    return tuple(map(''.join, zip(*m)))


@cache
def sl(m):
    return tuple(map(lambda l: '#'.join(''.join(sorted(x, reverse=True)) for x in l.split('#')), m))


@cache
def sr(m):
    return tuple(map(lambda l: '#'.join(''.join(sorted(x)) for x in l.split('#')), m))


def count_load(m):
    return sum(
        sum(c == 'O' for c in row) * (len(m) - i)
        for i, row in enumerate(m)
    )


@cache
def cycle(m):
    return sr(t(sr(t(sl(t(sl(t(m))))))))

for i in tqdm.tqdm(range(1_000_000_000), dynamic_ncols=True):
    input = cycle(input)

print(count_load(input))
