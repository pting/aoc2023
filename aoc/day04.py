# You can copy/paste this template to start a new day

"""04: PROBLEM NAME"""
import aoc.util
import re
from aoc.utilities import printlist

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
        self.cards = []
        for l in self.lines:
            self.cards.append(list(map(int, self.numberpattern.findall(l))))
        
        sp = self.lines[0].split(" | ")
        self.N = len(list(map(int, self.numberpattern.findall(sp[0]))))
        self.copies = [1] * len(self.lines)
        

    def part_one(self) -> int:
        ret = 0
        for row in self.cards:
            winners = set()
            winners.update(row[1:self.N])
            score = 0
            for i in range(self.N, len(row)):
                if row[i] in winners:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
            ret += score
            
        return ret
    
    def part_two(self) -> int:
        for i, row in enumerate(self.cards):
            winners = set()
            numbers = set()
            winners.update(row[1:self.N])
            numbers.update(row[self.N:])
            count = len(winners.intersection(numbers))
            # print(f"i: {i}, count = {count}")
            for j in range(i+1, i+count+1):
                self.copies[j] += self.copies[i]
                # print(f"Added {self.copies[i] * count} to {j}")
        return sum(self.copies)