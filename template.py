import sys

with open(sys.argv[1]) as f:
	input = [line.strip() for line in f.readlines()]
print(input)
