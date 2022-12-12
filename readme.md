# Advent of Code

## Current Year: [adventofcode.com/2022](https://adventofcode.com/2022)

View [Belleville Leader Board](https://adventofcode.com/2022/leaderboard/private/view/2588518) or [join](https://adventofcode.com/2022/leaderboard/private) pls request a code [from me](mailto:greg.denyes@gmail.com) to join.

- 2022 Day 01 [**] Calorie Counter
- 2022 Day 02 [**] Rock, Paper, Scissors
- 2022 Day 03 [**] Find the Common Item
- 2022 Day 04 [**] Camp Cleanup
- 2022 Day 05 [**] Supply Stacks
- 2022 Day 06 [**] Tuning Trouble
- 2022 Day 07 [__] No Space Left On Device
- 2022 Day 08 [**] Treetop Tree House
- 2022 Day 09 [*_] Rope Bridge
- 2022 Day 10 [**] Cathode-Ray Tube
- 2022 Day 11 [*_] Monkey in the Middle

## Previous Year's Progress

### [adventofcode.com/2016](https://adventofcode.com/2016)

- 2016 Day 01 [**] No Time for a Taxicab
- 2016 Day 02 [**] Bathroom Security

### [adventofcode.com/2015](https://adventofcode.com/2015)

- 2015 Day 01 [**] Not Quite Lisp
- 2015 Day 02 [**] I Was Told There Would Be No Math [1](#1)
- 2015 Day 03 [**] Perfectly Spherical Houses in a Vacuum
- 2015 Day 04 [**] The Ideal Stocking Stuffer [2](#2)
- 2015 Day 05 [**] Doesn't He Have Intern-Elves For This?
- 2015 Day 06 [**] Probably a Fire Hazard

[1]: *silly coder, of course there's math!*

[2]: BLOCK CHAIN HASHING!!!! YEAH!!!!

## Personal Projects

Writing a script to:

1. get year and day for selected puzzle from user
2. authenticate with adeventofcode.com
3. grab instructions & inputs for given day/year
4. create a new working folder for given day/year <-- **available in update 2022.12.10**
5. poplulate working folder with directions.md (markdown version of html from site)
6. poplulate working folder with input.txt (from site)
7. create python file from template for given day

This should be really cool, if I can figure out the OAuth1 portion of the project.

**update 2022.12.10**
get_new_day.py works... kinda
It will build a folder and working files from template using the given args from command line.

run it as
  >python get_new_day.py

it will print to screen the usage documentation without making any changes
**WARNING!!!**
double check your args when executing!!!
This prog will overwrite any files with the names:

  "description.md"
  "input.txt"
  "sample.txt"
  f"day_{day_str}.py"
