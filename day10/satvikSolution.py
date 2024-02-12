from math import ceil

def parse(data, dataset, strip=True):
    with open(dataset) as f:
        n = f.readline()
        while n != '':
            data.append(n.strip() if strip else n)
            n = f.readline()

class Node:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.direction = ''
        self.distance = -1

    def get_openings(self):
        match self.val:
            case '|':
                return (self.row-1, self.col), (self.row+1, self.col)
            case '-':
                return (self.row, self.col-1), (self.row, self.col+1)
            case 'L':
                return (self.row-1, self.col), (self.row, self.col+1)
            case 'J':
                return (self.row-1, self.col), (self.row, self.col-1)
            case '7':
                return (self.row+1, self.col), (self.row, self.col-1)
            case 'F':
                return (self.row+1, self.col), (self.row, self.col+1)
        return (-1, -1), (-1, -1)


# given that r1, c1 exists
def equivalent(nodes, r1, c1, r2, c2):
    if valid(r2, c2, nodes):
        return (r1, c1) == (r2, c2)
    return False


def valid(row, col, nodes):
    return 0 <= row < len(nodes) and 0 <= col < len(nodes[0])


def dfs(prev, curr, distance, nodes):
    if curr.val == 'S':
        return None

    (r1, c1), (r2, c2) = curr.get_openings()
    r, c = 0, 0
    if equivalent(nodes, prev.row, prev.col, r1, c1):
        r, c = r2, c2
    else:
        r, c, = r1, c1

    curr.distance = distance
    if valid(r, c, nodes):
        return curr, nodes[r][c], distance + 1, nodes
    return None

# 0 if down, 1 if up, -1 if neither
def calculate_direction(loop, node):
    if node.val == '-':
        return -1

    if node.distance < len(loop) - 1:
        # check the vertical relation to the next node
        if loop[node.distance + 1].row > node.row: # moving down
            return 0
        if loop[node.distance + 1].row < node.row: # moving up
            return 1

    if node.distance > 0:
        # check the vertical relation to the previous node
        if node.row > loop[node.distance - 1].row: # moving down
            return 0
        if node.row < loop[node.distance - 1].row: # moving up
            return 1

    return -1 # this will only be in the case -S- (I think)


def solve(dataset):
    data = []
    parse(data, dataset)

    nodes = []
    starting = Node(0, 0, 0)
    for i, row in enumerate(data):
        curr = []
        for j, e in enumerate(row):
            curr.append(Node(i, j, e))
            if curr[-1].val == 'S':
                starting = curr[-1]
        nodes.append(curr)

    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]:
        if valid(starting.row + dr, starting.col + dc, nodes):
            next = nodes[starting.row + dr][starting.col + dc]
            if (starting.row, starting.col) in list(next.get_openings()):
                # loop is here to get around pythons recursive limit
                # and to save memory
                d = starting, next, 1, nodes
                while True:
                    prev, curr, distance, nodes = d
                    d = dfs(prev, curr, distance, nodes)
                    if d == None:
                        break
                break

    starting.distance = 0
    loop = [starting]

    for row in nodes:
        for e in row:
            if e.distance > 0:
                loop.append(e)

    loop = sorted(loop, key=lambda x: x.distance)

    total = 0
    for row in nodes:
        last_direction = -1
        num_direction_changes = 0
        for e in row:
            if e.distance >= 0: # in loop
                new_dir = calculate_direction(loop, e)
                if new_dir != -1 and new_dir != last_direction:
                    num_direction_changes += 1
                    last_direction = new_dir
            else:
                if num_direction_changes % 2 == 1: # in the loop
                    total += 1
    print(total)

if __name__ == '__main__':
    print('--input--')
    solve('input.txt')
