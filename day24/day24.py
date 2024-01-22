from numpy import array, cross # for vector cross product

filename = "testInput.txt"
lines = []
with (open(filename)) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    # parsing input into lists with comically long list comprehensions
    positions, velocities = [], []
    for line in lines:
        pVect = [int(coord.strip()) for coord in line.split("@")[0].split(",")]
        vVect = [int(coord.strip()) for coord in line.split("@")[1].split(",")]
        positions.append(array(pVect)) # numpy array
        velocities.append(array(vVect)) # numpy array

    count = 0 # tracks number of collisions in test area
    lower_bound = 7 # lower bound of collision area
    upper_bound = 27 # upper bound of collision area

    # brute force check all of them
    i = 0
    while i < len(positions):
        j = i + 1
        while j < len(positions):
            # parallel
            if (cross(velocities[i], velocities[j]) == 0):
                if (positions[i] == positions[j]): # not coinciding
                    continue
                else: # conciding
                    # TODO
                    break

            









part1()
