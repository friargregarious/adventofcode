import sys

PART2 = "part2" in sys.argv

def build_grid(rows, cols, default=0):
    return [[default for x in range(cols)] for y in range(rows)]

def light_count(g):
    # 1 is on
    # 0 is off
    return int(sum(sum(x) for x in g))

def instructions(i: list):    
    for row in i:
        row = str(row).strip().replace("turn ", "")
        cmd, start_pos, _, end_pos = row.split(" ")
        yield cmd, start_pos, end_pos

def toggle(start, finish, grid):
    s_row, s_col = start.split(",")
    s_row = int(s_row)
    s_col = int(s_col)

    f_row, f_col = finish.split(",")
    f_row = int(f_row)
    f_col = int(f_col)

    for y_row, row in enumerate(grid):
        for x_col, col in enumerate(row):
            if (s_row <= y_row <= f_row) and (s_col <= x_col <= f_col):
                if PART2:
                    grid[y_row][x_col] += 2
                else:
                    cell = grid[y_row][x_col]
                    if cell == 1:
                        grid[y_row][x_col] = 0
                    else:
                        grid[y_row][x_col] = 1

    return grid


def activate(start, finish, grid):
    s_row, s_col = start.split(",")
    s_row = int(s_row)
    s_col = int(s_col)

    f_row, f_col = finish.split(",")
    f_row = int(f_row)
    f_col = int(f_col)

    for y_row, row in enumerate(grid):
        for x_col, col in enumerate(row):
            if (s_row <= y_row <= f_row) and (s_col <= x_col <= f_col):
                if PART2:
                    grid[y_row][x_col] += 1
                else:
                    grid[y_row][x_col] = 1

    return grid


def deactivate(start, finish, grid):
    s_row, s_col = start.split(",")
    s_row = int(s_row)
    s_col = int(s_col)

    f_row, f_col = finish.split(",")
    f_row = int(f_row)
    f_col = int(f_col)

    for y_row, row in enumerate(grid):
        for x_col, col in enumerate(row):
            if (s_row <= y_row <= f_row) and (s_col <= x_col <= f_col):
                if PART2:
                    grid[y_row][x_col] -= 1
                    if grid[y_row][x_col] < 0:
                        grid[y_row][x_col] = 0
                else:
                    grid[y_row][x_col] = 0

    return grid

if __name__ == "__main__":
    if PART2:
        outfile = "output_part2.txt"
    else:
        outfile = "output.txt"

    with open(outfile, "w") as output:
    
        TEST = "test" in sys.argv

        if TEST:
            inputs = [
                "turn on 0,0 through 9,9",  # turn them all on
                "toggle 0,0 through 9,0",  # toggle off only the leftmost col
                "turn off 4,4 through 5,5",  # turns off the 4 in the center
                "toggle 3,3 through 6,6"  # toggles on the 4 in the center, and off the square around them
            ]

            grid = build_grid(10, 10)

            for row in grid:
                print(row, file=output)

        else:
            inputs = list(open("input.txt").readlines())
            grid = build_grid(1000, 1000)

        print(
            f"Starting with: {light_count(grid)} lights are currently on", file=output)



        for cmd, start_pos, end_pos in instructions(inputs):
            if cmd == "off":
                grid = deactivate(start_pos, end_pos, grid)
            elif cmd == "on":
                grid = activate(start_pos, end_pos, grid)
            elif cmd == "toggle":
                grid = toggle(start_pos, end_pos, grid)

            if TEST:
                for row in grid:
                    print(row, file=output)

            print(f"{light_count(grid)} lights are currently on",
                  file=output, end=" ")
            print(f"cmds: {cmd} - {start_pos} to {end_pos}",
                  file=output)
