# You can copy/paste this template to start a new day

"""02: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)

        self.map = {}
        for l in self.input.splitlines():
            tokens = l.split(":")
            if not tokens:
                continue
            game = int(tokens[0].split()[1])
            self.map[game] = []
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
            self.map[game].append(red)
            self.map[game].append(green)
            self.map[game].append(blue)


    def part_one(self) -> int:
        ret = 0
        for id, rounds in self.map.items():
            if rounds[0] <= 12 and rounds[1] <= 13 and rounds[2] <= 14:
                ret += id
        return ret
    
        
    def part_two(self) -> int:
        ret = 0
        for _, rounds in self.map.items():
            ret += rounds[0] * rounds[1] * rounds[2]
        return ret