from collections import defaultdict
import sys

with open(sys.argv[1]) as f:
	input = [line.strip() for line in f.readlines()]

graph = defaultdict(lambda: ((-1, -1), (-1, -1)))

s_loc = (-1, -1)
for i in range(len(input)):
	for j in range(len(input[0])):
		curr = input[i][j]

		if curr == '|':
			graph[(i, j)] = ((i-1, j), (i+1, j))
		elif curr == '-':
			graph[(i, j)] = ((i, j-1), (i, j+1))
		elif curr == 'L':
			graph[(i, j)] = ((i-1, j), (i, j+1))
		elif curr == 'J':
			graph[(i, j)] = ((i-1, j), (i, j-1))
		elif curr == '7':
			graph[(i, j)] = ((i+1, j), (i, j-1))
		elif curr == 'F':
			graph[(i, j)] = ((i+1, j), (i, j+1))
		elif curr == 'S':
			s_loc = (i, j)

# Try going each direction from S, 
# if you incounter somewhere you have been before S or reach a dead end, quit
current = s_loc
running = True

current = s_loc

# next = (s_loc - 1, s_loc)
start_moves = []
if (s_loc[0] - 1) >= 0 and s_loc in graph[(s_loc[0] - 1, s_loc[1])]:
	start_moves.append((s_loc[0] - 1, s_loc[1]))
if (s_loc[0] + 1) < len(input) and s_loc in graph[(s_loc[0] + 1, s_loc[1])]:
	start_moves.append((s_loc[0] + 1, s_loc[1]))
if (s_loc[1] - 1) >= 0 and s_loc in graph[(s_loc[0], s_loc[1] - 1)]:
	start_moves.append((s_loc[0], s_loc[1] - 1))
if (s_loc[1] + 1) < len(input[0]) and s_loc in graph[(s_loc[0], s_loc[1] - 1)]:
	start_moves.append((s_loc[0], s_loc[1] + 1))

if len(start_moves) > 2:
	print("unimplemented")
	exit()

next = start_moves[0]
path = []

while next != s_loc:
	temp = graph[next][0] if graph[next][1] == current else graph[next][1]
	current = next
	next = temp
	path.append(current)

print((len(path) + 1) // 2)

