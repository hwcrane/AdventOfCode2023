import sys

with open(sys.argv[1]) as f:
    input = [line.strip().split(' ') for line in f.readlines()]
    input = [(m, tuple(map(int, n.split(',')))) for m, n in input]


def count_solutions(maps, nums, current_num=0) -> int:

    if len(maps) == 0:
        if len(nums) == 0 and current_num == 0:
            return 1
        else:
            return 0

    n_solutions = 0
    options = ['.', '#'] if maps[0] == '?' else maps[0]

    for op in options:
        if op == '#':
            n_solutions += count_solutions(maps[1:], nums, current_num + 1)

        else:
            if current_num > 0:
                if nums and nums[0] == current_num:
                    n_solutions += count_solutions(maps[1:], nums[1:])
            else:
                n_solutions += count_solutions(maps[1:], nums)

    return n_solutions


print(sum(count_solutions(m + '.', n) for m, n in input))
