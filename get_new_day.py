from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import markdownify
import requests
import os, sys

QUIT_MSG = """USAGE:
    You need to use arguments (year or y) and (day or d) at the prompt or this won't do anything.
    Day must be an integer
            one or two digits (leading 0's are ignored)
        1 <= [day | d] <= 25
    Year must be either 
            2 digits:  
        15 <= [year | y] <= (current year - 2000) *
            or 4 digits: 
        2015 <= [year | y] <= current year
         *(adventofcode doesn't have puzzles earlier that 2015)
EXAMPLE SYNTAX:
    get_new_day.py year=16 day=8            <--- this works
    get_new_day.py day=08 year=2016         <--- this works
    get_new_day.py dur day=8 year=2016      <--- this works
    get_new_day.py y=2016 d=8 poop          <--- this works
    get_new_day.py 16 8                     <--- this does NOT work
    get_new_day.py 2016 8                   <--- this does NOT work
    get_new_day.py 2016 d=8                 <--- this does NOT work
    get_new_day.py year=16 day=38           <--- this does NOT work
    get_new_day.py day=eight year=2016      <--- this does NOT work
"""

# get sys params "Year" "day"
def get_year(sys_list):
    for i in sys_list:
        if "year=" in i.lower() or "y=" in i.lower():
            y = int(i.strip().split("=")[1])
            if y >= 2015:
                return y
            elif 15 <= y < 99 and 2015 <= 2000 + y:
                return 2000 + y
    print(QUIT_MSG)
    sys.exit()


def get_day(sys_list):
    for i in sys_list:
        if "day=" in i.lower() or "d=" in i.lower():
            d = int(i.strip().split("=")[1])
            if 1 <= d <= 25:
                return d
    print(QUIT_MSG)
    sys.exit()


year = get_year(sys.argv)
day = get_day(sys.argv)
day_str = str(day).rjust(2, "0")
######################################################
# if year folder doesn't exist, make a new year folder
######################################################

# Year & Day Directory
year_dir = f"adventofcode_{year}"
day_dir = f"day_{day_str}"
path = os.path.join(year_dir, day_dir)

# Create the directory
os.makedirs(path, exist_ok=True)
print(f"Directory '{path}' created")

os.chdir(path)

# if description.md, input.txt and day_xx.py don't exist, populate them
filenames = ["description.md", "input.txt", "sample.txt", f"day_{day_str}.py"]

for file in filenames:
    if file not in os.listdir():
        thisfile = open(file, "w")

        if file == "description.md":
            thisfile.write(f"# --- Day {day_str} --- \n\n")
            thisfile.write(f"## --- Part 1 --- \n\n")
            thisfile.write(f"## --- Part 2 --- \n")

        thisfile.close()


# def get_from_advent():
#     url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
#     auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#                 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

#     git_loc = "https://github.com/login"

#     # years = [2015 + x for x in range(6)] ## 2015 - 2021
#     days = [1 + x for x in range(25)]  # always 25 days of advent

#     years = [2015]
#     for year in years:
#         for day in days:
#             input_url = f"https://adventofcode.com/{year}/day/{day}/input"
#             page = requests.get(input_url, auth=git_auth)

#             # md = markdownify.markdownify(page.content, heading_style="ATX")

#             with open(f"Day_{str(day).rjust(2,'0')}\input.txt", "w") as inputfile:
#                 inputfile.write(str(page.content))
