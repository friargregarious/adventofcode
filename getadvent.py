import requests
import markdownify

from requests_oauthlib import OAuth1
from bs4 import BeautifulSoup

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

git_loc = "https://github.com/login"



# years = [2015 + x for x in range(6)] ## 2015 - 2021
days = [1 + x for x in range(25)] ## always 25 days of advent

years = [2015]
for year in years:
    for day in days:
        input_url = f"https://adventofcode.com/{year}/day/{day}/input"
        page = requests.get(input_url, auth=git_auth)


        # md = markdownify.markdownify(page.content, heading_style="ATX")

        with open( f"Day_{str(day).rjust(2,'0')}\input.txt" , "w") as inputfile:
            inputfile.write(str(page.content))



