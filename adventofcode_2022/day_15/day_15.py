import sys
import math

TEST = "test" in sys.argv
VERBOSE = "verbose" in sys.argv

if TEST:
    SOURCE = "sample.txt"
else:
    SOURCE = "input.txt"

this_map = []
sensor_ranges={}

# Calculating Manhattan Distance from Scratch
def manhattan_distance(point1, point2):
    # point1 = (x1, y1)
    # point1 = (x2, y2)
    # distance = |x2 - x1| + |y2 - y1|

    distance = 0
    for i1, i2 in zip(point1, point2):
        distance += abs(i2 - i1)

    return distance


def gen_data(source=SOURCE):

    raw = list(open(source).readlines())
    for row in raw:
        left_side, right_side = row.strip().split(":")
        s_x_str, s_y_str = left_side.strip("Sensor at ").split(", ")
        b_x_str, b_y_str = right_side.strip(
            "closest beacon is at ").split(", ")

        sensor = int(s_y_str.strip("y=")), int(s_x_str.strip("x="))
        beacon = int(b_y_str.strip("y=")), int(b_x_str.strip("x="))

        # print(sensor, beacon)
        yield sensor, beacon

## The range of a sensor IS the NEAREST BEACON
# 1 - calculate the distance between each sensor + beacon pair
# 2 - paint the map with the distance found at the location of each sensor
# 3 - paint all the ranges
# 4 - count the unpainted addressess

DATA = list(gen_data())

def draw_map(data=DATA):
    X, Y = 1, 0

    lower_range_of_cols = 0
    lower_range_of_rows = 0

    upper_range_of_cols = 0
    upper_range_of_rows = 0

    for sensor, beacon in data:
        if sensor[Y] > upper_range_of_rows:
            upper_range_of_rows = sensor[Y]

        if sensor[Y] < lower_range_of_rows:
            lower_range_of_rows = sensor[Y]

        if sensor[X] > upper_range_of_cols:
            upper_range_of_cols = sensor[X]

        if sensor[X] < lower_range_of_cols:
            lower_range_of_cols = sensor[X]

        if beacon[Y] > upper_range_of_rows:
            upper_range_of_rows = beacon[Y]

        if beacon[Y] < lower_range_of_rows:
            lower_range_of_rows = beacon[Y]

        if beacon[X] > upper_range_of_cols:
            upper_range_of_cols = beacon[X]

        if beacon[X] < lower_range_of_cols:
            lower_range_of_cols = beacon[X]

    ## because they may use negative integers
    # for addresses, we need to adjust them to 
    # zero because we can't index strings or 
    # lists below zero
    if VERBOSE:
        print(f"lower cols: {lower_range_of_cols}",
            f"\nlower rows: {lower_range_of_rows}")
        print(f"upper cols: {upper_range_of_cols}",
            f"\nupper rows: {upper_range_of_rows}")

    col_adjust = abs(lower_range_of_cols) 
    max_cols = upper_range_of_cols + col_adjust

    row_adjust = abs(lower_range_of_rows) 
    max_rows = upper_range_of_rows + row_adjust

    if VERBOSE:
        print(f"\n max cols: {max_cols}", f"\n max rows: {max_rows}")

    this_map = [
        ["." for col in range(max_cols)] for row in range(max_rows)
    ]

    if VERBOSE:
        for row in this_map:
            print("".join(row))
            # print(str(row))
            # print(row)

    # sensor_ranges = {}

    for sen, bea in DATA:
        s_r, s_c = sen
        b_r, b_c = bea

        # now we need to apply the adjusment to each
        # sensor and beacon address as it's painted

        if VERBOSE:
            print("Before Adjustment:", s_r, s_c, b_r, b_c,
                  f"          Row Adj:{row_adjust}", 
                  f"          Col Adj:{col_adjust}")

        s_r += row_adjust 
        b_r += row_adjust

        s_c += col_adjust
        b_c += col_adjust

        # now we put the stuff on the map

        if VERBOSE:
            print(" After Adjustment:", s_r, s_c, b_r, b_c)
            print(f"           Map is: {max_rows}x{max_cols}")
            print(f"         Measured: {len(this_map)}x{len(this_map[0])}")

        this_map[s_r][s_c] = "S"
        sensor_ranges[(s_r, s_c)] = manhattan_distance(sen, bea)

        if TEST:
            print("".join(this_map[s_r]))



if __name__ == "__main__":

    draw_map()
    with open("output.txt", "" )
    for row in this_map:
        print("".join(row))
    for item, value in sensor_ranges:
        print(item,value)
