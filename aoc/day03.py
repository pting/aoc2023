# You can copy/paste this template to start a new day

"""03: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):

    def __init__(self, input: str):
        self.scem = []
        self.sym = []
        self.stars = []

        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        lines = self.input.splitlines()
        pad = "." * (len(lines[0]) + 2)
        self.scem.append(pad)
        for r, row in enumerate(lines):
            row = "." + row + "."
            self.scem.append(row)
            for c, v in enumerate(row):
                if not v.isdigit() and not v == '.':
                    self.sym.append([r+1, c])
                    if v == '*':
                        self.stars.append([r+1, c])
        self.scem.append(pad)
        
    
    def getAdj(self, r, c):
        return [(r-1, c-1), (r-1, c), (r-1, c+1),
                (r, c-1), (r, c+1),
                (r+1, c-1), (r+1, c), (r+1, c+1)]


    def part_one(self) -> int:
        ret = 0
        seen = set()
        for row, col in self.sym:
            for r, c in self.getAdj(row, col):
                if self.scem[r][c].isdigit() and (r, c) not in seen:
                    partnum = []
                    seen.add((r, c))
                    # Traverse left and right
                    partnum.append(self.scem[r][c])
                    curr = c - 1
                    while self.scem[r][curr].isdigit():
                        seen.add((r, curr))
                        partnum.insert(0, self.scem[r][curr])
                        curr -= 1
                    curr = c + 1
                    while self.scem[r][curr].isdigit():
                        seen.add((r, curr))
                        partnum.append(self.scem[r][curr])
                        curr += 1
                    ret += int("".join(partnum))
        return ret


    def part_two(self) -> int:
        ret = 0
        for row, col in self.stars:
            seen = set()
            nums = []
            for r, c in self.getAdj(row, col):
                if self.scem[r][c].isdigit() and (r, c) not in seen:
                    partnum = []
                    seen.add((r, c))
                    # Traverse left and right
                    partnum.append(self.scem[r][c])
                    curr = c - 1
                    while self.scem[r][curr].isdigit():
                        seen.add((r, curr))
                        partnum.insert(0, self.scem[r][curr])
                        curr -= 1
                    curr = c + 1
                    while self.scem[r][curr].isdigit():
                        seen.add((r, curr))
                        partnum.append(self.scem[r][curr])
                        curr += 1
                    nums.append(int("".join(partnum)))
            if len(nums) == 2:
                ret += nums[0] * nums[1]
        return ret