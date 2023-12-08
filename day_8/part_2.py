import sys
import math

with open(sys.argv[1]) as f:
    input = [
        line.strip()
        .replace('=', '')
        .replace('(', '')
        .replace(')', '')
        .replace(',', '')
        .split()
        for line in f.readlines()
    ]

graph = {i[0]: (i[1:]) for i in input[2:]}
path = input[0][0]
curr = [i[0] for i in input[2:] if i[0][2] == 'A']
steps = 0
path_cur = 0

s = []
for c in curr:
    steps = 0
    path_cur = 0
    while c[2] != 'Z':
        if path[path_cur] == 'L':
            c = graph[c][0]
        else:
            c = graph[c][1]

        steps += 1
        path_cur = (path_cur + 1) % len(path)
    s.append(steps)


print(math.lcm(*s))
