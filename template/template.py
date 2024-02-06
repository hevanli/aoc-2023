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

print("--test 1--")
part1("testInput.txt")
print("--real 1--")
part1("input.txt")

print("--test 2--")
part2("testInput.txt")
print("--real 2--")
part2("input.txt")
