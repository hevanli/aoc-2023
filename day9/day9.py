def parse(filename: str) -> list[str]:
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def part1(filename: str) -> None:
    lines = parse(filename)

    total = 0
    for line in lines:
        arrs = [[int(num) for num in line.split()]]
        all_zeroes = False
        while not all_zeroes:
            all_zeroes = True
            prev_nums = arrs[len(arrs)-1]
            cur_arr = []
            for i in range(len(prev_nums)-1):
                cur_num = prev_nums[i+1] - prev_nums[i]
                cur_arr.append(cur_num)
                if cur_num != 0: all_zeroes = False
            arrs.append(cur_arr)
       
        prediction = 0
        for i in range(len(arrs)-1, -1, -1): # iterate backwards
            prediction += arrs[i][len(arrs[i])-1]
        total += prediction
    print(total)

def part2(filename: str) -> None:
    lines = parse(filename)
    total = 0
    for line in lines:
        arrs = [[int(num) for num in line.split()]]
        all_zeroes = False
        while not all_zeroes:
            all_zeroes = True
            prev_nums = arrs[len(arrs)-1]
            cur_arr = []
            for i in range(len(prev_nums)-1):
                cur_num = prev_nums[i+1] - prev_nums[i]
                cur_arr.append(cur_num)
                if cur_num != 0: all_zeroes = False
            arrs.append(cur_arr)
       
        last_prediction = 0
        for i in range(len(arrs)-2, -1, -1): # iterate backwards
            last_prediction = arrs[i][0] - last_prediction
        total += last_prediction
    print("total answer:", total)

#print("--test1--")
#part1("testInput.txt")
#print("--real1--")
#part1("input.txt")

print("--test2--")
part2("testInput.txt")
print("--real2--")
part2("input.txt")
