
def part1_2(population, days):
    ages = [0]*9
    total_fish = len(population)

    # initialize counters for each age
    for fish in population:
        ages[fish] += 1

    # iterate over days
    for i in range(days):
        if i == 80:
            print(f'part1: {total_fish}')

        # get current 0 aged fish
        new_count = ages[0]
        i = 1
        while i < 9:
            # Move all same aged fishes down one
            ages[i-1] = ages[i]
            i+=1

        # add the current aged 0 back to 6
        ages[6] += new_count
        # Add new spawned
        ages[8] = new_count
        # add new to total
        total_fish += new_count
    print(f'total_fish after {days} days: {total_fish}')


def main():
    with open('input.txt') as f:
        population = [int(i) for i in f.readline().split(',')]

    part1_2(population, 256)

if __name__ == '__main__':
    main()
