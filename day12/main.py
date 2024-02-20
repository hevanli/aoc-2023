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
    
    if t_idx == len(target) - 1 and target[t_idx] != cur_len: return False
    return True

def num_combos_valid(record: str, target: list[int]):
    q_count = record.count("?")
    q_idxs = [i for i,v in enumerate(record) if v == "?"]

    window_len = 0
    while window_len <= q_count:
        window_position = 0
        while window_position < len(record) - window_len:

        


    print(q_idxs)

def part1(filename: str) -> None:
    lines = parse(filename)
    records = [line.split()[0] for line in lines]
    targets = [[int(n) for n in line.split()[1].split(',')] for line in lines]

print("--test 1--")
part1("testInput.txt")
