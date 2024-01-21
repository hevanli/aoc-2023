filename = "input4.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    winning_nums, nums_i_have = [], []
    for line in lines:
        winning_nums.append(line.split("|")[0][line.index(":")+2:].split())
        nums_i_have.append(line.split("|")[1].split())

    point_total = 0
    for i in range(len(winning_nums)):
        matches = 0
        for num in nums_i_have[i]:
            if num in winning_nums[i]: matches += 1 
        
        if matches > 0: 
            point_total += 2 ** (matches - 1)

    print(point_total)

def part2():
    winning_nums, nums_i_have = [], []
    for line in lines:
        winning_nums.append(line.split("|")[0][line.index(":")+2:].split())
        nums_i_have.append(line.split("|")[1].split())

    copies = []
    for i in range(len(lines)):
        copies.append(1)

    for i in range(len(winning_nums)):
        matches = 0
        for num in nums_i_have[i]:
            if num in winning_nums[i]: matches += 1

        if matches > 0:
            for j in range(i+1, i+1+matches):
                copies[j] += copies[i]

    sum = 0
    for copy in copies:
        sum += copy

    print(sum)

part2()



