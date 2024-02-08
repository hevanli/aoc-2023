from math import ceil

# debugging function
def print_data(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == -1: print(".", end=" ")
            else: print(data[i][j], end=" ")
        print("\n")

def parse(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def in_bounds(r: int, c: int, arr: list[str]) -> bool:
    return r >= 0 and c >= 0 and r < len(arr) and c < len(arr[0]) 
    
def part1(filename: str) -> None:
    lines = parse(filename)
    s_r,s_c = 0,0 # start coordinates
    dist = [] # distance map
    
    # find starting coord
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S": 
                s_r = i
                s_c = j

    pipes = {
            "|": [(-1,0),(1,0)],
            "-": [(0,-1),(0,1)],
            "L": [(-1,0),(0,1)],
            "J": [(-1,0),(0,-1)],
            "7": [(1,0),(0,-1)],
            "F": [(1,0),(0,1)],
            }
    
    up = ["|","7","F"]
    down = ["|","L","J"]
    left = ["-","L","F"]
    right = ["-","J","7"]

    to_check = []
    if s_c > 0 and lines[s_r-1][s_c] in up: 
        to_check.append([s_r-1, s_c]) # up
    if s_r > 0 and lines[s_r][s_c-1] in left: 
        to_check.append([s_r, s_c-1]) # left
    if s_c < len(lines)-1 and lines[s_r+1][s_c] in down: 
        to_check.append([s_r+1, s_c]) # down
    if s_r < len(lines[0])-1 and lines[s_r][s_c+1] in right: 
        to_check.append([s_r, s_c+1]) # right

    for possible_path in to_check:
        # initialize distance map
        dist = []
        for i in range(len(lines)):
            cur = []
            for j in range(len(lines[0])):
                cur.append(-1)
            dist.append(cur)
        dist[s_r][s_c] = 0

        cur_dist = 1 # current distance traveled from the (S)tart
        r,c = possible_path # current coords
        dist[r][c] = cur_dist # set start node to 1 distance
        cur_tile = lines[r][c] 

        found_path = False # check if you have a path that works
        searching = True # are you still searching this path
        while searching:
            possible_dirs = pipes[cur_tile]
            dir_confirmed = False
            
            for possible_dir in possible_dirs:
                dr,dc = possible_dir
                if in_bounds(r+dr, c+dc, lines): # stays in bounds
                    next_tile = lines[r+dr][c+dc]
                    if next_tile == "S" and cur_dist != 1: # got back to the start
                        found_path = True
                        searching = False
                        break
                    if dist[r+dr][c+dc] == -1: # hasn't been checked yet
                        can_up = dr == -1 and next_tile in up
                        can_down = dr == 1 and next_tile in down
                        can_left = dc == -1 and next_tile in left
                        can_right = dc == 1 and next_tile in right
                        if can_up or can_down or can_left or can_right:
                            r,c = r+dr,c+dc
                            cur_dist += 1
                            dist[r][c] = cur_dist
                            cur_tile = lines[r][c]
                            dir_confirmed = True
                            break
            if not dir_confirmed:
                searching = False

        if found_path:
            print("the farthest position is", ceil(cur_dist/2), "tiles away")
            break

def part2(filename: str) -> None:
    lines = parse(filename)
    # idea:
    # use part 1's logic to generate a distance map for the path
    # create a row and column list 
    # row list contains the highest and lowest path row for a column
    # col list contains the leftest and rightest path for a row
    # traverse through the input:
    # if the length of row and col list at that coord are 0, move on
    # elif the coord is below the highest and above the leftest:
    # and the coord is between the leftest and rightest
        # count++

print("--real 1--\n")
part1("input.txt")

