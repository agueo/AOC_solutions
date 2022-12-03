
example_file = "example.txt"
input1_file = "input1.txt"
input2_file = "input2.txt"

def day1():
    '''Find the sum of the error items'''
    data = []
    with open(input1_file) as file:
        data = [line.strip() for line in file.readlines()]
    
    # priorities for a-z are 1-26
    # ascii a is 97 
    # priorities for A-Z are 27-52
    # ascii A is 65  - 38 diff
    errors = []

    for rucksack in data:
        midpoint = int(len(rucksack) / 2)
        left = set(rucksack[0:midpoint])
        right = set(rucksack[midpoint:])
        # do an intersection to find the dup item
        item = left.intersection(right).pop()
        #print(item)
        if item.islower():
            errors.append(ord(item) - 96)
        else:
            errors.append(ord(item) - 38)

    print(sum(errors))

def day2():
    '''Find the sum of the badge items'''
    data = []
    with open(input2_file) as file:
        data = [line.strip() for line in file.readlines()]
    
    # priorities for a-z are 1-26
    # ascii a is 97 
    # priorities for A-Z are 27-52
    # ascii A is 65  - 38 diff
    badges = []

    for group in range(3, len(data)+1, 3):
        first, second, third = data[group-3:group]
        first = set(first)
        second = set(second)
        third = set(third)
        # do an intersection to find the dup item
        item = (first & second & third).pop()
        # print(item)
        if item.islower():
            badges.append(ord(item) - 96)
        else:
            badges.append(ord(item) - 38)

    print(sum(badges))


def main():
    day1()
    day2()


if __name__ == '__main__':
    main()