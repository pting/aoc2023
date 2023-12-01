"""01: PROBLEM NAME"""
import aoc.util
import re

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    map = [
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

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        

    def part_one(self) -> int:
        sum = 0
        nums = [0, 0]
        for l in self.lines:
            for c in l:
                if c.isdigit():
                    nums[0] = c
                    break
            
            for c in reversed(l):
                if c.isdigit():
                    nums[1] = c
                    break
                    
            if nums[0]:
                sum += int("".join(nums))
                nums[0] = 0

        return sum
    
    
    def part_two(self) -> int:
        sum = 0
        nums = [0, 0]
        for l in self.lines:
            for a, b in self.map:
                l = l.replace(a, b)

            for c in l:
                if c.isdigit():
                    nums[0] = c
                    break
            
            for c in reversed(l):
                if c.isdigit():
                    nums[1] = c
                    break
                    
            if nums[0]:
                sum += int("".join(nums))
                nums[0] = 0

        return sum
