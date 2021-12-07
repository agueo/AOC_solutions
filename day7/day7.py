from statistics import mean, median, mode
from math import ceil

if __name__=='__main__':
    with open('input.txt') as f:
        data = sorted([int(i) for i in f.read().strip().split(',')])

    # part 1
    m = int(median(data))
    total = sum(map(lambda x: abs(m-x), data))
    print(f'part1: {total}')

    # part 2
    def calc_fuel_at_pos(pos, fishes):
        p2total = 0
        memo = {}
        for fish in fishes:
            dist = abs(pos-fish)
            if dist in memo:
                p2total += memo[dist]
                continue
            count = (dist+1) * dist // 2  # sum([i for i in range(dist+1)])
            memo[dist] = count
            p2total += count
        # print(f'pos{pos} - {memo} - {p2total}')
        return p2total

    max_val = max(data)
    p2total = min((calc_fuel_at_pos(i, data) for i in range(max_val+1)))

    print(f'part2: {p2total}')

