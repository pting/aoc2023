# You can copy/paste this template to start a new day

"""DAY: PROBLEM NAME"""
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

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        

    def part_one(self) -> int:
        ret = 0
        
        return ret

    def part_two(self) -> int:
        ret = 0
        
        return ret
