# You can copy/paste this template to start a new day

"""14: PROBLEM NAME"""
import aoc.util

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


    def move_N(self):
        grid = self.lines
        for c in range(self.L):
            drop = 0
            for r in range(len(grid)):
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
            for r in range(len(grid) - 1, -1, -1):
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
        for row in self.lines:
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
            score = 0
            for r, row in enumerate(self.lines):
                for c, ch in enumerate(row):
                    if ch == "O":
                        points.append((r, c))
                        score += self.L - r
            return tuple(points), score
        
        seen = {0: -1}
        array = [0]

        i = 0
        while True:
            i += 1
            cycle()
            key, score = buildkey()
            if key in seen:
                break
            seen[key] = i
            array.append((key, score))

        first = seen[key]
        _, score = array[(1000000000 - first) % (i - first) + first]
        return score
