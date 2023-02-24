import genetics

source_file = list(open("input.txt").readlines())

LOCAL_MAP = {}
STARTING_POINT = ()
END_POINT = ()


def height_of_loc(loc, the_map):
    # HEIGHTS = {chr(x+97): x for x in range(27)}
    return LOCAL_MAP[loc][1]


# build the map and grab the special points
for row_i, row in enumerate(source_file):
    for col_i, square in enumerate(row):

        if square == "S":
            STARTING_POINT = (row_i, col_i)
        elif square == "E":
            END_POINT = (row_i, col_i)
        else:
            LOCAL_MAP[(row_i, col_i)] = ord(square)-96


def SHORTEST_DISTANCE(starting_point=STARTING_POINT, end_point=END_POINT):
    s_r, s_c = starting_point
    e_r, e_c = end_point
    return (e_r-s_r)+(e_c-s_c)


SHORTEST = SHORTEST_DISTANCE()

# I stole some code I wrote from the 2015 puzzels.
# It's always a good idea to go back and look for inspiration.


class Courier:
    def __init__(self):
        self.col_x = 0
        self.row_y = 0
        self.steps_taken = 0

    @property
    def loc(self):
        return (self.row_y, self.col_x,)

    def go(self, direction):
        if direction == "<":  # WEST
            self.col_x -= 1

        elif direction == "^":  # NORTH
            self.row_y += 1

        elif direction == ">":  # EAST
            self.col_x += 1

        elif direction == "v":  # SOUTH
            self.row_y -= 1


if __name__ == "__main__":
    print(LOCAL_MAP)
