import sys

TEST = "test" in sys.argv


if TEST:
    source = "sample.txt"
else:
    source = "input.txt"

def data(file=source):
    raw = str(open(file).readall())
    while True:
        for i in raw:
            yield i


SPACE_CHAR, FL_CHAR = ".", "-"
FALLING, STOPPED = "@", "#"

GAME_ROW = ["|"] + [SPACE_CHAR] * 7 + ["|"]
FLOOR = ["|"] + [FL_CHAR] * 7 + ["|"]
GAME_SPACE = [GAME_ROW] * 4 + [FLOOR]



def shift(dir=""):
    if dir == "Right":
        pass


this_stone_space = []
def stone_gen():
    stones = [
        [((0, 3), (0, 4), (0, 5), (0, 6)), [GAME_ROW.copy()]],
        [((0, 4), (1, 3), (1, 4), (1, 5), (2, 4)), [GAME_ROW.copy()] * 3],
        [((0, 5), (1, 5), (2, 3), (2, 3), (2, 3)), [GAME_ROW.copy()] * 3],
        [((0, 3), (1, 3), (2, 3), (3, 3)), [GAME_ROW.copy()] * 4],
        [((0, 3), (0, 4), (1, 3), (1, 4)), [GAME_ROW.copy()] * 2]
    ]

    points, this_stone_space = stones[0]

    for r, c in points:
        this_stone_space[r][c] = FALLING
        stones.append(stones.pop(0))

    yield this_stone_space



if __name__ == "__main__":
    round_count = 0
    target_rounds = 2022

    print("GAME_ROW:", "".join(GAME_ROW))
    print( "FLOOR:", "".join(FLOOR) )
    
    print("\n")
    for row in GAME_SPACE:
        print("".join(row))
    print("\n")

    for y in range(12):
        x = stone_gen()
        x = list(x)
        for row in x:
            # print("".join(row))
            print(row)

        print("\n*****************\n")



