# You can copy/paste this template to start a new day

"""08: PROBLEM NAME"""
import aoc.util
import math

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        blocks = self.input.split("\n\n")
        self.D = []
        for d in blocks[0]:
            self.D.append(0 if d == "L" else 1)
        
        self.network = {}
        bl = blocks[1].split("\n")

        self.curr = []
        self.lenD = len(self.D)
        for l in bl:
            l = l.replace(',', '').replace('(', '').replace(')', '').replace('=', '')
            k, v1, v2 = l.split()
            self.network[k] = (v1, v2)
            if k[-1] == 'A':
                self.curr.append(k)

    def part_one(self) -> int:
        ret = 0
        curr = "AAA"
        i = 0
        while curr != "ZZZ":
            curr = self.network[curr][self.D[i]]
            ret += 1
            i += 1
            if i == self.lenD:
                i = 0
        return ret

    def part_two(self) -> int:
        ret = 0
        multiples = []
        
        for seed in self.curr:
            ret = 0
            i = 0
            while True:
                seed = self.network[seed][self.D[i]]
                ret += 1
                if seed[-1] == 'Z':
                    multiples.append(ret)
                    break
                i += 1
                if i == self.lenD:
                    i = 0

        return math.lcm(*multiples)
