"""
        [C]         [Q]         [V]    
        [D]         [D] [S]     [M] [Z]
        [G]     [P] [W] [M]     [C] [G]
        [F]     [Z] [C] [D] [P] [S] [W]
    [P] [L]     [C] [V] [W] [W] [H] [L]
    [G] [B] [V] [R] [L] [N] [G] [P] [F]
    [R] [T] [S] [S] [S] [T] [D] [L] [P]
    [N] [J] [M] [L] [P] [C] [H] [Z] [R]
     1   2   3   4   5   6   7   8   9 
"""

STARTING_DATA = [["N", "R", "G", "P"],
                 ["J", "T", "B", "L", "F", "G", "D", "C"],
                 ["M", "S", "V"],
                 ["L", "S", "R", "C", "Z", "P"],
                 ["P", "S", "L", "V", "C", "W", "D", "Q"],
                 ["C", "T", "N", "W", "D", "M", "S"],
                 ["H", "D", "G", "W", "P"],
                 ["Z", "L", "P", "H", "S", "C", "M", "V"],
                 ["R", "P", "F", "L", "W", "G", "Z"]]


def top_crates(data_set):
    final_code = ""
    for column in data_set:
        if len(column) > 0:
            final_code += str(column[-1])

    return final_code


if __name__ == "__main__":
    def parse_instructions():
        raw = open("input.txt","r").readlines()

        for row in raw:
            if row.startswith("move"):
                print("----> ", row, file=outfile)
                _, howmany, _, pile_from, _, pile_to = row.split(" ")
                yield int(howmany), int(pile_from) - 1, int(pile_to) - 1 ## -1 for list indexing

    my_ship = STARTING_DATA.copy()
    my_ship_p2 = STARTING_DATA.copy()

    outfile = open("output.txt","w")

    print(f"Starting point: ", file=outfile)
    for i, col in enumerate(my_ship_p2):
        print(i+1, col, file=outfile)

    print("*" * 20, file=outfile)

    for h, f, t in parse_instructions():

        # ## part 1 - 9000
        # for x in range(h):
        #     my_ship[t].append(my_ship[f].pop())


        ## part 2 - 9001
        my_ship_p2[t].extend(my_ship_p2[f][-h:]) ## commit the move of crates
        print(f"Moving from pile {f+1} to pile {t+1} crates: {my_ship_p2[f][-h:]}", file=outfile)
        my_ship_p2[f] = my_ship_p2[f][:-h] ## remove the moved crates

        for i, col in enumerate(my_ship_p2):
            print(i+1, col, file=outfile)

    # print(f"Part 1 top row of crates are: {top_crates(my_ship)}")
    print(f"Part 2 top row of crates are: {top_crates(my_ship_p2)}")
    outfile.close()
