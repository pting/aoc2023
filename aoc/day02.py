# You can copy/paste this template to start a new day

"""02: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.lines = self.input.splitlines()
        

    def part_one(self) -> int:
        return (sum(i for i,x in enumerate(self.lines,1)if all(x>y for x,y in zip([13,14,15],map(dict(sorted((y[0],int(x))for x,y in[q.split()for q in x.split(":")[1].replace(";",",").split(", ")])).get,"rgb")))))
    
        
    def part_two(self) -> int:
        return (sum((a:=dict(sorted((y[0],int(x))for x,y in[q.split()for q in x.split(":")[1].replace(";",",").split(", ")])))["r"]*a["g"]*a["b"]for i,x in enumerate(self.lines,1)))

    