'''
WIP
moore neighbourhood

(i) Select an integer q in the range 2 through 255. Cells may be in any of the states 1 through q.
(ii) Select two integers k1 and k2 in the range 1 through 8 and an integer g in the range 0 through 100.
(iii) In the transition from one "step" to the next the state of each cell is changed once according to rules (iv) - (vii) below:
(iv) A cell in state q changes to state 1.
(v) A cell in state 1 changes to state a/k1 + b/k2 + 1
where a is the number of neighbors of the cell which are in states 2 through q-1 and b is the number of neighbors in state q.
(vi) A cell in any of states 2 through q-1 changes to S/(9 - c) + g, 
where S is the sum of the states of the cell and its neighbors and c is the number of neighbors in state 1.
(vii) If the application of rule (v) or rule (vi) would result in a cell having a state > q then the state of that cell becomes q.
'''

q = 255
k1 = 8
k2 = 8
g = 20

def total_neighbours(neighbours):
    total = 0
    for row in neighbours:
        total += sum(row)
    return total

def count_infected(neighbours):
    total = 0
    for y in range(3):
        for x in range(3):
            if (x,y) != (1,1) and (neighbours[y][x] >=2 and neighbours[y][x] <= q-1):
                total += 1
    return total

def count_ill(neighbours):
    total = 0
    for y in range(3):
        for x in range(3):
            if (x,y) != (1,1) and (neighbours[y][x] == q):
                total += 1
    return total

def get_neighbours(x,y,grid,looparound):
    neighbours = [[0,0,0],[0,0,0],[0,0,0]]
    for y_new in range(3):
        for x_new in range(3):
            if looparound:
                y_com = ((y-1)+y_new)%len(grid)
                x_com = ((x-1)+x_new)%len(grid[0])
            else:
                y_com = ((y-1)+y_new)
                x_com = ((x-1)+x_new)
                if y_com > len(grid)-1 or x_com > len(grid)-1 or y_com < 0 or x_com < 0:
                    continue
            neighbours[y_new][x_new] = grid[y_com][x_com]
    return neighbours

class bz:

    cell_colours = lambda x : (x,x,0) if x < 255 else (255,255,0)

    def updatefunc(grid, looparound = True):
        new_grid = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for y in range(len(grid)):
            for x in range(len(grid)):
                current = grid[y][x]

                if current == q:
                    new_grid[y][x] = 1
                    continue

                neighbours = get_neighbours(x,y, grid,looparound)
                a=count_infected(neighbours) 
                b=count_ill(neighbours)
                S=total_neighbours(neighbours)

                if current == 1: 
                    new_grid[y][x] = min(a/k1 + b/k2 + 1,q)
                else: 
                    new_grid[y][x] = min(S/(9 - (8-(a+b))) + g, q)
                
        return new_grid
