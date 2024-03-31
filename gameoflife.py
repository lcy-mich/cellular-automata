'''
moore neighbourhood

if cell is alive at time t, it will remain alive at time t+1 if not overcrowded or undernourished (at least two living neighbours and no more than three)
if cell is dead at time t, it will remain dead unless it has three adjacent cells.

'''
def count_neighbours(neighbours):
    count = -neighbours[1][1]
    for row in neighbours:
        count += sum(row)
    return count

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

class gameoflife:

    cell_colours = lambda x : (0,255,0) if x == 1 else (0,0,0)

    def updatefunc(grid, looparound=True):
        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid)):
                current = grid[y][x]
                count = count_neighbours(get_neighbours(x,y,grid,looparound))
                new_grid[y][x] = current if count == 2 else 1 if count == 3 else 0
        return new_grid
