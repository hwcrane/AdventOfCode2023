import sys


def differences(arr):
    return [arr[i] - arr[i - 1] for i in range(1, len(arr))]


with open(sys.argv[1]) as f:
    input = [list(map(int, line.strip().split())) for line in f.readlines()]

sum = 0
for line in input:
    diffs = [line]
    diff = differences(line)
    while any(n != 0 for n in diff):
        diffs.append(diff)
        diff = differences(diff)

    new_vals = [0]
    for i in range(1, len(diffs) + 1):
        new_vals.append(diffs[-i][0] - new_vals[-1])
    sum += new_vals[-1]

print(sum)
