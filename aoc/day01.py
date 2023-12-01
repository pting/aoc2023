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
            ("three", "t3ree"),
            ("four", "f4ur"),
            ("five", "f5ve"),
            ("six", "s6x"),
            ("seven", "s7ven"),
            ("eight", "e8ight"),
            ("nine", "n9ne")
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
                    
            if len(nums) > 0:
                sum += (int(nums[0]) * 10) + int(nums[-1])

        return sum
    
    
    def part_two(self) -> int:
        sum = 0
        for l in self.lines:
            first = []
            for s, d in self.map:
                indexes = [m.start() for m in re.finditer(s, l)]
                for i in indexes:
                    first.append([i, (s, d)])
            first.sort()
            
            if len(first) > 1:
                _, (s, d) = first[0]
                l = re.sub(s, d, l, 1)
                _, (s, d) = first[-1]
                l = (re.sub(s[::-1], d, l[::-1], 1))[::-1]
            if len(first) == 1:
                _, (s, d) = first[0]
                l = re.sub(s, d, l, 1)
                
            nums = []
            
            for c in l:
                if c.isdigit():
                    nums.append(c)
                    break
            
            for c in l[::-1]:
                if c.isdigit():
                    nums.append(c)
                    break
                    
            if len(nums) > 0:
                sum += (int(nums[0]) * 10) + int(nums[-1])

        return sum