import pygame

class button():
    def __init__(self,win,name,size,color,x,y) -> None:
        self.win=win
        self.name=name
        self.size=size
        self.color=color
        self.x=x
        self.y=y
        self.box_size=self.size*len(self.name)//2

    def draw_buttons(self):

        btn_font=pygame.font.SysFont("comicon",self.size)
        btn_surf=btn_font.render(self.name,True,self.color)
        pygame.draw.rect(self.win,(0,0,0),(self.x,self.y,self.box_size,self.size))
        self.win.blit(btn_surf,(self.x+3,self.y+3))

    def button_clicked(self,x,y):
        if y in range(self.y,self.y+self.box_size) and x in range(self.x,self.x+self.box_size):
            return 1
        return 0

    def png_button(self,png1,png2=None,condition:bool=True):
        if condition:
            self.win.blit(png1,(self.x,self.y))
        else:
            self.win.blit(png2,(self.x,self.y))

    def png_button_clicked(self,x,y):
        if y in range(self.y,self.y+self.size) and x in range(self.x,self.x+self.size):
            return 1
        return 0

def draw_timer(win,content,x,y):
    text_font=pygame.font.SysFont("comicon",20)
    text_surf=text_font.render(f"{str(content//60)} :: {str(content%60)}",True,(0,0,0))
    win.blit(text_surf,(x,y))

def draw_moves(win,content,x,y):
    text_font=pygame.font.SysFont("comicon",20)
    text_surf=text_font.render(f"MOVES = {str(content)}",True,(0,0,0))
    win.blit(text_surf,(x,y))

def draw_board_vals(win,n,x,y,color):
    if n>0:
        text_font=pygame.font.SysFont("comicon",20)
        text_surf=text_font.render(str(n),True,color)
        win.blit(text_surf,(22+50*x,72+50*y))
