from ca import ca
from sys import exit
from argparse import ArgumentParser
from gameoflife import gameoflife as gol
from belousovzhabotinsky import bz as nilered
from random import randint
from enum import Enum, auto
from typing import Any

class CellType(Enum):
    NileRed = auto()
    GameOfLife = auto()

    @property
    def aliases(self) -> list[str]:
        return {
            CellType.NileRed: ["nilered", "zhaboutinsky", "bz", "belousov-zhaboutinsky", "belousov", "owo"],
            CellType.GameOfLife: ["gol", "life", "conway", "conways"],
        }[self]
    
    def class_of(self) -> Any:
        return {
             CellType.NileRed: nilered,
             CellType.GameOfLife: gol,
        }[self]

def main(catype):
    initial_state = [[(1 if randint(1,200) == 1 else 150) for _ in range(150)] for _ in range(150)]

    cell = None
    for celltype in CellType:
        if catype in celltype.aliases:
            cell = celltype.class_of()
            break
    
    #initial_state[155][155]=initial_state[156][156]=initial_state[157][155]=initial_state[157][156]=initial_state[157][154] =  1
    
    
    #for y in range(100):
    #   initial_state[y+50][100] = 1

    #initial_state[0][0] = 250
    
    cellularauto = ca(cell, initial_state, True, 2,2)
    cellularauto.show()

    while True:
        try:
            cellularauto.update(True)
        except Exception as e:
            t = input(f"The program has quit with exception: {e}, do you choose to quit, or go back to time t? (q/t) ").strip().lower()
            if t == "q":
                 exit()
            elif t == "t":
                t = int(input(f"input t value (0-{len(cellularauto.t)-1}) ").strip())
                cellularauto.rewind(t)

if __name__ == "__main__":
    parser = ArgumentParser(prog="mmmm celltomata", description="cellularly au tomota 🍅")
    parser.add_argument("catype", help=f"The type of cellular automata.", choices=sum((x.aliases for x in CellType), start=[]))
    args = parser.parse_args()
    main(args.catype)