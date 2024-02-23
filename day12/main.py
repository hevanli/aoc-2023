def parse(filename: str) -> list[str]:
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def valid(record: str, target: list[int]) -> bool:
    t_idx = 0
    in_spring = False
    cur_len = 0

    for c in record:
        if c == "#" and in_spring: 
            cur_len += 1
        elif c == "#" and not in_spring:
            cur_len = 1
            in_spring = True
        elif c == "." and in_spring:
            if t_idx >= len(target) or target[t_idx] != cur_len: return False
            in_spring = False
            cur_len = 0
            t_idx += 1
    
    if t_idx > len(target) - 1 and cur_len: return False # too many #'s
    if t_idx < len(target) - 1: return False # didn't reach the last target
    if t_idx == len(target) - 1 and target[t_idx] != cur_len: return False # didn't complete last target
    return True # otherwise, it's valid!

def all_combos(record: str) -> list[str]:
    steps = []

    for i,c in enumerate(record):
        if c == "?":
            if len(steps) == 0:
                dot = record[0:i] + "." + record[i+1:]
                hash = record[0:i] + "#" + record[i+1:]
                steps.append([dot, hash])
            else:
                cur_step = []
                for elem in steps[len(steps)-1]:
                    cur_step.append(elem[0:i] + "." + elem[i+1:])
                    cur_step.append(elem[0:i] + "#" + elem[i+1:])
                steps.append(cur_step)
    
    return steps[len(steps)-1]

def part1(filename: str) -> None:
    lines = parse(filename)
    records = [line.split()[0] for line in lines]
    targets = [[int(n) for n in line.split()[1].split(',')] for line in lines]

    count = 0
    for i,record in enumerate(records):
        cur_count = 0 # get rid of later
        target = targets[i]
        combos = all_combos(record)
        for combo in combos:
            if valid(combo, target):
                count += 1
                cur_count += 1
        print("Line",i,"has",cur_count,"solutions")
    
    print("The solution is:", count)

# improve upon alg, make it recursive so the required memory doesn't grow so crazily
# then... idfk tbh
def part2(filename: str) -> None:
    lines = parse(filename)
    records = []
    records = [((line.split()[0]+"?")*5)[:-1] for line in lines]
    targets = [[int(n) for n in line.split()[1].split(',')]*5 for line in lines]

    # for record in records: print(record)
    # for target in targets: print(target)

    count = 0
    for i,record in enumerate(records):
        target = targets[i]
        print("CURRENT RECORD:", record)
        print("CURRENT TARGET:", target)

        cur_count = 0 # get rid of later
        combos = all_combos(record)
        print("ALL COMBOS:", combos)

        for combo in combos:
            if valid(combo, target):
                count += 1
                cur_count += 1
        print("Line",i,"has",cur_count,"solutions")
    
    print("The solution is:", count)
    

#print("--test 1--")
#part1("testInput.txt")

print("--test 2--")
part2("testInput.txt")

#print("--real 1--")
#part1("input.txt")
