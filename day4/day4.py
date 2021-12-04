#!/usr/bin/python3
import sys
import pprint
from typing import List
from collections import OrderedDict

'''Test input
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''
# to win a board needs to have row or column complete
# numbers get called in batches of 5
# when the last number is called and one board completes the score is calculated as follows
# sum of unmarked squares * the winning number


def get_input(filename: str) -> (List, List):
    ''' get the input string of number && generate all boards '''
    boards = []
    i = 0
    with open(filename) as f:
        numbers = f.readline().strip().split(',')
        # Read empty line
        f.readline()
        board = []
        for line in f:
            b = OrderedDict()
            line = line.strip()
            board.append(b.fromkeys(line.split()))
            i += 1
            if i % 5 == 0:
                # read new empty line
                f.readline()
                boards.append(board)
                board = []
                i = 0
    return numbers, boards


def print_board(board):
    for line in board:
        print(line)

def check_rows(board) -> bool:
    ''' check all rows for win
    return true if won, false otherwise
    '''
    for row in board:
        if all(row.values()):
            return True
    return False


def check_cols(board) -> bool:
    ''' check all columns for win
    return true if won, false otherwise'''
    for i in range(0,5):
        col = []
        for row in board:
            val = list(row.values())[i]
            col.append(val)
        if len(col) == 5 and all(col):
            return True
            print("Won with column")
    return False


def update_board(board, num) -> bool:
    ''' go through each number and update the boards '''
    for row in board:
        if num in row.keys():
            row[num] = True
            if check_rows(board) or check_cols(board):
                return True
            break
    return False

def calc_winner(board: List, num: int) -> int:
    ans = 0
    for row in board:
        for k ,v in row.items():
            if not v:
                print(f'adding {k}')
                ans+=int(k)
    print(f'sum: {ans}')
    return int(num)*ans

def part1(numbers: List, boards: List):
    ''' do part 1 '''

    for i in range(0,len(numbers),5):
        cur_nums = numbers[i:i+5]
        for num in cur_nums:
            for board in boards:
                isWinner = update_board(board, num)
                if isWinner:
                    print("Winning board:")
                    print_board(board)
                    print(f"Winning number: {num}")
                    print(f'Answer: {calc_winner(board, num)}')
                    return

def calc_winner_part2(board: List, win_num: int) -> int:
    ans = 0
    for row in board:
        for k,v in row.items():
            if not v and k != win_num:
                ans+=int(k)
    return int(win_num) * ans

def part2(numbers: List, boards:List) -> int:
    ''' do part 2 '''

    total_boards = len(boards)
    winning_boards = []

    for i in range(0,len(numbers),5):
        cur_nums = numbers[i:i+5]
        for num in cur_nums:
            for board in boards:
                if board in winning_boards:
                    continue

                isWinner = update_board(board, num)
                if isWinner:
                    # Check if this is the last winner
                    if len(winning_boards) == total_boards-1:
                        print(f"last winning number: {num}")
                        print("last board left")
                        print_board(board)
                        print(f'Answer: {calc_winner(board, num)}')
                        return

                    winning_boards.append(board)


def main(filename = 'input.txt'):
    numbers, boards = get_input(filename)
    part1(numbers, boards)
    part2(numbers, boards)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
