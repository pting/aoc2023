# You can copy/paste this template to start a new day

"""07: PROBLEM NAME"""
import aoc.util

# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        record = []

        for l in self.input.splitlines():
            hand = l.split()
            n = int(hand[1])
            record.append([hand[0], n])

        record.sort(key=self.score1)
        self.ret1 = 0
        for i, [_, n] in enumerate(record):
            self.ret1 += (i+1) * n

        record.sort(key=self.score2)
        self.ret2 = 0
        for i, [_, n] in enumerate(record):
            self.ret2 += (i+1) * n



    order1 = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    order2 = {"A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}

    def score1(self, s):
        temp = []
        count = {}
        for c in s[0]:
            temp.append(self.order1[c])
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        i = 1
        score = 0
        for n in reversed(temp):
            score += n * i
            i *= 13

        for n in count.values():
            if n == 5:
                score += 20000000
                break
            if n == 4:
                score += 10000000
                break
            if n == 3:
                score += 5000000
            if n == 2:
                score += 1000000
        return score


    def score2(self, s):
        temp = []
        count = {}
        for c in s[0]:
            temp.append(self.order2[c])
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        i = 1
        score = 0
        for n in reversed(temp):
            score += n * i
            i *= 13

        cards = []
        for card, n in count.items():
            if card != "J":
                cards.append(n)
        cards.sort(reverse=True)
        jokers = count["J"] if "J" in count else 0

        if jokers < 5:
            cards[0] += jokers
        else:
            score += 20000000
            return score
                
        for n in cards:
            if n == 5:
                score += 20000000
                break
            if n == 4:
                score += 10000000
                break
            if n == 3:
                score += 5000000
            if n == 2:
                score += 1000000
        return score


    def part_one(self) -> int:
        return self.ret1
 
    def part_two(self) -> int:
         return self.ret2
