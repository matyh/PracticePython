import requests
from bs4 import BeautifulSoup


url = ("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky"
       "-humiliation-culture")

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
article = soup.find("div", {"class": "content drop-cap"})  # whole article
# list of sections in article
sections = article.find_all("section", {"class": "content-section"})

for sec in sections:
    # in each section find paragraphs
    paragraphs = sec.find_all("p")  # list of paragraphs
    for p in paragraphs:
        print p.text
