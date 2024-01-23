filename = "input6.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    times = [int(time) for time in lines[0].split()[1:]]
    distances = [int(distance) for distance in lines[1].split()[1:]]

    total = 1
    for i in range(len(times)):
        count = 0
        for time in range(1, times[i]):
            if (times[i] - time) * time > distances[i]:
                count += 1
        if count > 0:
            total *= count
    print(total)

def part2_brute():
    time = ""
    for s in lines[0].split()[1:]:
        time += s
    time = int(time)

    distance = ""
    for s in lines[1].split()[1:]:
        distance += s
    distance = int(distance)

    count = 0
    for t in range(1, time):
        if (time - t) * t > distance:
            count += 1

    print(count)

part2_brute()

