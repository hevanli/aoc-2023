from math import lcm

def part2(filename):
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f]

    nav = {}

    directions = lines[0]
    lines = lines[2:]

    for d in lines:
        element = d[:3]
        left = d[7:10]
        right = d[12:15]
        nav[element] = [left, right]

    ghosts = [e for e in nav if e[2] == 'A']
    coefs = []
    for g in ghosts:
        curr = g
        steps = 0
        done = False
        while not done:
            for d in directions:
                next = 0 if d == 'L' else 1
                curr = nav[curr][next]
                steps += 1
                done = curr[2] == 'Z'
                if done:
                    break
        coefs.append(steps)

    print(lcm(*coefs))

if __name__ == '__main__':
    print('--test--')
    part2('testInput.txt')
    print('--input--')
    part2('input.txt')
