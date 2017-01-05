import os
import requests
from bs4 import BeautifulSoup



url = ("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky"
       "-humiliation-culture")

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
article = soup.find("div", {"class": "content drop-cap"})  # whole article
# list of sections in article
sections = article.find_all("section", {"class": "content-section"})

file_name = raw_input("Enter name of the text file where the full-text of the article will be saved: ") + ".txt"
if not os.path.exists(file_name):
    with open(file_name, 'a') as my_file:
        for sec in sections:
            # in each section find paragraphs
            paragraphs = sec.find_all("p")  # list of paragraphs
            for p in paragraphs:
                text = p.text
                my_file.write(text.encode('utf-8') + '\n')
else:
    print "File named %s already exists." % file_name
