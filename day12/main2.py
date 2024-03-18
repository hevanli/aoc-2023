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

def valid_combos(record: str, target: list[int]) -> int:
    if '?' not in record:
        return 1 if valid(record, target) else 0

    repDot = record.replace('?', '.', 1)
    repHash = record.replace('?', '#', 1)

    return valid_combos(repDot, target) + valid_combos(repHash, target)

def part1(filename: str) -> None:
    lines = parse(filename)

    sum = 0
    for line in lines:
        record = line.split()[0]
        target = [int(n) for n in line.split()[1].split(',')]
        sum += valid_combos(record, target)

    print(sum)

part1("testInput.txt")
part1("input.txt")


