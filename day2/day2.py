filename = "input2.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    sum = 0
    # iterates through each game
    for i, line in enumerate(lines):
        flag = True
        subsets = line[line.index(":")+2:].split(";")
        # iterates through each subset in each game
        for subset in subsets:
            colors = [color.strip() for color in subset.split(", ")]
            r,g,b = 0,0,0
            for color in colors:
                indexOfSpace = color.index(" ")
                if ("red" in color):
                    r = (int)(color[0:indexOfSpace])
                if ("green" in color):
                    g = (int)(color[0:indexOfSpace])
                if ("blue" in color):
                    b = (int)(color[0:indexOfSpace])
                if (r > 12 or g > 13 or b > 14):
                    flag = False
                    break
        if flag:
            sum += i + 1

    print(sum)

def part2():
    sum = 0
    # iterates through each game
    for i, line in enumerate(lines):
        g_r,g_g,g_b = 0,0,0
        subsets = line[line.index(":")+2:].split(";")
        # iterates through each subset in each game
        for subset in subsets:
            colors = [color.strip() for color in subset.split(", ")]
            r,g,b = 0,0,0
            for color in colors:
                indexOfSpace = color.index(" ")
                if ("red" in color):
                    r = (int)(color[0:indexOfSpace])
                if ("green" in color):
                    g = (int)(color[0:indexOfSpace])
                if ("blue" in color):
                    b = (int)(color[0:indexOfSpace])
            g_r = max(g_r, r)
            g_g = max(g_g, g)
            g_b = max(g_b, b)
        sum += g_r * g_g * g_b

    print(sum)


part1()
part2()

