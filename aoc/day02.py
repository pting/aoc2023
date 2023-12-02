# You can copy/paste this template to start a new day

"""02: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.ret1 = 0
        self.ret2 = 0

        for l in self.input.splitlines():
            tokens = l.split(":")
            if not tokens:
                continue
            id = int(tokens[0].split()[1])
            tokens[1] = tokens[1].replace(';', ',')

            red, green, blue = 0, 0, 0
            for pull in tokens[1].split(','):
                r = pull.split()
                match r[1]:
                    case "red":
                        red = max(red, int(r[0]))
                    case "green":
                        green = max(green, int(r[0]))
                    case "blue":
                        blue = max(blue, int(r[0]))
            if red <= 12 and green <= 13 and blue <= 14:
                self.ret1 += id
            self.ret2 += red * green * blue


    def part_one(self) -> int:
        return self.ret1
    
        
    def part_two(self) -> int:
        return self.ret2
    