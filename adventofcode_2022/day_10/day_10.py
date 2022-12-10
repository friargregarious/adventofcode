import sys, math

if "test" in sys.argv:
    source = "sample.txt"
elif "small" in sys.argv:
    source = "small_sample.txt"
else:
    source = "input.txt"

# each row on the screen is 40 cycles
# Cycle   1 -> ######################################## <- Cycle  40
# Cycle  41 -> ######################################## <- Cycle  80
# Cycle  81 -> ######################################## <- Cycle 120

EXAMPLE = list(open("screen.txt").readlines())

PIXEL_LIT = "#"
PIXEL_DRK = "."


def sig_strength(c, x):
    """signal strength(the cycle number multiplied by the value of the X register)"""
    return c * x


def cycleprint(t, x, c, d, r, p):
    t = str(t).ljust(3)
    x = str(x).rjust(3)
    c = str(c).rjust(3)
    d = str(d).rjust(2)
    r = str(r).rjust(6)

    print(
        f"Cycle #{c}: x vs crt:{x}/{t} delay = {d} Running cycle strength ={r}, pixel drawn = {p}"
    )


DATA = iter(list(open(source).readlines()))
x_reg = 1
x_delay, cycle = 0, 0
sig_strengths, this_row, SCREEN = [], [], []

endflag = False
while not endflag:
    ###### THIS IS THE BEGINNING OF THE CYCLE ###########################################
    # the leading edge of the cycle
    # THIS IS THE BEGINNING OF THE BEGINNING OF THE CYCLE ###############################

    cycle += 1  # new cycle starts here

    # get the command for this cycle
    noop = False
    addx = False

    if not x_delay:
        try:
            inst = str(next(DATA))
        except StopIteration as e:
            print("End of Instructions")
            endflag = True

        cmd = inst[:4]
        noop = cmd == "noop"
        addx = not noop

        if addx:
            x_delay = int(cycle)
            x_mod = int(inst.strip().split(" ")[1])

    # THIS IS THE END OF THE BEGINNING OF THE CYCLE #####################################
    # the working portion of the cycle
    # THIS IS THE BEGINNING OF THE MIDDLE OF THE CYCLE ##################################

    # On the 20th cycle AND
    # every 40 cycles after that
    #   (that is, during the 20th, 60th, 100th, 140th

    twentieth = cycle == 20
    every_forty_after = (cycle - 20) % 40 == 0

    if twentieth or every_forty_after:
        sig_strengths.append(sig_strength(cycle, x_reg))

    # PART 2 - DRAW THE PIXEL #########################
    # 1 row every 40 cycles = 40 pixels per row
    crt_pos = len(this_row) + 1
    this_pixel = PIXEL_DRK

    if crt_pos in [x_reg, x_reg + 1, x_reg+2]:  # PIXEL_DRK or PIXEL_LIT
        this_pixel = PIXEL_LIT

    this_row.append(this_pixel)
    if len(this_row) == 40:
        SCREEN.append("".join(this_row))
        this_row.clear()

    # THIS IS THE END OF THE MIDDLE OF THE CYCLE ########################################
    # the trailing edge of the cycle
    # THIS IS THE BEGINNING OF THE END OF THE CYCLE #####################################

    if cycle - x_delay not in [0, 1]:
        c_delay = "x"
    else:
        c_delay = cycle - x_delay

    cycleprint(crt_pos, x_reg, cycle, c_delay, sum(sig_strengths), this_pixel)

    if cmd == "noop":
        continue  # END CYCLE HERE, NOTHING ELSE TO SEE

    elif cycle - x_delay == 1:
        x_delay = 0
        x_reg += x_mod

    # THIS IS THE END OF THE END OF THE CYCLE ###########################################
    ###### THIS IS THE END OF THE CYCLE #################################################

print(f"\n\t\tTotal cycles: {cycle}")
print(f"\t\tTotal of sig strengths: {sum(sig_strengths)}\n\n{sig_strengths}")
print("Final Screen:")
if "test" in sys.argv:
    errors = []
    for mine, correct in zip(SCREEN, EXAMPLE):
        error = len(mine)
        for i in range(len(mine)):
            if mine[i] != correct[i]:
                error -= 1

        accuracy = int((error/40)*100)
        errors.append(accuracy)
        print(mine, correct.strip(), f"{accuracy}% accuracy")
    print(f"Average accuracy: {sum(errors)//len(errors)}%")
else:
    for row in SCREEN:
        print(row)
