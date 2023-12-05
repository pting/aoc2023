# You can copy/paste this template to start a new day

"""05: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.seeds, *blocks = self.input.split("\n\n")
        self.seeds = list(map(int, self.seeds.split(":")[1].split()))
        self.graph = []
        for bl in blocks:
            ranges = []
            for line in bl.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))
            self.graph.append(ranges)

        self.ret1 = float("inf")
        for s in self.seeds:    
            for gr in self.graph:
                for end, start, range in gr:
                    if s >= start and s < start + range:
                        offset = s - start
                        s = end + offset
                        break
            self.ret1 = min(self.ret1, s)
        

    def part_one(self) -> int:
        return self.ret1


    def part_two(self) -> int:
        seeds = []
        for i in range(0, len(self.seeds), 2):
            seeds.append((self.seeds[i], self.seeds[i] + self.seeds[i + 1]))
        
        for ranges in self.graph:
            new = []
            while len(seeds) > 0:
                # print(seeds)
                s, e = seeds.pop()
                # print(f"popped ({s}, {e})")
                for a, b, c in ranges:
                    left = max(s, b)
                    right = min(e, b + c)
                    if left < right:
                        new.append((left - b + a, right - b + a))
                        if left > s:
                            seeds.append((s, left))
                        if e > right:
                            seeds.append((right, e))
                        break
                else:
                    new.append((s, e))
                # print(f"new = {new}")
            seeds = new
            # print(seeds)

        return (min(seeds)[0])