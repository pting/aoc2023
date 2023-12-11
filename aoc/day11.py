# You can copy/paste this template to start a new day

"""11: PROBLEM NAME"""
import aoc.util
import aoc.utilities
import itertools

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        
        points = []
        points2 = []
        colmask = [1] * len(self.lines[0])
        rowadd = 0
        for r, row in enumerate(self.lines):
            empty = True
            for c, ch in enumerate(row):
                if ch == '#':
                    colmask[c] = 0
                    points.append([r + rowadd, c])
                    points2.append([r + rowadd * 999999, c])
                    empty = False
            if empty:
                rowadd += 1
        
        coladd = 0
        for i, n in enumerate(colmask):
            if n == 1:
                coladd += 1
            colmask[i] = coladd
        
        newpoints = []
        newpoints2 = []
        for r, c in points:
            newpoints.append([r, c + colmask[c]])

        for r, c in points2:
            newpoints2.append([r, c + (colmask[c] * 999999)])
        
        self.ret1 = 0
        for begin, end in itertools.combinations(newpoints, 2):
            self.ret1 += abs(begin[0] - end[0]) + abs(begin[1] - end[1])
            
        self.ret2 = 0
        for begin, end in itertools.combinations(newpoints2, 2):
            self.ret2 += abs(begin[0] - end[0]) + abs(begin[1] - end[1])
           
        

    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        return self.ret2
