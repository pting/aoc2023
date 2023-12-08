# You can copy/paste this template to start a new day

"""08: PROBLEM NAME"""
import aoc.util
import re
import math

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input
    wordpattern = re.compile(r"[\w']+")
    # x1, y1, x2, y2 = map(int, pattern.findall(l))
    # mylist = list(map(int, pattern.findall(l)))

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        blocks = self.input.split("\n\n")
        self.D = blocks[0]
        self.network = {}
        bl = blocks[1].split("\n")

        self.curr = []
        self.lenD = len(self.D)
        for l in bl:
            k, v1, v2 = self.wordpattern.findall(l)
            self.network[k] = (v1, v2)
            if k[-1] == "A":
                self.curr.append(k)

    def part_one(self) -> int:
        ret = 0
        curr = "AAA"
        while curr != "ZZZ":
            if self.D[ret % self.lenD] == "R":
                curr = self.network[curr][1]
            else:
                curr = self.network[curr][0]
            ret += 1
        return ret

    def part_two(self) -> int:
        ret = 0
        multiples = []
        
        for seed in self.curr:
            ret = 0
            seen = set()
            while True:
                dir = 1 if self.D[ret % self.lenD] == "R" else 0
                seed = self.network[seed][dir]
                ret += 1
                if seed[-1] == "Z":
                    seen.add(seed)
                    multiples.append(ret)
                    break

        return math.lcm(*multiples)
