import sys

with open(sys.argv[1]) as f:
	input = [(i, line.strip()[line.index(':')+2:].replace("|", "").split()) for i, line in enumerate(f.readlines())]

n = len(input)
total = 0
for line in input:
	winning = (len(line[1]) - len(set(line[1])))
	for i in range(line[0] + 1, line[0] + 1 + winning):
		if i < n:
			input.append(input[i])
print(len(input))
