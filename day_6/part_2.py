import sys

with open(sys.argv[1]) as f:
	input = [line.strip().split() for line in f.readlines()]
time = int(''.join(input[0][1:]))
dist = int(''.join(input[1][1:]))
ways = [i for i in range(1,time) if i * (time - i) > dist]

print(len(ways))
