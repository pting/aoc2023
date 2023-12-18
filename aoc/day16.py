# You can copy/paste this template to start a new day

"""16: PROBLEM NAME"""
import aoc.util
from collections import deque
from multiprocessing import Pool

def energized(params):
    global lines
    global R
    global C
    sr, sc, sd = params
    q = deque()
    seen = {}
    # R = len(lines)
    # C = len(lines[0])
    
    q.append((sr, sc, sd))
    
    while q:
        (r, c, d) = q.popleft()
        # print(r, c, d)
        if not (r, c) in seen:
            seen[(r, c)] = []
        elif d in seen[(r, c)]:
            continue

        seen[(r, c)].append(d)
        
        match d:
            case "N":
                match lines[r][c]:
                    case "/":
                        if c + 1 < C:
                            q.append((r, c + 1, "E"))
                    case "\\":
                        if c > 0:
                            q.append((r, c - 1, "W"))
                    case "-":
                        if c + 1 < C:
                            q.append((r, c + 1, "E"))
                        if c > 0:
                            q.append((r, c - 1, "W"))
                    case _:
                        if "S" in seen[(r, c)]:
                            continue
                        if r > 0:
                            q.append((r - 1, c, "N"))
            case "S":
                match lines[r][c]:
                    case "/":
                        if c > 0:
                            q.append((r, c - 1, "W"))
                    case "\\":
                        if c + 1 < C:
                            q.append((r, c + 1, "E"))
                    case "-":
                        if c + 1 < C:
                            q.append((r, c + 1, "E"))
                        if c > 0:
                            q.append((r, c - 1, "W"))
                    case _:
                        if "N" in seen[(r, c)]:
                            continue
                        if r + 1 < R:
                            q.append((r + 1, c, "S"))
            case "E":
                match lines[r][c]:
                    case "/":
                        if r > 0:
                            q.append((r - 1, c, "N"))
                    case "\\":
                        if r + 1 < R:
                            q.append((r + 1, c, "S"))
                    case "|":
                        if r > 0:
                            q.append((r - 1, c, "N"))
                        if r + 1 < R:
                            q.append((r + 1, c, "S"))
                    case _:
                        if "W" in seen[(r, c)]:
                            continue
                        if c + 1 < C:
                            q.append((r, c + 1, "E"))
            case "W":
                match lines[r][c]:
                    case "/":
                        if r + 1 < R:
                            q.append((r + 1, c, "S"))
                    case "\\":
                        if r > 0:
                            q.append((r - 1, c, "N"))
                    case "|":
                        if r > 0:
                            q.append((r - 1, c, "N"))
                        if r + 1 < R:
                            q.append((r + 1, c, "S"))
                    case _:
                        if "E" in seen[(r, c)]:
                            continue
                        if c > 0:
                            q.append((r, c - 1, "W"))
    return(len(seen))

def init_p(grid):
    global lines
    global R
    global C
    lines = grid
    R = len(grid)
    C = len(grid[0])


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()

    def part_one(self) -> int:
        init_p(self.lines)
        return energized((0, 0, "E"))

    def part_two(self) -> int:
        startlist = deque()
        R = len(self.lines)
        C = len(self.lines[0])
        for r in range(R):
            startlist.append((r, 0, "E"))
            startlist.append((r, C - 1, "W"))
        for c in range(C):
            startlist.append((0, c, "S"))
            startlist.append((R - 1, c, "N"))

        with Pool(initializer=init_p, initargs=[self.lines]) as pool:
            ret2 = max(pool.map(energized, startlist))
        return ret2
