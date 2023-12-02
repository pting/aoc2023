# You can copy/paste this template to start a new day

"""DAY: PROBLEM NAME"""
import aoc.util
import re

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers in input
    pattern = re.compile(r"-?\d+")
    # x1, y1, x2, y2 = map(int, pattern.findall(l))
    # mylist = list(map(int, pattern.findall(l)))

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)

        # optionally do something with self.input, like parsing it to a more
        # useful representation and storing it in the instance

    def part_one(self) -> int:
        # TODO: actually return the answer
        return 0

    def part_two(self) -> int:
        # TODO: actually return the answer
        return 0
