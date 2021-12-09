import pygame
import threading
import time
from utility import button,draw_board_vals,draw_moves,draw_timer
from solver import solver
from generator import sudoku_gen
from random import randrange

pygame.init()

width,height=450,450

win=pygame.display.set_mode((width,height+100))
pygame.display.set_caption("   SUDOKU   ")

board=pygame.transform.scale(pygame.image.load("./utils/sudoku.png"),(width,height))
pause_png=pygame.transform.scale(pygame.image.load("./utils/pause.png"),(30,30))
resume_png=pygame.transform.scale(pygame.image.load("./utils/resume_s.png"),(30,30))
new_png=pygame.transform.scale(pygame.image.load("./utils/reload.png"),(30,30))
reset_button=button(win,"RESET",22,(255,255,255),120,height+60)
solve_button=button(win,"SOLVE",22,(255,255,255),270,height+60)
cancel_button=button(win,"CANCEL",22,(255,255,255),270,height+60)
game_state_button=button(win,"pause_resume",30,(0,0,0),180,10)
new_set=button(win,"new",30,(0,0,0),240,10)

grid=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

grid[randrange(9)][randrange(9)]=randrange(1,10)

locked={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}

thread=None
moves=0
current_time=0
actual_time=0
active_cell=None
pause=False

Solve=solver(grid)

def timer():
    global current_time,pause
    time.sleep(1)
    while 1:
        if not pause: 
            current_time+=1
        time.sleep(1)

def reset():
    global moves,current_time,actual_time,grid,active_cell

    moves=0
    current_time=0
    active_cell=[0,50]
    for i in range(9):
        for j in range(9):
            if j not in locked[i]:
                grid[i][j] = 0

def setup():
    global moves,current_time,grid,active_cell

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:locked[i].append(j)
            if active_cell == None and grid[i][j] == 0: active_cell=[50*j,50*(i+1)]
    moves=0
    current_time=0

def load_new_set():
    sudoku_gen().generator(grid)
    setup()

Timer=threading.Thread(target=timer,daemon=True)
sudoku_gen().generator(grid)

setup()
Timer.start()
run=True
while run:

    mouse_x,mouse_y=pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_y in range(50,501):
            active_cell=[mouse_x-(mouse_x%50),mouse_y-(mouse_y%50)]

        if reset_button.button_clicked(mouse_x,mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
            reset()
        
        if game_state_button.png_button_clicked(mouse_x,mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
            if not pause:pause=True
            else:pause=False
        
        if new_set.png_button_clicked(mouse_x,mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
            load_new_set()

        if solve_button.button_clicked(mouse_x,mouse_y) and event.type == pygame.MOUSEBUTTONDOWN and Solve.stop:
            Solve.stop=False
            threading.Thread(target=Solve.solve,daemon=True).start()
            active_cell=None

        elif cancel_button.button_clicked(mouse_x,mouse_y) and event.type == pygame.MOUSEBUTTONDOWN and not Solve.stop:
            Solve.stop=True
        
        if not Solve.stop and not Solve.find_empty():
            Solve.stop=True
        
    keys=pygame.key.get_pressed()

    if active_cell != None:change_x,change_y=active_cell[0]//50,(active_cell[1]//50)-1

    if keys[pygame.K_1] and change_x not in locked[change_y] and grid[change_y][change_x] != 1:
        grid[change_y][change_x]=1
        moves+=1
    elif keys[pygame.K_2] and change_x not in locked[change_y] and grid[change_y][change_x] != 2:
        grid[change_y][change_x]=2
        moves+=1
    elif keys[pygame.K_3] and change_x not in locked[change_y] and grid[change_y][change_x] != 3:
        grid[change_y][change_x]=3
        moves+=1
    elif keys[pygame.K_4] and change_x not in locked[change_y] and grid[change_y][change_x] != 4:
        grid[change_y][change_x]=4
        moves+=1
    elif keys[pygame.K_5] and change_x not in locked[change_y] and grid[change_y][change_x] != 5:
        grid[change_y][change_x]=5
        moves+=1
    elif keys[pygame.K_6] and change_x not in locked[change_y] and grid[change_y][change_x] != 6:
        grid[change_y][change_x]=6
        moves+=1
    elif keys[pygame.K_7] and change_x not in locked[change_y] and grid[change_y][change_x] != 7:
        grid[change_y][change_x]=7
        moves+=1
    elif keys[pygame.K_8] and change_x not in locked[change_y] and grid[change_y][change_x] != 8:
        grid[change_y][change_x]=8
        moves+=1
    elif keys[pygame.K_9] and change_x not in locked[change_y] and grid[change_y][change_x] != 9:
        grid[change_y][change_x]=9
        moves+=1


    win.fill((255,255,255))
    win.blit(board,(0,50))
    draw_timer(win,current_time,380,20)
    draw_moves(win,moves,40,20)
    reset_button.draw_buttons()

    if Solve.stop: solve_button.draw_buttons()
    else: cancel_button.draw_buttons()
    
    game_state_button.png_button(resume_png,pause_png,pause)
    new_set.png_button(new_png)

    if active_cell != None: pygame.draw.rect(win,(0,100,0),(active_cell[0],active_cell[1],50,50),4)
    else: pygame.draw.rect(win,(0,100,0),(Solve.pos_x,Solve.pos_y,50,50),4)

    for i in range(9):
        for j in range(9):
            if j in locked[i]: draw_board_vals(win,grid[i][j],j,i,(255,0,0))
            else: draw_board_vals(win,grid[i][j],j,i,(0,255,0))
    
    pygame.display.update()

pygame.quit()