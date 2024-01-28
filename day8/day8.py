filename = "testInput.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
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

def part2():
    moves = lines[0]
    node_network = {}
    for line in lines[2:]:
        parts = line.split()
        key = parts[0]
        node = (parts[2][1:len(parts[2])-1], parts[3][:len(parts[3])-1])
        node_network.update({key: node})

    for k,v in node_network.items():
        print(k,v)
    

part2()
            
