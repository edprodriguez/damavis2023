from collections import deque

# "O" - objective
# "X" - start
# labyrinth
# "." - free
# "#" - blocked

# Test 1
labyrinth1 = [
["X",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".",".","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","O"]]
# Result 12 - rod 1
# Result 11 - rod 3

# Test 2
labyrinth2 = [
["X",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".","#","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","O"]
]
# Result 12 - rod 1
# Result -1 - rod 3

# Test 3:
labyrinth3 = [
["X",".","."],
[".",".","."],
[".",".","O"]
]
# Result 4 - rod 1
# Result 2 - rod 3

labyrinth4 = [
["X",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".","#",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".","#",".",".",".","#",".",".",".","."],
[".",".",".",".",".",".","#",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","O"]
]
# Result 18 - rod 1
# Result 16 - rod 3

labyrinth5 = [
["X",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".","#",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".","#",".",".",".","#",".",".",".","."],
[".",".",".",".",".",".","#",".",".","."],
[".",".",".",".",".",".",".",".",".","#"],
[".",".",".",".",".",".",".",".","#","O"]
]
# Result -1 - rod 1
# Result -1 - rod 3

# change the labyrinth among labyrinth1, labyrinth2, labyrinth3, labyrinth4 to test acceptance tests cases
labyrinth = labyrinth4


matrix_lines = len(labyrinth)
matrix_columns = len(labyrinth[0])
rod_size = int(3) # must be odd to have a perfect center
rod_shift = int((rod_size - 1) / 2)

rod_horizontal = 1
debug = 1

# rod matrix values
# head position linea, columna
# 1 horizontal, 0 vertical


if (debug == 1):
    for l in range(matrix_lines):
        print (labyrinth[l])

if (debug == 1):
    print ("labyrinth lines=", matrix_lines)
    print ("labyrinth columns=", matrix_columns)
    print ("rod size=",rod_size)

movements = 0



# solution for a rod of 1
def solveLabRod1(lab):
    lines, columns = len(lab), len(lab[0])

    start = (0, 0)
    for l in range(lines):
        for c in range(columns):
            if lab[l][c] == 'X':
                start = (l, c)
                break
        else: continue
        break
    else:
        return -1

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * columns for _ in range(lines)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        if lab[coord[0]][coord[1]] == "O":
            return coord[2]

        for dir in directions:
            nl, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nl < 0 or nl >= lines or nc < 0 or nc >= columns or lab[nl][nc] == "#" or visited[nl][nc]): continue
            queue.appendleft((nl, nc, coord[2]+1))

    return -1

print("Labyrinth 1 - Number of moves of rod 1: ", solveLabRod1(labyrinth1))

print("Labyrinth 2 - Number of moves of rod 1: ", solveLabRod1(labyrinth2))

print("Labyrinth 3 - Number of moves of rod 1: ", solveLabRod1(labyrinth3))

print("Labyrinth 4 - Number of moves of rod 1: ", solveLabRod1(labyrinth4))

print("Labyrinth 5 - Number of moves of rod 1: ", solveLabRod1(labyrinth5))

# solution for a rod of 3
def solveLabRod3(lab):
    debug = 0
    lines, columns = len(lab), len(lab[0])

    # expanding the objective to the center of the rod when horizontal for rod 3
    for s in range(rod_shift):
        if lab [lines-1][columns-1-1-s] != "#":
            lab [lines-1][columns-1-1-s] = "O"

    if (debug == 1):
        for l in range(lines):
            print (lab[l])

    start = (0, 0)
    for l in range(lines):
        for c in range(columns):
            if lab[l][c] == 'X':
                start = (l, c + rod_shift)
                rod_center_line = l # initially position horizontal - in the future it is possible to set this as a parameter
                rod_center_column = c + rod_shift
                break
        else: continue
        break
    else:
        return -1

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * columns for _ in range(lines)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        if lab[coord[0]][coord[1]] == "O":
            return coord[2]

        for dir in directions:
            nl, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nl < 0 or nl >= lines or nc < 0 or nc >= columns or lab[nl][nc] == "#" or visited[nl][nc]): continue
            queue.appendleft((nl, nc, coord[2]+1))

    return -1

print("Labyrinth 1 - Number of moves of rod 3: ", solveLabRod3(labyrinth1))

print("Labyrinth 2 - Number of moves of rod 3: ", solveLabRod3(labyrinth2))

print("Labyrinth 3 - Number of moves of rod 3: ", solveLabRod3(labyrinth3))

print("Labyrinth 4 - Number of moves of rod 3: ", solveLabRod3(labyrinth4))

print("Labyrinth 5 - Number of moves of rod 3: ", solveLabRod3(labyrinth5))