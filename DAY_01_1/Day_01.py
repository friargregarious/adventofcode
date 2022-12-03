
this_bacpack = 0
max_cals = 0
for item in open("Day_01_Input.txt", "r").readlines():

    if (item == "\n") or (not item): ### blank line between elves
        if this_bacpack > max_cals:
            max_cals = this_bacpack
        
        this_bacpack = 0

    else:
        this_bacpack += int(item)

print(f"MAX Cals: {max_cals}")

