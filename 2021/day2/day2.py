def part1(data):
    horizontal_pos = 0
    vertical_pos = 0
    for step in data:
     amt = int(step.split()[1])
     if 'down' in step:
      vertical_pos += amt
     elif 'up' in step:
      vertical_pos -= amt
     elif 'forward' in step:
      horizontal_pos += amt

    return horizontal_pos * vertical_pos



def part2(data):
    horizontal_pos = 0
    vertical_pos = 0
    aim = 0
    for step in data:
     amt = int(step.split()[1])
     if 'down' in step:
      aim += amt
     elif 'up' in step:
      aim -= amt
     elif 'forward' in step:
      horizontal_pos += amt
      vertical_pos += aim * amt
    return horizontal_pos * vertical_pos

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [line.strip() for line in f]

    print(part1(data))
    print(part2(data))
