# You can copy/paste this template to start a new day

"""10: PROBLEM NAME"""
import aoc.util
from collections import deque

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    # Get list of all numbers or all words in input

    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        lines = self.input.splitlines()

        for r, row in enumerate(lines):
            if (c := row.find("S")) != -1:
                sr = r
                sc = c
                break

        seen = {(sr, sc)}
        q = deque([(sr, sc)])

        possibles = {"|", "-", "J", "L", "7", "F"}

        while q:
            r, c = q.popleft()
            ch = lines[r][c]

            if r > 0 and ch in "S|JL" and lines[r - 1][c] in "|7F" and (r - 1, c) not in seen:
                nxt = (r - 1, c)
                seen.add(nxt)
                q.append(nxt)
                if ch == "S":
                    possibles &= {"|", "J", "L"}
                
            if r < len(lines) - 1 and ch in "S|7F" and lines[r + 1][c] in "|JL" and (r + 1, c) not in seen:
                nxt = (r + 1, c)
                seen.add(nxt)
                q.append(nxt)
                if ch == "S":
                    possibles &= {"|", "7", "F"}

            if c > 0 and ch in "S-J7" and lines[r][c - 1] in "-LF" and (r, c - 1) not in seen:
                nxt = (r, c - 1)
                seen.add(nxt)
                q.append(nxt)
                if ch == "S":
                    possibles &= {"-", "J", "7"}

            if c < len(lines[r]) - 1 and ch in "S-LF" and lines[r][c + 1] in "-J7" and (r, c + 1) not in seen:
                nxt = (r, c + 1)
                seen.add(nxt)
                q.append(nxt)
                if ch == "S":
                    possibles &= {"-", "L", "F"}

        self.ret1 = len(seen) // 2
        
        # Need to replace S with the correct pipe, and remove any pipes not connected to our loop
        S = possibles.pop()
        grid = [list(ch if (r, c) in seen else "." for c, ch in enumerate(row)) for r, row in enumerate(lines)]
        grid[sr][sc] = S

        outside = set()

        for r, row in enumerate(grid):
            inside = False
            up = None
            for c, ch in enumerate(row):
                if ch == "|":
                    inside = not inside
                elif ch in "LF":
                    up = ch == "L"
                elif ch in "7J":
                    if ch != ("J" if up else "7"):
                        inside = not inside
                    up = None
                if not inside:
                    outside.add((r, c))
                    
        self.ret2 = len(grid) * len(grid[0]) - len(outside | seen)


    def part_one(self) -> int:
        return self.ret1
    

    def part_two(self) -> int:
        return self.ret2
