import requests
import re
from bs4 import BeautifulSoup

fighterURL = []


# the loop iterates through all the different pages of fighters from A to Z
for i in (list(map(chr, range(97, 123)))):
    url = "http://ufcstats.com/statistics/fighters?char=" + \
        str(i) + "&page=all"

    response = requests.get(url)
    texth = response.text

    soup = BeautifulSoup(texth, 'html.parser')
    
    # The loop iterates through all collected links and parses it to only leave the fighter's unique ID to their fighter page 
    for link in soup.find_all('a', href=re.compile("http://ufcstats.com/fighter-details/")):
        text = str(link.get('href'))
        splitter = text.split("http://ufcstats.com/fighter-details/")
        Parsed = splitter[1]
        fighterURL.append(Parsed)
        print(Parsed)

    fighterURL = list(dict.fromkeys(fighterURL))

# This saves all the fighters ID's in a text file named 'UniqueIDS.txt to be used to scrape the data afterwards
with open('UniqueIDS.txt', 'w') as filehandle:
    for listitem in fighterURL:
        filehandle.write('%s\n' % listitem)
