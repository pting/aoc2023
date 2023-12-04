# You can copy/paste this template to start a new day

"""04: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):

    
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        lines = self.input.splitlines()
        cards = []
        N = 0
        SEQUENCE = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        
        for l in lines:
            temp = l.split()
            nums = []
            for i, v in enumerate(temp):
                if v.isdigit():
                    nums.append(int(v))
                if not N and v == "|":
                    N = i - 2
            cards.append(nums)
        
        self.copies = [1] * len(lines)
        self.ret = 0
        for i, row in enumerate(cards):
            winners = set(row[:N])
            numbers = set(row[N:])
            count = len(winners.intersection(numbers))
            if count:
                self.ret += SEQUENCE[count]

            for j in range(i+1, i+count+1):
                self.copies[j] += self.copies[i]


    def part_one(self) -> int:
        return self.ret
    
    def part_two(self) -> int:
        return sum(self.copies)