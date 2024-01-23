filename = "input5.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    seeds = [int(seed) for seed in lines[0][lines[0].index(":")+1:].split()]
    # initializaing map stuff
    map_lines = lines[2:]
    maps = [] 

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

def min_seed_range_location(maps, seed_range):
    cur_ranges = [seed_range]
    for map in maps:
        ranges_to_check = cur_ranges
        cur_ranges = []
        while len(ranges_to_check) > 0:
            hit_a_range = False
            for cur_map in map:
                dest,source,c_len = cur_map # splat m_range
                start,s_len = ranges_to_check[0] # splat s_range
                m_end = source + c_len - 1
                s_end = start + s_len - 1 

                # is completely in the range
                if start >= source and s_end <= m_end:
                    #print("hi i'm in!", cur_map, " ", m_end)
                    new_start = (start - source) + dest
                    cur_ranges.append((new_start, s_len))
                    ranges_to_check.pop(0)
                    hit_a_range = True
                    break

                # seed range is partially in the range
                    # top part
                end_in_range = s_end >= source and s_end <= m_end
                if end_in_range and start < source:
                    ranges_to_check[0] = (start, source - start)
                    new_len = s_end - source + 1
                    new_start = dest
                    cur_ranges.append((new_start, new_len))
                    hit_a_range = True
                    break

                    # bottom part 
                start_in_range = start >= source and start <= m_end
                if start_in_range and s_end > m_end:
                    ranges_to_check[0] = (m_end + 1, s_end - m_end)
                    new_len = m_end - start + 1
                    new_start = dest + (start - source)
                    cur_ranges.append((new_start, new_len))
                    hit_a_range = True
                    break

            # if this seed range isn't in any range, don't change it
            if not hit_a_range:
                cur_ranges.append(ranges_to_check[0])
                ranges_to_check.pop(0)

        print(cur_ranges) 

    min_location = 1e12
    for location_range in cur_ranges:
        start,length = location_range
        min_location = min(min_location, start)
    return min_location

def part2():
    seeds = [int(seed) for seed in lines[0][lines[0].index(":")+1:].split()]
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i+1]))
    #print(seed_ranges)

    # initializaing map stuff
    map_lines = lines[2:]
    maps = [] 

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

    min_location = 1e12 # arbitrarily large value
    for seed_range in seed_ranges:
        min_location = min(min_location, min_seed_range_location(maps, seed_range))

    print(min_location)

part2()
