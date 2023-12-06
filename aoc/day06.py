# You can copy/paste this template to start a new day

"""06: PROBLEM NAME"""
import aoc.util
import math

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        d = []
        self.race2 = []
        for l in self.lines:
            d.append(list(map(float, l.split(":")[1].split())))
            self.race2.append(float(l.split(":")[1].replace(" ", "")))
        
        self.races = list(zip(d[0], d[1]))

        
    def part_one(self) -> int:
        wins = 1
        for time, target in self.races:
            square = math.sqrt(time ** 2 - 4 * target)
            wins *= math.ceil((time + square) / 2 - 1) - math.floor((time - square) / 2 + 1) + 1
        return wins


    def part_two(self) -> int:
        square = math.sqrt(self.race2[0] ** 2 - 4 * self.race2[1])
        return math.ceil((self.race2[0] + square) / 2 - 1) - math.floor((self.race2[0] - square) / 2 + 1) + 1
