from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import markdownify
import requests
import os



# get sys params "Year" "day"
year = 2015
day = 3

######################################################
# if year folder doesn't exist, make a new year folder
######################################################


# Directory
directory = f"adventofcode_{year}"

# Parent Directory path
parent_dir = "C://GitHub//ADVENTOFCODE//"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# with mode 0o666
mode = 0o666
os.makedirs(path, mode=0o777, exist_ok=True)
print(f"Directory '{directory}' created")


# if day folder doesn't exist, make a new day folder



# if description.md, input.txt and day_xx.py don't exist, populate them
filenames = ["description.md", "input.txt", f"day_{str(day).rjust(2, str='0')}.py"]
for file in filenames:
    thisfile = open(file, "w").write(" ")
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
