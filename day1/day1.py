# take in file input
filename = "input1.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    sum = 0
    for line in lines:
        # create list of only the digits in the line
        nums = [char for char in line if char.isdigit()] 
        # combine first and last digit in list and add to sum
        sum += (int)(nums[0] + nums[len(nums) - 1]) 
    print(sum)

def part2():
    sum = 0
    replace = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
            }
    for line in lines:
        digits = []
        # traverse char by char, rewriting the line
        for i, c in enumerate(line):
            if (c.isdigit()):
                digits.append(c)
            else:
                for k in replace.keys():
                    if (line[i:].startswith(k)):
                        digits.append(replace[k])
                        break
            # ignore irrelevant chars
        sum += (int)(digits[0] + digits[len(digits) - 1])
    print(sum)

part1()
part2()
