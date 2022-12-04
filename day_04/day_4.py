# In how many assignment pairs does one range fully contain the other?

RAW = open("input.txt", "r").readlines()
part_1_total, part_2_total = 0, 0


class Elf:
    def __init__(self, assignment):
        start, end = assignment.split("-")
        self.min, self.max = int(start), int(end)

def cleanup(data):
    data = data.replace("\n", "")
    return data.split(",")

def compare_elves_overlap(e1, e2):
    if e1.min <= e2.min <= e1.max or e2.min <= e1.max <= e2.max:  # left overlap
        return True
    if e2.min <= e1.min <= e2.max or e1.min <= e2.max <= e1.max:  # right overlap
        return True
    return False

def compare_elves_envelope(e1, e2):
    if (e1.min >= e2.min) and (e1.max <= e2.max):  # e1 in e2
        return True
    if (e2.min >= e1.min) and (e2.max <= e1.max):  # e2 in e1
        return True
    return False


if __name__ == "__main__":

    for i, row in enumerate(RAW):
        left, right = cleanup(row)
        elf1, elf2 = Elf(left), Elf(right)

        ## part 1
        if compare_elves_envelope(elf1, elf2):
            part_1_total += 1

        # part 2
        if compare_elves_overlap(elf1, elf2):
            part_2_total += 1

    print(f"Total part 1 envelopes : {part_1_total}.")
    print(f"Total part 2 overlaps  : {part_2_total}.")
