# setup
this_backpack = 0
max_cals = 0
cal_totals = []  # for part 2

# body of work
for item in open("Input.txt", "r").readlines():

    if (item == "\n") or (not item):  ### blank line between elves
        ##### This section is for part 2
        cal_totals.append(this_backpack)

        if len(cal_totals) > 3:
            cal_totals.pop(cal_totals.index(min(cal_totals)))
        ##### End part 2

        if this_backpack > max_cals:
            max_cals = this_backpack

        this_backpack = 0

    else:
        this_backpack += int(item)


# report
print(f"MAX Cals: \t{max_cals}")
print(f"Sum of Top 3: \t{sum(cal_totals)}")
