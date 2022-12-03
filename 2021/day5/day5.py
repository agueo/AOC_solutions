#!/usr/bin/python3
from collections import namedtuple

'''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''

Point = namedtuple('Point', 'x y')

def day5(filename: str):
    p1memo = dict()
    p2memo = dict()

    def update_memo(p, m):
        if tmp not in m.keys():
            m[p] = 1
        else:
            m[p] += 1

    with open(filename) as f:
        for line in f:
            p1, p2 = (lambda t1: ( Point(int(t1[0][0]), int(t1[0][1])), Point(int(t1[1][0]), int(t1[1][1])) )) (
                (lambda p1: ( p1[0].split(','), p1[2].split(',') )) (
                    line.strip().split()))

            if p1.x == p2.x:
                if p1.y > p2.y:
                    # do a range for
                    for i in range(p2.y, p1.y+1):
                        tmp = (p1.x, i)
                        update_memo(tmp, p1memo)
                        update_memo(tmp, p2memo)

                elif p2.y > p1.y:
                    for i in range(p1.y, p2.y+1):
                        tmp = (p1.x, i)
                        update_memo(tmp, p1memo)
                        update_memo(tmp, p2memo)

            elif p1.y == p2.y:
                if p1.x >= p2.x:
                    # do a range for
                    for i in range(p2.x, p1.x+1):
                        tmp = (i, p1.y)
                        update_memo(tmp, p1memo)
                        update_memo(tmp, p2memo)
                elif p2.x >= p1.x:
                    for i in range(p1.x, p2.x+1):
                        tmp = (i, p1.y)
                        update_memo(tmp, p1memo)
                        update_memo(tmp, p2memo)
            else:
                # up right
                # 5,5 -> 8,8
                if p1.x < p2.x and p1.y < p2.y:
                    for i, j in zip(range(p1.x, p2.x+1), range(p1.y, p2.y+1)):
                        tmp = (i,j)
                        update_memo(tmp, p2memo)
                # down right
                elif p1.x < p2.x and p2.y < p1.y:
                    # example 5,6 -> 7,4
                    for i, j in zip(range(p1.x, p2.x+1), range(p1.y, p2.y-1, -1)):
                        tmp = (i,j)
                        update_memo(tmp, p2memo)
                # up left
                elif p2.x < p1.x and p1.y < p2.y:
                    # example 9,7 -> 7,9
                    # 9,7 - 8,8, 7,9
                    for i, j in zip(range(p1.x, p2.x-1, -1), range(p1.y, p2.y+1)):
                        tmp = (i,j)
                        update_memo(tmp, p2memo)
                # down left
                elif p2.x < p1.x and p2.y < p1.y:
                    # example: 7,5 -> 5,3
                    # want 7,5 - 6,4, - 5,3
                    # 5,3 - 6,4 - 7,5
                    for i, j in zip(range(p2.x, p1.x+1), range(p2.y, p1.y+1)):
                        tmp = (i,j)
                        update_memo(tmp, p2memo)

    ans1 = sum([1 for num in p1memo.values() if num >= 2], start=0)
    ans2 = sum([1 for num in p2memo.values() if num >= 2], start=0)
    print(ans1)
    print(ans2)


def main(filename='input.txt'):
    day5(filename)

if __name__ == '__main__':
    main('test_input.txt')
