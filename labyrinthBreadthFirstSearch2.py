
from collections import deque

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

labyrinth5 = []
labyrinth5.append (["O"," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," "," "])
labyrinth5.append ([" "," "," "," "," "," "," "," "," ","X"])
# Result 16

def solveMaze(maze):
    R, C = len(maze), len(maze[0])

    start = (0, 0)
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'X':
                start = (r, c)
                break
        else: continue
        break
    else:
        return None

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == "O":
            return coord[2]

        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2]+1))

labyrinth = labyrinth5

print("Number of moves: ", solveMaze(labyrinth))