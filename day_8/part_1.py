import sys

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
curr = 'AAA'
steps = 0
path_cur = 0

while curr != 'ZZZ':
    if path[path_cur] == 'L':
        curr = graph[curr][0]
    else:
        curr = graph[curr][1]

    steps += 1
    path_cur = (path_cur + 1) % len(path)
print(steps)
