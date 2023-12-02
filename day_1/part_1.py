import sys

with open(sys.argv[1]) as f:
    input = [
        [l for l in line if l.isnumeric()] for line in f.readlines()
    ]

sum = 0
for line in input:	
	sum+= int(line[0]+line[-1])
print(sum)
