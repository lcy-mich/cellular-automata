import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    from pygame.locals import QUIT

defaultsize = 20

speed = 15

pygame.init()

class ca:
    def __init__(self, handler, initial_state, looparound=True, cellx= defaultsize,celly= defaultsize):
        self.grid = initial_state
        self.updatefunc = handler.updatefunc
        self.colours = handler.cell_colours
        self.t = []
        self.t.append(initial_state)
        self.current_t = 0

        self.looparound = looparound
        
        self.celly=celly
        self.cellx=cellx
        
        self.windowy = self.celly*len(self.grid)
        self.windowx = self.cellx*len(self.grid[0])
        
        pygame.display.set_caption("Cellular Automata")
        self.window = pygame.display.set_mode((self.windowx,self.windowy))
        self.fps = pygame.time.Clock()
        
    def update(self, show=False):
        if self.current_t == len(self.t)-1:
            self.grid = self.updatefunc(self.grid, self.looparound)
            self.t.append(self.grid)
            self.current_t += 1
        else:
            self.current_t+=1
            self.grid = self.t[self.current_t]
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                raise Exception("Quitting")

        if show:
            self.show()
             
    def rewind(self, t):
        if not pygame.display.get_init():
            self.window = pygame.display.set_mode((self.windowx,self.windowy))
        self.current_t = t
        self.grid = self.t[t]

    def show(self):
        #grid = list(map(lambda x : list(map(lambda y: deadcell if y ==0 else livecell, x)),self.grid))
        #print("\n".join(" ".join(i) for i in grid))
        for y in range(0, self.windowy, self.celly):
            for x in range(0, self.windowx, self.cellx):
                pygame.draw.rect(self.window, self.colours(self.grid[y//self.celly][x//self.cellx]), pygame.Rect(x,y,self.cellx,self.celly))

        pygame.display.update()
        self.fps.tick(speed)