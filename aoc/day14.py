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

        L = len(z[0])
        for row in z:
            i, drop = 0, 0
            for i in range(L):
                match row[i]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            row[i - drop] = "O"
                            row[i] = "."
                            self.ret1 += L - (i - drop)
                        else:
                            self.ret1 += L - i
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
        # printgrid(self.lines)


    def move_N(self):
        grid = self.lines
        for c in range(self.L):
            drop = 0
            for r in range(len(grid)):
                # print(r, c, grid[r][c])
                match grid[r][c]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            # print(r, c, grid[r][c], "dropping to", r - drop, ",", c)
                            grid[r - drop][c] = "O"
                            grid[r][c] = "."
        # printgrid(grid)
                    
                
    def move_S(self):
        grid = self.lines
        for c in range(self.L):
            drop = 0
            for r in range(len(grid) - 1, -1, -1):
                # print(r, c, grid[r][c])
                match grid[r][c]:
                    case ".":
                        drop += 1
                    case "#":
                        drop = 0
                    case "O":
                        if drop:
                            # print(r, c, grid[r][c], "dropping to", r - drop, ",", c)
                            grid[r + drop][c] = "O"
                            grid[r][c] = "."
        # printgrid(self.lines)
         

    def move_E(self):
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


    def part_two(self) -> int:
        def cycle():
            self.move_N()
            self.move_W()
            self.move_S()
            self.move_E()

        def buildkey():
            points = []
            for r, row in enumerate(self.lines):
                for c, ch in enumerate(row):
                    if ch == "O":
                        points.append((r, c))
            return tuple(points)
        
        key = buildkey()
        seen = {key}
        array = [key]

        i = 0
        while True:
            i += 1
            cycle()
            key = buildkey()
            if key in seen:
                break
            seen.add(key)
            array.append(key)

        key = buildkey()
        first = array.index(key)
        grid = array[(1000000000 - first) % (i - first) + first]

        L = len(self.lines)
        ret2 = 0
        for r, _ in grid:
            ret2 += L - r
            
        return ret2
