import sys
from functools import reduce


with open(sys.argv[1]) as f:
	input = [line.strip().split(": ")[1] for line in f.readlines()]

total = 0

for i, line in enumerate(input):
	bag = {'blue': 0, 'red': 0, 'green': 0}
	rounds = line.split('; ')
	for round in rounds:
		grabs = round.split(', ')
		for grab in grabs:
			n, colour = grab.split()
			bag[colour] = n if (n := int(n)) > bag[colour] else bag[colour]
	power = bag['red'] * bag['blue'] * bag['green']
	total += power
print(total)

