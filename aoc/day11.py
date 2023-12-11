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
        colmask = [1] * len(self.lines[0])
        rowmask = [0] * len(self.lines[0])
        rowadd = 0
        for r, row in enumerate(self.lines):
            empty = True
            for c, ch in enumerate(row):
                if ch == '#':
                    colmask[c] = 0
                    points.append([r, c])
                    empty = False
            if empty:
                rowadd += 1
            rowmask[r] = rowadd

        coladd = 0
        for i, n in enumerate(colmask):
            if n == 1:
                coladd += 1
            colmask[i] = coladd

        self.ret1 = 0
        self.ret2 = 0
        for b, e in itertools.combinations(points, 2):
            # point = [r + rowmask[r], c + colmask[c]]
            self.ret1 += abs((b[0] + rowmask[b[0]]) - (e[0] + rowmask[e[0]])) + abs((b[1] + colmask[b[1]]) - (e[1] + colmask[e[1]]))
            self.ret2 += abs((b[0] + rowmask[b[0]] * 999999) - (e[0] + rowmask[e[0]] * 999999)) + abs((b[1] + colmask[b[1]] * 999999) - (e[1] + colmask[e[1]] * 999999))


    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        return self.ret2
