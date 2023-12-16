# You can copy/paste this template to start a new day

"""16: PROBLEM NAME"""
import aoc.util
from collections import deque
from multiprocessing import Pool

def energized(params):
    sr, sc, sd, lines = params
    q = deque()
    seen = {}
    R = len(lines)
    C = len(lines[0])
    
    q.append((sr, sc, sd))
    
    while q:
        (r, c, d) = q.popleft()
        # print(r, c, d)
        if not (r, c) in seen:
            seen[(r, c)] = []
        if d in seen[(r, c)]:
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
                        if c > 0:
                            q.append((r, c - 1, "W"))
    return(len(seen))


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input
    ret1, ret2 = 0, 0

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        
        self.ret1 = energized((0, 0, "E", self.lines))

    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        startlist = []
        R = len(self.lines)
        C = len(self.lines[0])
        for r in range(R):
            startlist.append((r, 0, "E", self.lines))
            startlist.append((r, C - 1, "W", self.lines))
        for c in range(C):
            startlist.append((0, c, "S", self.lines))
            startlist.append((R - 1, c, "N", self.lines))

        with Pool() as pool:
            self.ret2 = max(pool.map(energized, startlist))
        return self.ret2
