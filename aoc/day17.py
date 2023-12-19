# You can copy/paste this template to start a new day

"""17: PROBLEM NAME"""
import aoc.util
from heapq import heappush, heappop
from collections import defaultdict

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        self.grid = [list(map(int, line)) for line in self.lines]
        self.R = len(self.grid)
        self.C = len(self.grid[0])

    def minheat(self, start, least, most):
        queue = [(0, *start, 0,0)]
        seen = set()

        def default_value():
            return 1000000

        costs = defaultdict(default_value)
        # count = 0
        
        while queue:
            heat, r, c, pc, pr = heappop(queue)
            if r == self.R - 1 and c == self.C - 1:
                # print(count)
                return heat

            if heat > costs[(r, c)]:
                # print(heat, costs[(r, c)])
                # count += 1
                continue
            
            if (r, c, pc, pr) in seen:
                continue
            seen.add((r, c, pc, pr))

            # calculate turns only
            for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {(pc, pr), (-pc, -pr)}:
                nr, nc, h = r, c, heat
                # go straight
                for i in range(1, most + 1):
                    nr, nc = nr + dr, nc + dc
                    if 0 <= nr < self.R and 0 <= nc < self.C:
                        h += self.grid[nr][nc]
                        if i >= least:
                            costs[(nr, nc)] = h
                            heappush(queue, (h, nr, nc, dr, dc))


    def part_one(self) -> int:
        return(self.minheat((0,0), 1, 3))
    
    def part_two(self) -> int:
        return(self.minheat((0,0), 4, 10))