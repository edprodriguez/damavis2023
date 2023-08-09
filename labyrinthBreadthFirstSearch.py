import queue

# labyrinth
# "." or " " - free
# "#" - blocked 
# "O" - start
# "X" - end

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

# Verify valid moves

def valid(lab, moves):
    for x, pos in enumerate(lab[0]):
        if pos == "O":
            start = x

    column = start
    line = 0

    for move in moves:
        if move == "L":
            column -= 1
        elif move == "R":
            column += 1
        elif move == "U":
            line -= 1
        elif move == "D":
            line += 1

        if not(0 <= column < len(lab[0]) and 0 <= line < len(lab)):
            return False
        elif (lab[line][column] == "#"):
            return False

#Find End Search

def findEnd(lab, moves):
    for x, pos in enumerate(lab[0]):
        if pos == "O":
            start = x

    column = start
    line = 0

    for move in moves:
        if move == "L":
            column -= 1
        elif move == "R":
            column += 1
        elif move == "U":
            line -= 1
        elif move == "D":
            line += 1

    if lab[line][column] == "X":
        print("Found using ", moves ," moves")
        return True
    
    return False

# Breadth First Search Algorithm with a simple rod (1x1)
debug = 1
n = queue.Queue()
n.put("")
a = ""

# change the labyrinth among labyrinth1, labyrinth2, labyrinth3, labyrinth4 to test acceptance tests cases

labyrinth = labyrinth5

while not findEnd(labyrinth, a):
    a = n.get()
#    if (debug == 1):
    print(a)
    for j in ["L", "R", "U", "D"]:
        put = a + j
        if valid(labyrinth, put):
            n.put(put)