'''
moore neighbourhood

if cell is alive at time t, it will remain alive at time t+1 if not overcrowded or undernourished (at least two living neighbours and no more than three)
if cell is dead at time t, it will remain dead unless it has three adjacent cells.

'''
def count_neighbours(x,y,grid, looparound):
        count = 0 if grid[y][x]==0 else -1
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
                if grid[y_com][x_com] == 1:
                    count+=1
        return count

class gameoflife:

    cell_colours = lambda x : (255,255,0) if x == 1 else ((0,0,0) if x == 0 else None)

    def updatefunc(grid, looparound=True):
        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid)):
                current = grid[y][x]
                count = count_neighbours(x,y,grid, looparound)
                if current == 1: #live
                    if count == 2 or count == 3:
                        new_grid[y][x] = 1
                else: #dead
                    if count == 3:
                        new_grid[y][x] = 1
        return new_grid
