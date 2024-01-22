filename = "input5.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

# initializaing stuff
seeds = [int(seed) for seed in lines[0][lines[0].index(":")+1:].split()]

map_lines = lines[2:]
maps = [] # list of dictionaries that rep each map

# fill up maps
line_num,map_num = 0, 0
while line_num < len(map_lines):
    # procedure for adding one map
    line_num += 1 # skip map name
    maps.append([]) # create new empty map
    cur_map = maps[map_num]
    cur_line = map_lines[line_num] 
    while map_lines[line_num] != "":
        cur_map.append([int(num) for num in cur_line.split()])
        line_num += 1

        if line_num >= len(map_lines): break
        else: cur_line = map_lines[line_num]

    line_num += 1
    map_num += 1

def part1():
    min_location = 1e12 # arbitrarily large value
    for seed in seeds:
        cur = seed
        for map in maps:
            for m_range in map:
                dest,source,range_len = m_range # splat
                # check if cur falls within the range
                if cur >= source and cur < source + range_len:
                    cur = cur - source + dest
                    break
        min_location = min(min_location, cur)

    print(min_location)

def part2():
    min_location = 1e12 # arbitrarily large value
    for seed in seeds:
        cur = seed
        for map in maps:
            for m_range in map:
                dest,source,range_len = m_range # splat
                # check if cur falls within the range
                if cur >= source and cur < source + range_len:
                    cur = cur - source + dest
                    break
        min_location = min(min_location, cur)

    print(min_location)

part1()

