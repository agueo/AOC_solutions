

def main(filename):
    with open(filename) as f:
        data = [[int(d) for d in line.strip()] for line in f]

    # DFS?
    # part 1 calculate total flashes after 100 cycles
