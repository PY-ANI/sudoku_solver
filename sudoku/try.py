from random import randrange
# from generator import sudoku_gen

grid=[
    [1,2,3, 4,5,6, 7,8,9],
    [4,5,6, 7,8,9, 1,2,3],
    [7,8,9, 1,2,3, 4,5,6],

    [2,1,4, 3,6,5, 8,9,7],
    [3,6,5, 8,9,7, 2,1,4],
    [8,9,7, 2,1,4, 3,6,5],
    
    [5,3,1, 6,4,2, 9,7,8],
    [6,4,2, 9,7,8, 5,3,1],
    [9,7,8, 5,3,1, 6,4,2]]

bo=[
    [0,0,0 ,0,0,0 ,0,0,0],
    [0,0,0 ,0,0,0 ,0,0,0],
    [0,0,0 ,0,0,0 ,0,0,0],

    [0,0,0 ,0,0,0 ,0,0,0],
    [0,0,0 ,0,0,0 ,0,0,0],
    [0,0,0 ,0,0,0 ,0,0,0],

    [0,0,0 ,0,0,0 ,0,0,0],
    [0,0,0 ,0,0,0 ,0,0,0],
    [0,0,0 ,0,0,0 ,0,0,0],
    ]


def valid(num, pos):
    global bo

    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty():
    global bo

    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)
    return None

def solve():
    global bo

    find = find_empty()
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(i, (row, col)):
            bo[row][col] = i
            if solve():
                return True
            bo[row][col] = 0

    return False

def puzzle_density(value_set,density):
    for i in range(9):
        for j in range(density):
            value_set[i][randrange(0,9)]=0

def do_some():
    global grid

    for i in range(9):
        for j in range(9):
            if not valid(grid[i][j],(j,i)):
                print("galat ha!!!!")
                return
    print("sahi ha!!!!")

def shuffle():
    global grid




do_some()
