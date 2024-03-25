'''
WIP
moore neighbourhood

(i) If the cell is healthy (state 0) then its new state is [a/k1] + [b/k2], 
where a is the number of infected cells among its eight neighbors, 
b is the number of ill cells among its neighbors, 
and k1 and k2 are constants. Here "[]" means the integer part of the number enclosed, so that, for example, [7/3] = [2+1/3] = 2.

(ii) If the cell is ill (state n) then it miraculously becomes healthy (i.e., its state becomes 0).

(iii) If the cell is infected (state other than 0 and n) 
then its new state is [s/(a+b+1)] + g, where a and b are as above, 
s is the sum of the states of the cell and of its neighbors and g is a constant.
'''

def count_neighbours(x,y,grid,state_type):
        count = 0
        for y_new in range(3):
            for x_new in range(3):
                y_com = ((y-1)+y_new)%len(grid)
                x_com = ((x-1)+x_new)%len(grid[0])
                if grid[y_com][x_com] == 1 and x_com != x and y_com != y:
                    count+=1
        return count

class bz:

    cell_colours = lambda x : (0,255,0) if x == 0 else (() if x != 1 or x!=0)

    def updatefunc(grid):
        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid)):
                current = grid[y][x]
                
        return new_grid
