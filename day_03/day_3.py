RAW = open("input.txt", "r").readlines()

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
LETTERS = [chr(x + 97) for x in range(26)] + [chr(x + 65) for x in range(26)]

# for part 1
priority_sum = 0

# for part 2
group = []
badges_sum = 0


def find_common_in_3(group):
    for i in group[0]:
        if (i in group[1]) and (i in group[2]):
            return i


def find_common(pack):
    midpoint = len(pack) // 2
    left, right = pack[:midpoint], pack[midpoint:]

    for i in left:
        if i in right:
            return i


def priority(letter):
    return LETTERS.index(letter) + 1


for example in RAW:
    # part 1
    priority_sum += priority(find_common(example))

    group.append(example)
    if len(group) == 3:
        # print(group, find_common_in_3(group), priority(find_common_in_3(group)))
        badges_sum += priority(find_common_in_3(group))
        group.clear()


print(f"priority_sum: \t{priority_sum}")
print(f"badges_sum: \t{badges_sum}")
