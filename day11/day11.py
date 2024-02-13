def parse(filename: str) -> list[str]:
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def part1(filename: str) -> None:
    lines = parse(filename)

    idx = 0
    while idx < len(lines):
        all_space = True
        for e in lines[idx]:
            if e != ".": all_space = False
        if all_space:
            temp = ""
            for e in lines[0]: temp += "."
            lines.insert(idx, temp)
            idx += 1
        idx += 1
    idx = 0
    while idx < len(lines[0]):
        all_space = True
        for line in lines:
            if line[idx] != ".": all_space = False
        if all_space:
            lines = [(line[:idx] + "." + line[idx:]) for line in lines]
            idx += 1
        idx += 1

    gal_dict = dict()
    cur = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                #print("i:",i,", j:",j)
                gal_dict.update({cur: [i,j]})
                cur += 1

    total = 0
    for i in range(cur):
        for j in range(i + 1, cur):
            total += abs(gal_dict[i][0] - gal_dict[j][0])
            total += abs(gal_dict[i][1] - gal_dict[j][1])
    
    print(total)



def part2(filename: str) -> None:
    lines = parse(filename)
    gap_size = 1000000
    gal_dict = dict()
    cur = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                #print("i:",i,", j:",j)
                gal_dict.update({cur: [i,j]})
                cur += 1

    idx = len(lines) - 1
    while idx >= 0: # update rows
        all_spaces = True
        for e in lines[idx]:
            if e != ".": all_spaces = False
        if all_spaces:
            for k in gal_dict:
                if gal_dict[k][0] > idx:
                    gal_dict.update({k: [gal_dict[k][0] + (gap_size - 1), gal_dict[k][1]]})
        idx -= 1
    idx = len(lines[0]) - 1
    while idx >= 0: # update columns
        all_space = True
        for line in lines:
            if line[idx] != ".": all_space = False
        if all_space:
            for k in gal_dict:
                if gal_dict[k][1] > idx:
                    gal_dict.update({k: [gal_dict[k][0], gal_dict[k][1] + (gap_size - 1)]})
        idx -= 1

    total = 0
    for i in range(cur):
        for j in range(i + 1, cur):
            total += abs(gal_dict[i][0] - gal_dict[j][0])
            total += abs(gal_dict[i][1] - gal_dict[j][1])

    print(total)

#print("--test 1--")
#part1("testInput.txt")
#print("--real 1\n--")
#part1("input.txt")

print("--test 2--")
part2("testInput.txt")
print("--real 2\n--")
part2("input.txt")
