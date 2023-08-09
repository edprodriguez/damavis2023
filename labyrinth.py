# labyrinth
# "." - free
# "#" - blocked

# Test 1
labyrinth1 = [
[".",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".",".","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","."]]
# Result 11

# Test 2
labyrinth2 = [
[".",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".","#","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","."]
]
# Result -1

# Test 3:
labyrinth3 = [
[".",".","."],
[".",".","."],
[".",".","."]
]
# Result 2

labyrinth4 = [
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".","#",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".","#",".",".",".","#",".",".",".","."],
[".",".",".",".",".",".","#",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."]
]
# Result 16

# change the labyrinth among labyrinth1, labyrinth2, labyrinth3, labyrinth4 to test acceptance tests cases
labyrinth = labyrinth4


matrix_lines = len(labyrinth)
matrix_columns = len(labyrinth[0])
rod_size = 3
rod_horizontal = 1
debug = 1

# rod matrix values
# head position linea, columna
# 1 horizontal, 0 vertical


if (debug == 1):
    for l in range(matrix_lines):
        for c in range(matrix_columns):
            print ("line=",l,"column=",c,labyrinth[l][c])

if (debug == 1):
    print ("labyrinth lines=", matrix_lines)
    print ("labyrinth columns=", matrix_columns)
    print ("rod size=",rod_size)

#first way - horizontly right to the end then down to the end
movements = 0
rod_head_line = 0
rod_head_column = 2

# to the right horizontly
if (matrix_columns > 3):
    for c in range(matrix_columns - 3):
        if (labyrinth[0][c+3] == "."):
            rod_head_column += 1
            movements += 1
        else:
            movements = (-1)
            break
 
# down horizontly
if (movements != -1):
    for l in range(matrix_lines - 1):
        if ((labyrinth[l+1][matrix_columns-1] == ".") and (labyrinth[l+1][matrix_columns-2] == ".") and (labyrinth[l+1][matrix_columns-3] == ".")):
            rod_head_line += 1
            movements += 1
        else:
            movements = (-1)
            break

print("movements first way=",movements,"rod_head_line=",rod_head_line,"rod_head_column=",rod_head_column)


#second way - horizontly down, then to right
movements = 0
rod_head_line = 0
rod_head_column = 2

# down
for l in range(matrix_lines - 1):
    if ((labyrinth[l+1][0] == ".") and (labyrinth[l+1][1] == ".") and (labyrinth[l+1][2] == ".")):
        rod_head_line += 1
        movements += 1
    else:
        movements = (-1)
        break


# to the right
if (movements != -1 and matrix_columns > 3):
    for c in range(matrix_columns - 3):
        if (labyrinth[matrix_columns - 1][c+3] == "."):
            rod_head_column += 1
            movements += 1
        else:
            movements = (-1)
            break
 
print("movements second way=",movements,"rod_head_line=",rod_head_line,"rod_head_column=",rod_head_column)


# third way - horizontly, spin and down vertically
movements = 0
rod_head_line = 0
rod_head_column = 2

# to the right horizontly
if (matrix_columns > 3):
    for c in range(matrix_columns - 3):
        if (labyrinth[0][c+3] == "."):
            rod_head_column += 1
            movements += 1
        else:
            movements = (-1)
            break

# verify space to spin
if (movements != -1):
    for i in range (3):
        if (labyrinth[1][rod_head_column-i] == "#" or labyrinth[2][rod_head_column-i] == "#"):
            movements = (-1)
            break

# 1 position down
if (movements != -1):
    rod_head_line =+ 1
    movements += 1

# spin
if (movements != -1):
    rod_horizontal = 0
    rod_head_line =+1;
    rod_head_column =-1
    movements += 1


# 1 position right
if (movements != -1):
    rod_head_column =+1
    movements += 1

# down vertically
if (movements != -1 and matrix_lines > 3 and matrix_columns > 3):
    for l in range(matrix_lines - 3):
        if ((labyrinth[l+3][matrix_columns-1] == ".")):
            rod_head_line += 1
            movements += 1
        else:
            movements = (-1)
            break

print("movements third way=",movements,"rod_head_line=",rod_head_line,"rod_head_column=",rod_head_column)


# forth way - spin, vertically down, spin, horizontly to the right