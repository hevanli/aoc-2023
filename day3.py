filename = "input3.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def get_neighbors(row, col):
    neighbors = []

    if (row > 0):
        neighbors.append(lines[row-1][col]) # up
    if (row < len(lines)-1):
        neighbors.append(lines[row+1][col]) # down
    if (col > 0):
        neighbors.append(lines[row][col-1]) # left
    if (col < len(lines[0])-1):
        neighbors.append(lines[row][col+1]) # right
    if (row > 0 and col > 0):
        neighbors.append(lines[row-1][col-1]) # top left
    if (row > 0 and col < len(lines[0])-1):
        neighbors.append(lines[row-1][col+1]) # top right
    if (row < len(lines)-1 and col > 0):
        neighbors.append(lines[row+1][col-1]) # bottom left
    if (row < len(lines)-1 and col < len(lines[0])-1):
        neighbors.append(lines[row+1][col+1]) # bottom right

    return neighbors

def part1():
    sum,row = 0,0
    while (row < len(lines)):
        col = 0
        while (col < len(lines[0])):
            if (lines[row][col].isdigit()):
                part_num, is_part_num = "", False

                while (col < len(lines[0]) and lines[row][col].isdigit()):
                    part_num += lines[row][col]
                    neighbors = get_neighbors(row, col)
                    for neighbor in neighbors:
                        if (not neighbor.isdigit() and not neighbor == "."):
                            is_part_num = True
                    col += 1

                if (is_part_num):
                    sum += (int)(part_num)
            else:
                col += 1
        row += 1
    return sum

def part2():
    sum, row = 0,0
    while (row < len(lines)):
        col = 0
        while (col < len(lines[0])):
            if(lines[row][col] == "*"):
                neighbors = get_neighbors(row, col)


print(part1())
