import sys

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f.readlines()]

parts = []


def check(line, index):
    checks = [
        (line, index-1),
        (line, index+1),
        (line-1, index-1),
        (line-1, index),
        (line-1, index + 1),
        (line+1, index -1),
        (line+1, index),
        (line+1, index+ 1),
    ]
    return any(
        [
            not input[i][j].isnumeric() and input[i][j] != '.'
            for i, j in checks
            if i < len(input) and i > 0 and j < len(input[0]) and j > 0
        ]
    )


total = 0 
for i, line in enumerate(input):
    index = 0
    while index < len(line):
        if line[index].isnumeric():
            isPart = check(i, index)
            start = index
            while (index := index + 1) < len(line) and line[index].isnumeric():
                isPart = isPart or check(i, index)
            if isPart:
                total += int(line[start:index])

        else:
            index += 1


print(total)
