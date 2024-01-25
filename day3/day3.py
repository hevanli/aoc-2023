filename = "input3.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def get_neighbors(row, col):
    neighbors = {}

    if row > 0:
        neighbors.update({lines[row-1][col]:(row-1, col)}) # up
    if row < len(lines)-1:
        neighbors.update({lines[row+1][col]:(row+1, col)}) # down
    if col > 0:
        neighbors.update({lines[row][col-1]:(row, col-1)}) # left
    if col < len(lines[0])-1:
        neighbors.update({lines[row][col+1]:(row, col+1)}) # right
    if row > 0 and col > 0:
        neighbors.update({lines[row-1][col-1]:(row-1, col-1)}) # top left
    if row > 0 and col < len(lines[0])-1:
        neighbors.update({lines[row-1][col+1]:(row-1, col+1)}) # top right
    if row < len(lines)-1 and col > 0:
        neighbors.update({lines[row+1][col-1]:(row+1, col-1)}) # bottom left
    if row < len(lines)-1 and col < len(lines[0])-1:
        neighbors.update({lines[row+1][col+1]:(row+1, col+1)}) # bottom right

    return neighbors

def part1():
    sum,row = 0,0
    while (row < len(lines)):
        col = 0
        while (col < len(lines[0])):
            if lines[row][col].isdigit():
                part_num, is_part_num = "", False

                while (col < len(lines[0]) and lines[row][col].isdigit()):
                    part_num += lines[row][col]
                    neighbors = get_neighbors(row, col)
                    for neighbor in neighbors:
                        if (not neighbor.isdigit() and not neighbor == "."):
                            is_part_num = True
                    col += 1

                if is_part_num:
                    sum += int(part_num)
            else:
                col += 1
        row += 1
    return sum

def part2():
    sum,row = 0,0
    gears = {}

    while (row < len(lines)):
        col = 0
        while (col < len(lines[0])):
            if lines[row][col].isdigit():
                part_num = ""
                gear_positions = []

                while (col < len(lines[0]) and lines[row][col].isdigit()):
                    part_num += lines[row][col]
                    neighbors = get_neighbors(row, col)
                    for neighbor in neighbors.keys():
                        if neighbor == "*":
                            gear_positions.append(neighbors[neighbor])
                    col += 1

                gear_positions = list(set(gear_positions))
                for gear in gear_positions:
                    if gear in gears:
                        gears[gear].append(int(part_num))
                    else:
                        gears.update({gear:[int(part_num)]})
            else:
                col += 1

        row += 1

    for gear in gears:
        if len(gears[gear]) == 2:
            sum += gears[gear][0] * gears[gear][1]
    return sum

print(part2())
