''' day 9 solution '''

def check_top(data, i, j):
    if i == 0:
        return True
    if data[i-1][j] > data[i][j]:
        return True
    return False

def check_bottom(data, i, j):
    if i == len(data)-1:
        return True
    if data[i+1][j] > data[i][j]:
        return True
    return False

def check_left(data, i, j):
    if j == 0:
        return True
    if data[i][j-1] > data[i][j]:
        return True
    return False

def check_right(data, i, j):
    if j == len(data[i])-1:
        return True
    if data[i][j+1] > data[i][j]:
        return True
    return False

def check_up(data, i, j):
    # if not the top or if up is < 9
    if i == 0:
        return False
    point = data[i-1][j]
    if point < 9 and point != -1:
        return True
    return False

def check_down(data, i, j):
    # if not the top or if up is < 9
    if i == len(data)-1:
        return False
    point = data[i+1][j]
    if point < 9 and point != -1:
        return True
    return False

def check_lt(data, i, j):
    if j == 0:
        return False
    point = data[i][j-1]
    if point < 9 and point != -1:
        return True
    return False

def check_rt(data, i, j):
    if j == len(data[i])-1:
        return False

    point = data[i][j+1]
    if point < 9 and point != -1:
        return True
    return False

def main(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append([int(i) for i in line.strip()])

    # part 1
    lowest = []
    for i,row in enumerate(data):
        for j, point in enumerate(row):
            if all([
                check_top(data,i,j),
                check_bottom(data,i,j),
                check_left(data,i,j),
                check_right(data,i,j)]
            ):
                lowest.append(point)
    risk = sum(map(lambda x: x+1, lowest))
    print(risk)

    # part 2
    basins = []
    queue = []
    count = 0
    for i,row in enumerate(data):
        for j, point in enumerate(row):
            if point < 9 and point != -1:
                count = 1
                # append the current point
                queue.append((i,j))
                while len(queue) > 0:
                    row,col = queue.pop(0)
                    data[row][col] = -1

                    if check_up(data,row,col):
                        queue.append((row-1,col))
                        data[row-1][col] = -1
                        count += 1
                    if check_down(data, row, col):
                        queue.append((row+1, col))
                        data[row+1][col] = -1
                        count += 1
                    if check_lt(data, row, col):
                        queue.append((row, col-1))
                        data[row][col-1] = -1
                        count += 1
                    if check_rt(data, row, col):
                        queue.append((row, col+1))
                        data[row][col+1] = -1
                        count += 1
                basins.append(count)
                count = 0


    basins = sorted(basins, reverse=True)
    print(basins[0]*basins[1]*basins[2])

if __name__== '__main__':
    main('input.txt')
