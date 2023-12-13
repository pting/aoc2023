# You can copy/paste this template to start a new day

"""13: PROBLEM NAME"""
import aoc.util

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

        self.ret1 = 0
        self.ret2 = 0
        for b in self.blocks:
            self.ret1 += self.fold(b) * 100
            self.ret2 += self.fold2(b) * 100
            
            z = list(zip(*b))
            self.ret1 += self.fold(z)
            self.ret2 += self.fold2(z)
            

    def fold(self, g):
        for i in range(1, len(g)):
            above = g[:i]
            above.reverse()
            below = g[i:]
            
            below = below[:len(above)]
            above = above[:len(below)]
            
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
                if count > 1:
                    break
            if count == 1:
                return i
        return 0
            
    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        return self.ret2
