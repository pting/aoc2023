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
            rounds = tokens[1].split(";")
            for r in rounds:
                cubes = r.split(",")
                rnd = []
                for c in cubes:
                    rnd.append(c.split())
                self.map[game].append(rnd)
            

    def part_one(self) -> int:
        ret = 0
        for id, rounds in self.map.items():
            red, green, blue = 0, 0, 0
            for r in rounds:
                # print(r)
                for pull in r:
                    match pull[1]:
                        case "red":
                            red = max(red, int(pull[0]))
                        case "green":
                            green = max(green, int(pull[0]))
                        case "blue":
                            blue = max(blue, int(pull[0]))
                
            # print(f"red: {red}, green: {green}, blue: {blue}")
            if red <= 12 and green <= 13 and blue <= 14:
                ret += id
        return ret
    
        
    def part_two(self) -> int:
        ret = 0
        for id, rounds in self.map.items():
            red, green, blue = 0, 0, 0
            for r in rounds:
                # print(r)
                for pull in r:
                    match pull[1]:
                        case "red":
                            red = max(red, int(pull[0]))
                        case "green":
                            green = max(green, int(pull[0]))
                        case "blue":
                            blue = max(blue, int(pull[0]))
                
            # print(f"red: {red}, green: {green}, blue: {blue}")
            ret += red * green * blue

        return ret