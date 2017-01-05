"""
Use the BeautifulSoup and requests Python packages to print out a list of
all the article titles on the New York Times homepage (http://www.nytimes.com/)
"""


import requests
from bs4 import BeautifulSoup


url = "http://www.nytimes.com/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

articles = soup.find_all("h2", attrs={"class": "story-heading"})
# print articles
for article in articles:
    print article.text.strip()

