# Advent of Code

## Current Year: [adventofcode.com/2022](https://adventofcode.com/2022)

View [Belleville Leader Board](https://adventofcode.com/2022/leaderboard/private/view/2588518) or [join](https://adventofcode.com/2022/leaderboard/private) pls request a code [from me](mailto:greg.denyes@gmail.com) to join.

- 2022 Day 01 [x][x] Calorie Counter
- 2022 Day 02 [x][x] Rock, Paper, Scissors
- 2022 Day 03 [x][x] Find the Common Item
- 2022 Day 04 [x][x] Camp Cleanup
- 2022 Day 05 [x][x] Supply Stacks
- 2022 Day 06 [x][x] Tuning Trouble
- 2022 Day 07 [ ][ ] No Space Left On Device
- 2022 Day 08 [x][x] Treetop Tree House
- 2022 Day 09 [x][ ] Rope Bridge
- 2022 Day 10 [x][x] Cathode-Ray Tube
- 2022 Day 11 [x][ ] Monkey in the Middle
- 2022 Day 12 [ ][ ] Hill Climbing Algorithm [3](#3)
- 2022 Day 13 [ ][ ] Distress Signal
- 2022 Day 14 [ ][ ] Regolith Reservoir
- 2022 Day 15 [ ][ ] Beacon Exclusion Zone
- 2022 Day 16 [ ][ ] Proboscidea Volcanium
- 2022 Day 17 [ ][ ] Pyroclastic Flow [4](#4)
- 2022 Day 18 [ ][ ] Boiling Boulders
- 2022 Day 19 [ ][ ] Not Enough Minerals
- 2022 Day 20 [ ][ ] Grove Positioning System
- 2022 Day 21 [ ][ ] Monkey Math
- 2022 Day 22 [ ][ ] Monkey Map
- 2022 Day 23 [ ][ ] Unstable Diffusion
- 2022 Day 24 [ ][ ] Blizzard Basin
- 2022 Day 25 [ ][ ] Full of Hot Air

[3]: my attempt at genetic algorithym.

[4]: this one looks like tetris

## Previous Year's Progress

### [adventofcode.com/2016](https://adventofcode.com/2016)

- 2016 Day 01 [x][x] No Time for a Taxicab
- 2016 Day 02 [x][x] Bathroom Security
- 2016 Day 03 [ ][ ] Squares With Three Sides

### [adventofcode.com/2015](https://adventofcode.com/2015)

- 2015 Day 01 [x][x] Not Quite Lisp
- 2015 Day 02 [x][x] I Was Told There Would Be No Math [1](#1)
- 2015 Day 03 [x][x] Perfectly Spherical Houses in a Vacuum
- 2015 Day 04 [x][x] The Ideal Stocking Stuffer [2](#2)
- 2015 Day 05 [x][x] Doesn't He Have Intern-Elves For This?
- 2015 Day 06 [x][x] Probably a Fire Hazard
- 2015 Day 07 [ ][ ] Some Assembly Required

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

`
run it as:
get_new_day.py y=2022 d=19
`

it will print to screen the usage documentation without making any changes
**WARNING!!!**
double check your args when executing!!!
This prog will overwrite any files with the names:

     "description.md"
     "input.txt"
     "sample.txt"
     f"day_{day_str}.py"
