
import math
examples = ["22x29x19", "11x4x11", "8x10x5"]


def inputs():
    raw = open("input.txt").readlines()
    for i in raw:
        yield i


def parse(string):
    l, w, h = string.strip().split("x")
    return int(l), int(w), int(h)


def box_surface(l, w, h):
    # find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    sides = [l*w, w*h, h*l]
    return sum(sides) * 2


def box_smallest(l, w, h):
    # The elves also need a little extra paper for each present: the area of the smallest side.
    sides = [l*w, w*h, h*l]
    return min(sides)


def ribbon_length(l, w, h):
    # A present with dimensions 2x3x4
    # requires 2+2+3+3 = 10 feet of ribbon to wrap the present
    sides = [l, w, h]
    x = sides.pop(sides.index(min(sides)))
    y = sides.pop(sides.index(min(sides)))
    return (2 * x) + (2 * y)


def ribbon_bow(l, w, h):
    # A present with dimensions 2x3x4
    # requires 2*3*4 = 24 feet of ribbon for the bow
    sides = [l, w, h]
    return math.prod(sides)


# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
if __name__ == "__main__":

    # A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper
    # plus 6 square feet of slack, for a total of 58 square feet.
    l, w, h = 2, 3, 4
    a = box_surface(l, w, h)
    b = box_smallest(l, w, h)
    print(f"Test {l},{w},{h} = sum: {a}, smallest {b}")
    assert a + b == 52 + 6 == 58

    total_box_area = 0
    total_ribbon_length = 0

    for x in inputs():
        l, w, h = parse(x)
        this_box = box_surface(l, w, h)
        smallest = box_smallest(l, w, h)
        total_box_area += this_box + smallest
        # print(f"this box = {this_box} bringing our total to {total_box_area}")

        ribbon = ribbon_length(l, w, h)
        bow = ribbon_bow(l, w, h)
        total_ribbon_length += ribbon + bow

    print(f"Total paper needed: {total_box_area}")
    print(f"Total ribbon needed: {total_ribbon_length}")
