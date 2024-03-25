from ca import ca
import sys
from gameoflife import gameoflife as gol
#from random import randint

def main():
    initial_state = [[0 for _ in range(200)] for _ in range(200)]
    
    #initial_state[155][155]=initial_state[156][156]=initial_state[157][155]=initial_state[157][156]=initial_state[157][154] =  1
    
    
    for y in range(100):
        initial_state[y+50][100] = 1
    
    gameoflife = ca(gol, initial_state, 5,5)
    gameoflife.show()
    while True:
        try:
            gameoflife.update(True)
        except Exception as e:
            t = input(f"The program has quit with exception: {e}, do you choose to quit, or go back to time t? (q/t) ").strip().lower()
            if t == "q":
                sys.exit()
            elif t == "t":
                t = int(input(f"input t value (0-{len(gameoflife.t)-1}) ").strip())
                gameoflife.rewind(t)

if __name__ == "__main__":
    main()