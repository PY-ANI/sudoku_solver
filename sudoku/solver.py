from time import sleep

class solver():

    def __init__(self, bo):
        self.bo=bo
        self.pos_x=0
        self.pos_y=0
        self.stop=True

    def valid(self, num, pos):

        for i in range(len(self.bo[0])):
            if self.bo[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(self.bo)):
            if self.bo[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.bo[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.bo[i][j] == 0:
                    return (i, j)
        return None

    def solve(self):

        find = self.find_empty()
        if not find or self.stop:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.pos_x = col*50
                self.pos_y = (row+1)*50
                self.bo[row][col] = i
                sleep(0.005)
                if self.solve() and not self.stop:
                    return True
                self.bo[row][col] = 0

        return False



# -------------------------------another aproach for solution -----------------------------------


# def safe_to_enter(n,x,y,grid):

#     k_x,k_y=x-(x%3),y-(y%3)

#     for i in range(9):
#         if x != i and grid[y][i] == n:
#             return 0
#         if y != i and grid[i][x] == n:
#             return 0
    
#     for i in range(3):
#         for j in range(3):
#             if x != j and y != i and grid[k_y+i][k_x+j] == n:
#                 return 0
#     return 1

# def solver():
#     global grid_q,grid,active_cell

#     for i in range(9):
#         for j in range(9):
#             if grid_q[i][j] == 0:
#                 for n in range(1,10):
#                     if safe_to_enter(n,j,i,grid_q):
#                         grid_q[i][j]=n
#                         solver()
#                         grid_q[i][j]=0
#                 return
#     print(grid_q)
#     for i in range(9):
#         for j in range(9):
#             grid[i][j] = grid_q[i][j]
#             active_cell=[50*j,50*(i+1)]
#             time.sleep(0.002)
