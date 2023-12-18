# You can copy/paste this template to start a new day

"""18: PROBLEM NAME"""
import aoc.util
import re

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input
    numberpattern = re.compile(r"-?\d+")
    wordpattern = re.compile(r"[\w']+")
    # x1, y1, x2, y2 = map(int, pattern.findall(l))
    # mylist = list(map(int, pattern.findall(l)))
    ret1, ret2 = 0, 0

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()

        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        points = [(0, 0)]
        b = 0
        points2 = [(0, 0)]
        b2 = 0

        for line in self.lines:
            d, n, x = line.split()
            dr, dc = dirs[d]
            n = int(n)
            b += n
            r, c = points[-1]
            points.append((r + dr * n, c + dc * n))
            
            x = x[2:-1]
            dr2, dc2 = dirs["RDLU"[int(x[-1])]]
            n2 = int(x[:-1], 16)
            b2 += n2
            r2, c2 = points2[-1]
            points2.append((r2 + dr2 * n2, c2 + dc2 * n2))

        L = len(points)
        A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % L][1]) for i in range(L))) // 2
        i = A - b // 2 + 1
        self.ret1 = i + b

        L2 = len(points2)
        A2 = abs(sum(points2[j][0] * (points2[j - 1][1] - points2[(j + 1) % L2][1]) for j in range(L2))) // 2
        j = A2 - b2 // 2 + 1
        self.ret2 = j + b2
        

    def part_one(self) -> int:
        return self.ret1
    
    def part_two(self) -> int:
        return self.ret2
