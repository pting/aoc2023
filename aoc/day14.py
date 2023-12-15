# You can copy/paste this template to start a new day

"""14: PROBLEM NAME"""
import aoc.util
from aoc.utilities import printgrid

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input
    ret1, ret2 = 0, 0

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = [list(x) for x in self.input.splitlines()]
        self.L = len(self.lines[0])


    def part_one(self) -> int:
        z = [list(x) for x in zip(*self.lines)]

        for row in z:
            drop = 0
            for i in range(self.L):
                match row[i]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            row[i - drop] = "O"
                            row[i] = "."
                        self.ret1 += self.L - (i - drop)
        return self.ret1

    def move_W(self):
        for row in self.lines:
            drop = 0
            for c in range(self.L):
                match row[c]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            row[c - drop] = "O"
                            row[c] = "."


    def move_N(self):
        grid = self.lines
        for c in range(self.L):
            drop = 0
            for r in range(self.L):
                match grid[r][c]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            grid[r - drop][c] = "O"
                            grid[r][c] = "."
                    
                
    def move_S(self):
        grid = self.lines
        for c in range(self.L):
            drop = 0
            for r in range(self.L - 1, -1, -1):
                match grid[r][c]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            grid[r + drop][c] = "O"
                            grid[r][c] = "."
         

    def move_E(self):
        score = 0
        for r, row in enumerate(self.lines):
            drop = 0
            for c in range(self.L - 1, -1, -1):
                match row[c]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            row[c + drop] = "O"
                            row[c] = "."
                        score += self.L - r
        return score


    def part_two(self) -> int:
        def cycle():
            self.move_N()
            self.move_W()
            self.move_S()
            return self.move_E()
            

        seen = {0: 0}
        array = [0]

        idx = 0
        while True:
            idx += 1
            score = cycle()
            key = score
            if idx > 4:
                key = (score, array[-3])
                if key in seen:
                    break
            seen[key] = idx
            array.append(score)

        first = seen[key]
        offset = (1000000000 - first) % (idx - first)
        return(array[first + offset])
        
