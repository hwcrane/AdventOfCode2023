import sys

with open(sys.argv[1]) as f:
	input = [line.strip().split() for line in f.readlines()]
times = list(map(int, input[0][1:]))
distance = list(map(int, input[1][1:]))

total = 1
for time, dist in zip(times, distance):
	ways = [i for i in range(1,time) if i * (time - i) > dist]
	total *= ways[-1] - ways[0] + 1
print(total)

