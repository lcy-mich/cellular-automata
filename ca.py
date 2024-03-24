
defaultsize = 10
deadcell = "□"
livecell = "■"


class ca:
    def __init__(self, updatefunc, initial_state):
        self.grid = initial_state
        self.updatefunc = updatefunc
        self.t = []
        self.t.append(initial_state)
        self.current_t = 0
    
    def update(self, show=False):
        if self.current_t == len(self.t)-1:
            self.grid = self.updatefunc(self.grid)
            self.t.append(self.grid)
            self.current_t += 1
        else:
            self.current_t+=1
            self.grid = self.t[self.current_t]
             
        if show:
            self.show()
             
    def rewind(self, t):
        self.current_t = t
        self.grid = self.t[t]

    def show(self):
        grid = list(map(lambda x : list(map(lambda y: deadcell if y ==0 else livecell, x)),self.grid))
        print("\n".join(" ".join(i) for i in grid))
        