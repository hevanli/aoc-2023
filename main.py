def parse(filename: str) -> list[str]:
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def part1(filename: str) -> None:
    lines = parse(filename)

def part2(filename: str) -> None:
    lines = parse(filename)

print("--test 1--")
part1("testInput.txt")
