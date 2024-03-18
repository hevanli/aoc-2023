import functools

def parse(filename: str) -> list[str]:
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

@functools.cache
def valid_count(record: str, target: tuple) -> int:
    # base cases
    if record == "": 
        return 1 if target == () else 0
    if target == ():
        return 1 if '#' not in record else 0

    result = 0

    if record[0] in '.?':
        result += valid_count(record[1:], target)
    
    if record[0] in '#?':
        cur_target = target[0] # length of the current contiguous target

        if (
            cur_target <= len(record)
            and '.' not in record[:cur_target]
            and (cur_target == len(record) or record[cur_target] != '#')
            ):
            result += valid_count(record[cur_target+1:], target[1:])
            
    return result

def part1(filename: str) -> None:
    lines = parse(filename)

    count = 0
    for line in lines:
        record = line.split()[0]
        target = tuple(map(int, line.split()[1].split(',')))
        count += valid_count(record, target)

    print(count)

def part2(filename: str) -> None:
    lines = parse(filename)

    count = 0
    for line in lines:
        record = ((line.split()[0]+"?")*5)[:-1]
        target = tuple(map(int, line.split()[1].split(',')*5))
        count += valid_count(record, target)

    print(count)

#part1("testInput.txt")
#part1("input.txt")

part2("testInput.txt")
part2("input.txt")



