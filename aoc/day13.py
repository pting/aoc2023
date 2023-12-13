# You can copy/paste this template to start a new day

"""13: PROBLEM NAME"""
import aoc.util
from collections import OrderedDict

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.blocks = []
        for b in self.input.split("\n\n"):
            self.blocks.append(b.splitlines())


    def fold(self, g):
        for i in range(1, len(g)):
            above = g[:i]
            above.reverse()
            below = g[i:]
            
            above = above[:len(below)]
            below = below[:len(above)]
            
            if above == below:
                return i
        return 0
    
    def fold2(self, g):
        for i in range(1, len(g)):
            above = g[:i]
            above.reverse()
            below = g[i:]
            
            count = 0
            for l1, l2 in zip(above, below):
                count += sum(1 for a, b in zip(l1, l2) if a != b)
            if count == 1:
                return i
        return 0
            
    def part_one(self) -> int:
        ret1 = 0
        for b in self.blocks:
            r = self.fold(b)
            ret1 += r * 100
            
            z = list(zip(*b))
            f = self.fold(z)
            ret1 += f
        return ret1

    def part_two(self) -> int:
        ret2 = 0
        for b in self.blocks:
            r2 = self.fold2(b)
            ret2 += r2 * 100
            
            z = list(zip(*b))
            f2 = self.fold2(z)
            ret2 += f2
        return ret2
