"""
Utility functions for Advent of Code
"""

def printgrid(gr):
    print()
    for r in gr:
        print(r)
    print()

def printdict(d):
    for k, v in d.items():
        print(f"{k}: {v}")

def printlist(d):
    for v in d:
        print(v)

def getAdjacent(r: int, c: int) -> list:
    """
    Returns list of adjacent grid coordinates
    """
    return [(r-1, c-1), (r-1, c), (r-1, c+1),
            (r, c-1), (r, c+1),
            (r+1, c-1), (r+1, c), (r+1, c+1)]


def inbounds(r: int, c:int, grid:list) -> bool:
    """
    Is (r, c) inbounds of the grid
    """
    return (r >= 0 and r < len(grid) and c >= 0 and c < len(grid))


### Movement functions

def moveL(node):
    node[0] -= 1

def moveR(node):
    node[0] += 1

def moveU(node):
    node[1] += 1

def moveD(node):
    node[1] -= 1

movement = {
    "L": moveL,
    "R": moveR,
    "U": moveU,
    "D": moveD,
}

def make_move(dir):
    return movement[dir]

alldirsdiag = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

alldirs3d = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1],
]

# See 2022 Day22
DIRECTION = {
    "N": (-1, 0, 3, "^"),
    "S": (1, 0, 1, "v"),
    "E": (0, 1, 0, ">"),
    "W": (0, -1, 2, "<"),
}

TURN = {
    "L": {
        "N": "W",
        "S": "E",
        "E": "N",
        "W": "S",
    },
    "R": {
        "N": "E",
        "S": "W",
        "E": "S",
        "W": "N",
    },
}
