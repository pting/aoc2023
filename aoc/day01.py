"""01: PROBLEM NAME"""
import aoc.util
import re

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        self.map = [
            ("one", "o1e"),
            ("two", "t2o"),
            ("three", "t3e"),
            ("four", "4"),
            ("five", "5e"),
            ("six", "6"),
            ("seven", "7n"),
            ("eight", "e8t"),
            ("nine", "n9")
        ]
        

    def part_one(self) -> int:
        sum = 0
        for l in self.lines:
            nums = []
            for c in l:
                if c.isdigit():
                    nums.append(c)
                    break
            
            for c in l[::-1]:
                if c.isdigit():
                    nums.append(c)
                    break
                    
            if nums:
                sum += int("".join(nums))

        return sum
    
    
    def part_two(self) -> int:
        sum = 0
        for l in self.lines:
            for old, new in self.map:
                l = re.sub(old, new, l)
                
            nums = []
            
            for c in l:
                if c.isdigit():
                    nums.append(c)
                    break
            
            for c in reversed(l):
                if c.isdigit():
                    nums.append(c)
                    break
                    
            if nums:
                sum += int("".join(nums))

        return sum