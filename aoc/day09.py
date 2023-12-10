# You can copy/paste this template to start a new day

"""09: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        self.ret1 = 0
        self.ret2 = 0
        for line in self.lines:
            l = list(map(int, line.split()))
            diffs = []
            diffs.append(l)
            while True:
                d = []
                prev = None
                same = True
                for n in diffs[-1]:
                    if prev == None:
                        prev = n
                        continue
                    d.append(n - prev)
                    if same and prev != n:
                        same = False
                    prev = n
                diffs.append(d)
                if same:
                    break
            
            first = []
            for d in reversed(diffs):
                self.ret1 += d[-1]
                first.append(d[0])

            f = first[0]
            for i in range(1, len(first)):
                f = first[i] - f
            self.ret2 += f
            
            
    def part_one(self) -> int:
        return self.ret1

    def part_two(self) -> int:
        return self.ret2
