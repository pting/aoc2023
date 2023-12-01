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
        self.lines = [list(x) for x in self.input.splitlines()]
        

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
            n = len(l)
            for i, c in enumerate(l):
                if c == 'o':
                    if i + 2 < n and l[i+1] == 'n' and l[i+2] == 'e':
                        l[i+1] = '1'
                elif c == 't':
                    if i + 2 < n and l[i+1] == 'w' and l[i+2] == 'o':
                        l[i+1] = '2'
                    elif i + 4 < n and l[i+1] == 'h' and l[i+2] == 'r' and l[i+3] == 'e' and l[i+4] == 'e':
                        l[i+1] = '3'
                elif c == 'f':
                    if i + 3 < n and l[i+1] == 'o' and l[i+2] == 'u' and l[i+3] == 'r':
                        l[i+1] = '4'
                    elif i + 3 < n and l[i+1] == 'i' and l[i+2] == 'v' and l[i+3] == 'e':
                        l[i+1] = '5'
                elif c == 's':
                    if i + 2 < n and l[i+1] == 'i' and l[i+2] == 'x':
                        l[i+1] = '6'
                    elif i + 4 < n and l[i+1] == 'e' and l[i+2] == 'v' and l[i+3] == 'e' and l[i+4] == 'n':
                        l[i+1] = '7'
                elif c == 'e':
                    if i + 4 < n and l[i+1] == 'i' and l[i+2] == 'g' and l[i+3] == 'h' and l[i+4] == 't':
                        l[i+1] = '8'
                elif c == 'n':
                    if i + 3 < n and l[i+1] == 'i' and l[i+2] == 'n' and l[i+3] == 'e':
                        l[i+1] = '9'
            
            nums = [0, 0]
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
