import sys
from functools import reduce

with open(sys.argv[1]) as f:
	seeds, *maps = f.read().strip().split('\n\n')

def match(n, maps):
	ranges = maps.split("\n")[1::]
	for r in ranges:
		destination, source, step = map(int, r.split())
		if source <= n < source + step:
			return n - source + destination
	else:
		return n

print([(seed, reduce(match, maps, int(seed))) for seed in seeds.split()[1:]])
