from typing import List

open_list = ['(', '{', '[', '<']
close_list = [')', '}', ']', '>']

def check_line(line)->(bool, [List,str]):
    ''' check if a line is incomplete, corrupt, if corrupt return false and illegal char, if incomplete return true and no char'''
    stack = []
    for b in line:
        if b in open_list:
            stack.append(b)

        elif b in close_list:
            if len(stack) > 0:
                pos = close_list.index(b)
                # if last item is not the same one we're expecting it is corrupt
                if stack[-1] != open_list[pos]:
                    return (False, b)
                stack.pop()
            else:
                return (True, '')
    if len(stack) > 0:
        return (True, stack)


def main(filename):
    with open(filename) as f:
        data = [line.strip() for line in f]


    p1_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    p2_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    p1_total_points = 0
    p2_total_points = []

    for line in data:
        incomplete, illegal_char = check_line(line)
        if not incomplete:
            p1_total_points += p1_points[illegal_char]
        else:
            total_points=0
            while(len(illegal_char)):
                total_points *= 5
                total_points += p2_points[
                    close_list[
                        open_list.index(
                            illegal_char.pop(-1))]]
            p2_total_points.append(total_points)

    print(p1_total_points)
    print(sorted(p2_total_points)[len(p2_total_points)//2])


if __name__ == '__main__':
    main('input.txt')
