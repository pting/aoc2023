# You can copy/paste this template to start a new day

"""12: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input


    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)

        for l in self.input.splitlines():
            springs, nums = l.split()
            nums = tuple(map(int, nums.split(",")))
            self.ret1 += self.backtrack(springs, nums)

            springs2 = springs + ("?" + springs) * 4
            nums2 = nums * 5
            self.ret2 += self.backtrack(springs2, tuple(nums2))

    ret1 = 0
    ret2 = 0
    cache = {}

    def backtrack(self, spr, nums):
        # No more springs
        if not spr:
            if not nums:
                # We found a valid solution
                return 1
            return 0

        # No more numbers 
        if not nums:
            if spr.find("#") != -1:
                # Still have springs so invalid
                return 0
            return 1
        
        key = (spr, nums)
        if key in self.cache:
            return self.cache[key]
        
        result = 0
        
        if spr[0] in ".?":
            result += self.backtrack(spr[1:], nums)
            
        if spr[0] in "#?":
            # Must have enough #'s remaining in spr to cover the current number
            # and the next num[0] chars in spr must be all "#"
            # and (there are no springs left) or (the next char after next num[0] chars is not "#")
            if nums[0] <= len(spr) and spr[:nums[0]].find(".") == -1 and (nums[0] == len(spr) or spr[nums[0]] != "#"):
                result += self.backtrack(spr[nums[0]+1:], nums[1:])

        self.cache[key] = result
        return result            


    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        # print(self.count)
        return self.ret2
