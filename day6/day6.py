import time

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
    time,distance = "",""
    for s in lines[0].split()[1:]: time += s
    for s in lines[1].split()[1:]: distance += s
    time,distance = int(time),int(distance)

    count = 0
    for t in range(1, time):
        if (time - t) * t > distance:
            count += 1

    print(count)

def part2_smarter():
    time,distance = "",""
    for s in lines[0].split()[1:]: time += s
    for s in lines[1].split()[1:]: distance += s
    time,distance = int(time),int(distance)

    first_win, last_win = 0,0
    for i in range(0, time):
        if (time - i) * i > distance:
            first_win = i
            break
    for i in range(time, 0, -1):
        if (time - i) * i > distance:
            last_win = i
            break

    print(last_win - first_win + 1)
 
brute_start = time.time()
part2_brute()
brute_end = time.time()

smart_start = time.time()
part2_smarter()
smart_end = time.time()

print("Brute algorithm took:", brute_end - brute_start, "seconds.")
print("Smart algorithm took:", smart_end - smart_start, "seconds.")
