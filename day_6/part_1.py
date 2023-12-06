import sys
from functools import reduce

print(
    reduce(
        lambda acc, vals: acc * (vals[-1] - vals[0] + 1),
        [
            [i for i in range(1, time) if i * (time - i) > dist]
            for time, dist in zip(
                *[
                    list(map(int, line.strip().split()[1:]))
                    for line in open(sys.argv[1]).readlines()
                ]
            )
        ],
        1,
    )
)
