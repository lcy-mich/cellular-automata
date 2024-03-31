from ca import ca
import sys
from gameoflife import gameoflife as gol
from belousovzhabotinsky import bz
from random import randint

def main():
    initial_state = [[(1 if randint(1,254) == 1 else 254) for _ in range(150)] for _ in range(150)]
    
    #initial_state[155][155]=initial_state[156][156]=initial_state[157][155]=initial_state[157][156]=initial_state[157][154] =  1
    
    
    #for y in range(100):
    #   initial_state[y+50][100] = 1

    #initial_state[0][0] = 250
    
    gameoflife = ca(bz, initial_state, True, 2,2)
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