import sys

if "test" in sys.argv:
    data_file = "sample.txt"
else:
    data_file = "input.txt"


def deliver(who, where):
    previous_visits = len(visits)
    visits.add(where)
    if len(visits) > previous_visits:
        who.deliveries += 1


raw_data = iter(str(open(data_file).read()))


class Courier:
    def __init__(self):
        self.col_x = 0
        self.row_y = 0
        self.deliveries = 0

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


# Part 1 #################################
raw_data = str(open(data_file).read())

santa = Courier()
visits = set()
deliver(santa, santa.loc)
for i in raw_data:
    santa.go(i)
    deliver(santa, santa.loc)

print("Part: 1")
print(f"Santa visits {len(visits)} houses at least once.")


# part 2 #################################
raw_data = iter(str(open(data_file).read()))

starting_point = (0, 0,)
santa = Courier()
robo = Courier()
visits = set()
visits.add(starting_point)  # they both start on the same spot anyway
# they both deliver to the first house
santa.deliveries, robo.deliveries = 1, 1


complete = False
while not complete:
    for i in [santa, robo]:
        try:
            i.go(next(raw_data))
            deliver(i, i.loc)
        except StopIteration as e:
            print("Last Instruction Completed")
            complete = True

        deliver(i, i.loc)

print("Part: 2")
print(f"Santa & RoboSanta visit {len(visits)} houses at least once.")
print(f"Santa delivers {santa.deliveries} presents.")
print(f"RoboSanta delivers {robo.deliveries} presents.")
