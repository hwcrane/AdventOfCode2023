from collections import defaultdict
import sys
import numpy as np
from skimage.segmentation import flood_fill

with open(sys.argv[1]) as f:
    input = [list(line.strip()) for line in f.readlines()]

graph = defaultdict(lambda: ((-1, -1), (-1, -1)))

s_loc = (-1, -1)
for i in range(len(input)):
    for j in range(len(input[0])):
        curr = input[i][j]

        if curr == '|':
            graph[(i, j)] = ((i - 1, j), (i + 1, j))
        elif curr == '-':
            graph[(i, j)] = ((i, j - 1), (i, j + 1))
        elif curr == 'L':
            graph[(i, j)] = ((i - 1, j), (i, j + 1))
        elif curr == 'J':
            graph[(i, j)] = ((i - 1, j), (i, j - 1))
        elif curr == '7':
            graph[(i, j)] = ((i + 1, j), (i, j - 1))
        elif curr == 'F':
            graph[(i, j)] = ((i + 1, j), (i, j + 1))
        elif curr == 'S':
            s_loc = (i, j)

# Try going each direction from S,
# if you incounter somewhere you have been before S or reach a dead end, quit
current = s_loc
running = True

current = s_loc

start_moves = []
if (s_loc[0] - 1) >= 0 and s_loc in graph[(s_loc[0] - 1, s_loc[1])]:
    print('north')
    start_moves.append((s_loc[0] - 1, s_loc[1]))
if (s_loc[0] + 1) < len(input) and s_loc in graph[(s_loc[0] + 1, s_loc[1])]:
    print('south')
    start_moves.append((s_loc[0] + 1, s_loc[1]))
if (s_loc[1] - 1) >= 0 and s_loc in graph[(s_loc[0], s_loc[1] - 1)]:
    print('west')
    start_moves.append((s_loc[0], s_loc[1] - 1))
if (s_loc[1] + 1) < len(input[0]) and s_loc in graph[(s_loc[0], s_loc[1] - 1)]:
    print('east')
    start_moves.append((s_loc[0], s_loc[1] + 1))

next = start_moves[0]
path = []

while next != s_loc:
    temp = graph[next][0] if graph[next][1] == current else graph[next][1]
    current = next
    next = temp
    path.append(current)

for i in range(len(input)):
    for j in range(len(input[0])):
        if (i, j) not in path:
            input[i][j] = '.'
input[s_loc[0]][s_loc[1]] = 'S'

scale = 3
new_height = len(input) * scale
new_width = len(input[0]) * scale
scaled_input = np.zeros((new_height, new_width), dtype=int)

pipe_map = {
    '-': np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]),
    '|': np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]),
    'L': np.array([[0, 1, 0], [0, 1, 1], [0, 0, 0]]),
    'J': np.array([[0, 1, 0], [1, 1, 0], [0, 0, 0]]),
    '7': np.array([[0, 0, 0], [1, 1, 0], [0, 1, 0]]),
    'F': np.array([[0, 0, 0], [0, 1, 1], [0, 1, 0]]),
    'S': np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]]),
    '.': np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
}

for i, row in enumerate(input):
    for j, pipe in enumerate(row):
        scaled_input[
            i * scale : (i + 1) * scale, j * scale : (j + 1) * scale
        ] = pipe_map[pipe]

res = flood_fill(scaled_input, (0, 0), 1)
area = 0
for i, row in enumerate(res):
    for j, pipe in enumerate(row):
        if np.all(res[i : (i + 3), j : (j + 3)] == 0):
            area += 1
            res[i : (i + 3), j : (j + 3)] = 1

print(area)
