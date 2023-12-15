# You can copy/paste this template to start a new day

"""15: PROBLEM NAME"""
import aoc.util
import aoc.utilities

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input
    ret1, ret2 = 0, 0
    focals = {}
    
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        
        self.steps = self.lines[0].split(",")
        boxes = [[] for _ in range(256)]
        foc = -1
        self.focals = {}
        for s in self.steps:
            self.ret1 += self.myhash(s)

            if s.find("-") > 0:
                label = s.split("-")[0]
                op = "-"
            else:
                label, foc = s.split("=")
                op = "="
            h = self.myhash(label)

            match op:
                case "-":
                    if label in boxes[h]:
                        boxes[h].remove(label)
                case "=":
                    if label not in boxes[h]:
                        boxes[h].append(label)
                    self.focals[label] = int(foc)

        self.ret2 = 0

        for b, d in enumerate(boxes, 1):
            for i, label in enumerate(d, 1):
                self.ret2 += b * i * self.focals[label]

        
    def myhash(self, s):
        val = 0
        for c in s:
            val += ord(c)
            val *= 17
            val = val % 256
        return val
        

    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        return self.ret2
