import sys

with open(sys.argv[1]) as f:
    input = [
        line.strip()
        .replace('one', 'one1one')
        .replace('two', 'two2two')
        .replace('three', 'three3three')
        .replace('four', 'four4four')
        .replace('five', 'five5five')
        .replace('six', 'six6six')
        .replace('seven', 'seven7seven')
        .replace('eight', 'eight8eight')
        .replace('nine', 'nine9nine')
        for line in f.readlines()
    ]

sum = 0
for line in input:
    line = ''.join(filter(lambda s: s.isnumeric(), line))
    sum += int(line[0] + line[-1])
print(sum)
