# You can copy/paste this template to start a new day

"""17: PROBLEM NAME"""
import aoc.util
from heapq import heappush, heappop

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

    def part_one(self) -> int:
        seen = set()
        pq = [(0, 0, 0, 0, 0, 0)]

        while pq:
            hl, r, c, dr, dc, n = heappop(pq)
            
            if r == self.R - 1 and c == self.C - 1:
                return(hl)

            if (r, c, dr, dc, n) in seen:
                continue

            seen.add((r, c, dr, dc, n))
            
            if n < 3 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < self.R and 0 <= nc < self.C:
                    heappush(pq, (hl + self.grid[nr][nc], nr, nc, dr, dc, n + 1))

            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < self.R and 0 <= nc < self.C:
                        heappush(pq, (hl + self.grid[nr][nc], nr, nc, ndr, ndc, 1))
    
    def part_two(self) -> int:
        seen = set()
        pq = [(0, 0, 0, 0, 0, 0)]

        while pq:
            hl, r, c, dr, dc, n = heappop(pq)
            
            if r == self.R - 1 and c == self.C - 1 and n >= 4:
                return(hl)

            if (r, c, dr, dc, n) in seen:
                continue

            seen.add((r, c, dr, dc, n))
            
            if n < 10 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < self.R and 0 <= nc < self.C:
                    heappush(pq, (hl + self.grid[nr][nc], nr, nc, dr, dc, n + 1))

            if n >= 4 or (dr, dc) == (0, 0):
                for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                        nr = r + ndr
                        nc = c + ndc
                        if 0 <= nr < self.R and 0 <= nc < self.C:
                            heappush(pq, (hl + self.grid[nr][nc], nr, nc, ndr, ndc, 1))