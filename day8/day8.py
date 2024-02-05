from math import lcm

def parse(filename) -> list[str]:
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def part1(filename):
    lines = parse(filename)

    moves = lines[0]
    node_network = {}
    for line in lines[2:]:
        parts = line.split()
        key = parts[0]
        node = (parts[2][1:len(parts[2])-1], parts[3][:len(parts[3])-1])
        node_network.update({key: node})

    steps = 0
    cur = "AAA"
    while cur != "ZZZ":
        for step in moves:
            cur = node_network[cur][0 if step == "L" else 1]
            steps += 1
            if cur == "ZZZ": 
                break

    print(steps)

def part2(filename):
    lines = parse(filename)

    nav = {}

    directions = lines[0]
    lines = lines[2:]

    for d in lines:
        element = d[:3]
        left = d[7:10]
        right = d[12:15]
        nav[element] = [left, right]

    ghosts = [e for e in nav if e[2] == 'A']
    coefs = []
    for g in ghosts:
        curr = g
        steps = 0
        done = False
        while not done:
            for d in directions:
                next = 0 if d == 'L' else 1
                curr = nav[curr][next]
                steps += 1
                done = curr[2] == 'Z'
                if done:
                    break
        coefs.append(steps)

    print(lcm(*coefs))

print("--test2--")
part2("testInput.txt")
print("--real2--")
part2("input.txt")
            
