import sys
import math

if "test" in sys.argv:
    raw_data = open("sample.txt")
elif "large" in sys.argv:
    raw_data = open("lrg_sample.txt")
else:
    raw_data = open("input.txt")


def move_head(current_loc, dir):
    row, col = current_loc

    if dir == "U":
        return (
            row + 1,
            col,
        )

    if dir == "D":
        return (
            row - 1,
            col,
        )

    if dir == "L":
        return (
            row,
            col - 1,
        )

    if dir == "R":
        return (
            row,
            col + 1,
        )


def is_far(h_loc, t_loc):
    # scan the 8 directions
    tr, tc = t_loc
    directions = []

    directions.append(t_loc)  # same spot
    directions.append((tr + 1, tc))  # n
    directions.append((tr, tc + 1))  # e
    directions.append((tr - 1, tc))  # s
    directions.append((tr, tc - 1))  # w
    directions.append((tr + 1, tc + 1))  # ne
    directions.append((tr - 1, tc + 1))  # se
    directions.append((tr - 1, tc - 1))  # sw
    directions.append((tr + 1, tc - 1))  # nw

    return h_loc not in directions


def direction(h_loc, t_loc):
    h_y, h_x = h_loc
    t_y, t_x = t_loc

    # up and down direction
    if h_y > t_y:
        # more north
        t_y += 1
    elif h_y < t_y:
        # more north
        t_y -= 1

    # left and right direction
    if h_x > t_x:
        # more north
        t_x += 1

    elif h_x < t_x:
        # more north
        t_x -= 1

    return (t_y, t_x)


def seg_move(h_loc, t_loc, seg):
    # first we figure out which direction do I need to go?
    best_spot = direction(h_loc, t_loc)

    # then we add that spot to the list of visited spots
    # but only if it's the tail!!
    if seg == TAIL:
        tail_visits.add(best_spot)
        # print("Move #", len(tail_visits), tail_visits, "\n")

    # then we return the spot so the tail can move there
    return best_spot


def draw(points):
    furthest_east = 0
    furthest_west = 0
    furthest_north = 0
    furthest_south = 0

    for r, c in points:
        if r > furthest_north:
            furthest_north = r
        if r < furthest_south:
            furthest_south = r

        if c > furthest_east:
            furthest_east = r
        if c < furthest_west:
            furthest_west = r

    max_wide = furthest_east + -furthest_west
    max_tall = furthest_north + -furthest_south

    rows = range(furthest_south - 1, furthest_north + 1)
    cols = range(furthest_west - 1, furthest_east + 1)
        
    for r, c in zip(list(rows), list(cols)):
        this_row

        if (r,c,) in points:
           screen[r][c] = "#"

    # screen = [
    #     ["." for]
    #     for row in
    # ]



    for row in screen:
        print(row)


if __name__ == "__main__":

    HEAD, TAIL = 0, 9
    rope = [(0, 0) for x in range(10)]
    tail_visits = set()
    tail_visits.add(rope[TAIL])

    for cmd in raw_data:
        dir, moves = cmd.strip().split(" ")
        for seg, location in enumerate(rope):
            for move in range(int(moves)):
                if seg == HEAD:
                    rope[HEAD] = move_head(rope[HEAD], dir)
                else:
                    p_seg = rope[seg - 1]
                    if is_far(p_seg, rope[seg]):
                        rope[seg] = seg_move(p_seg, rope[seg], seg)

    draw(tail_visits)
    print("visited spaces:", len(tail_visits))
