import sys
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    from pygame.locals import QUIT

defaultsize = 20

speed = 15
deadcell = "□"
livecell = "■"

pygame.init()

class ca:
    def __init__(self, handler, initial_state):
        self.grid = initial_state
        self.updatefunc = handler.updatefunc
        self.colours = handler.cell_colours
        self.t = []
        self.t.append(initial_state)
        self.current_t = 0
        
        self.celly=defaultsize
        self.cellx=defaultsize
        
        self.windowy = self.celly*len(self.grid)
        self.windowx = self.cellx*len(self.grid[0])
        
        pygame.display.set_caption("Cellular Automata")
        self.window = pygame.display.set_mode((self.windowx,self.windowy),vsync=1)
        self.window.fill(pygame.Color(self.colours[0]))
        self.fps = pygame.time.Clock()
        
    def update(self, show=False):
        if self.current_t == len(self.t)-1:
            self.grid = self.updatefunc(self.grid)
            self.t.append(self.grid)
            self.current_t += 1
        else:
            self.current_t+=1
            self.grid = self.t[self.current_t]
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if show:
            self.show()
             
    def rewind(self, t):
        self.current_t = t
        self.grid = self.t[t]

    def show(self):
        #grid = list(map(lambda x : list(map(lambda y: deadcell if y ==0 else livecell, x)),self.grid))
        #print("\n".join(" ".join(i) for i in grid))
        for y in range(0, self.windowy, self.celly):
            for x in range(0, self.windowx, self.cellx):
                pygame.draw.rect(self.window, pygame.Color(self.colours[self.grid[y//self.celly][x//self.cellx]]), pygame.Rect(x,y,self.cellx,self.celly))
        pygame.display.update()
        self.fps.tick(speed)
        