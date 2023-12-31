# You can copy/paste this template to start a new day

"""12: PROBLEM NAME"""
import aoc.util
from multiprocessing import Pool

def backtrack(spr, nums, cache):
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
    
    key = (len(spr), len(nums))
    if key in cache:
        return cache[key]
    
    result = 0
    
    if spr[0] in ".?":
        result += backtrack(spr[1:], nums, cache)
        
    if spr[0] in "#?":
        # Must have enough #'s remaining in spr to cover the current number
        # and the next num[0] chars in spr must be all "#"
        # and (there are no springs left) or (the next char after next num[0] chars is not "#")
        if nums[0] <= len(spr) and spr[:nums[0]].find(".") == -1 and (nums[0] == len(spr) or spr[nums[0]] != "#"):
            result += backtrack(spr[nums[0]+1:], nums[1:], cache)

    cache[key] = result
    return result            


def process1(spring):
    seen = {}
    return backtrack(spring[0], spring[1], seen)

def process2(spring):
    seen = {}
    return backtrack(spring[0], spring[1], seen)


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input


    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        data1 = []
        data2 = []
        
        for l in self.input.splitlines():
            springs, nums = l.split()
            nums = tuple(map(int, nums.split(",")))
            # self.ret1 += self.backtrack(springs, nums)

            springs2 = springs + ("?" + springs) * 4
            nums2 = nums * 5
            # self.ret2 += backtrack(springs2, nums2)

            data1.append([springs, nums])
            data2.append([springs2, nums2])

        with Pool() as pool:
            self.ret1 = sum(pool.map(process1, data1))
            self.ret2 = sum(pool.map(process2, data2))


    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        # print(self.count)
        return self.ret2
