from collections import deque

# "O" - origin
# "X" - exit
# labyrinth
# "." - free
# "#" - blocked

# Test 1
labyrinth1 = [
["O",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".",".","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","X"]]
# Result 11

# Test 2
labyrinth2 = [
["O",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".","#","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","X"]
]
# Result -1

# Test 3:
labyrinth3 = [
["O",".","."],
[".",".","."],
[".",".","X"]
]
# Result 2

labyrinth4 = [
["O",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".","#",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".","#",".",".",".","#",".",".",".","."],
[".",".",".",".",".",".","#",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","X"]
]
# Result 16


# change the labyrinth among labyrinth1, labyrinth2, labyrinth3, labyrinth4 to test acceptance tests cases
labyrinth = labyrinth4


matrix_lines = len(labyrinth)
matrix_columns = len(labyrinth[0])
rod_size = 3
rod_horizontal = 1
debug = 0

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
rod_position_line = 0
rod_position_column = 1


# solution for a rod of 1
def solveLabRod1(lab):
    lines, columns = len(lab), len(lab[0])

    start = (0, 0)
    for r in range(lines):
        for c in range(columns):
            if lab[r][c] == 'X':
                start = (r, c)
                break
        else: continue
        break
    else:
        return None

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
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= lines or nc < 0 or nc >= columns or lab[nr][nc] == "#" or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2]+1))

print("Number of moves of rod 1: ", solveLabRod1(labyrinth1))

print("Number of moves of rod 1: ", solveLabRod1(labyrinth2))

print("Number of moves of rod 1: ", solveLabRod1(labyrinth3))

print("Number of moves of rod 1: ", solveLabRod1(labyrinth4))

# solution for a rod of 3
def solveLabRod3(lab):
    lines, columns = len(lab), len(lab[0])

    start = (0, 0)
    for r in range(lines):
        for c in range(columns):
            if lab[r][c] == 'X':
                start = (r, c)
                break
        else: continue
        break
    else:
        return None

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
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= lines or nc < 0 or nc >= columns or lab[nr][nc] == "#" or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2]+1))

print("Number of moves of rod 3: ", solveLabRod3(labyrinth1))

print("Number of moves of rod 3: ", solveLabRod3(labyrinth2))

print("Number of moves of rod 3: ", solveLabRod3(labyrinth3))

print("Number of moves of rod 3: ", solveLabRod3(labyrinth4))