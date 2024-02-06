def parse(filename: str) -> list[str]:
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def part1(filename: str) -> None:
    lines = parse(filename)
    return

def part2(filename: str) -> None:
    lines = parse(filename)
    return

print("--test1--")
part1("testInput.txt")
print("--real--")
part2("input.txt")
