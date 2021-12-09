from secrets import choice

class sudoku_gen():

    def __init__(self) -> None:
        self.set_1=[i for i in range(1,10)]
        self.set_2=[i for i in range(9)]

    def valid(self, num, pos,value_set):

        for i in range(9):
            if value_set[pos[0]][i] == num and pos[1] != i:
                return False
            if value_set[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if value_set[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty(self,value_set):

        for i in range(9):
            for j in range(9):
                if value_set[i][j] == 0:
                    return (i, j)
        return None

    def solve(self,value_set):

        find = self.find_empty(value_set)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.valid(i, (row, col),value_set):
                value_set[row][col] = i
                if self.solve(value_set):
                    return True
                value_set[row][col] = 0

        return False

    def puzzle_density(self,value_set,density):
        for i in range(9):
            for j in range(density):
                value_set[i][choice(self.set_2)]=0

    def empty(self,grid):
        for i in range(9):
            for j in range(9):
                grid[i][j]=0

    def generator(self,grid,lvl=9):
        self.empty(grid)
        grid[choice(self.set_2)][choice(self.set_2)]=choice(self.set_1)
        grid[0][0]=choice(self.set_1)
        self.solve(grid)
        self.puzzle_density(grid,lvl)
        
if __name__ == "__main__":
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

    sudoku_gen().generator(bo)

    print(bo)