import sys

with open(sys.argv[1]) as f:
	input = [line.strip()[line.index(':')+2:].replace("|", "").split() for line in f.readlines()]

total = 0
for line in input:
	winning = (len(line) - len(set(line)))
	if winning:
		total += 2**(winning - 1)
print(total)
