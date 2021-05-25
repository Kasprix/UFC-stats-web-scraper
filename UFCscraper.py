import requests
import pandas as pd
from bs4 import BeautifulSoup
import re


fighterURLid = []
fighterDic = []

# Opens the unique id's file
with open("UniqueIDS.txt") as file:
    fighterURLid = [line.strip() for line in file]

# Iterates through every unique ID and scrapes the fighters' page to collate their fight details
for i in fighterURLid:
    
    counter = 1
    noFights = []

    url = "http://ufcstats.com/fighter-details/" + str(i)

    response = requests.get(url)

    htmlText = response.text

    # Web Scraping for collum 1 of the career stats
    name = htmlText.split("class=\"b-content__title-highlight\">")
    namefirstsplit = name[1].split("</span>")[0]
    nameSecondSplit = namefirstsplit.split("\n\n")[0]
    nameSecondSplit.strip()
    print(nameSecondSplit.strip())

    # Scraping for the Strikes Landed Per Minute
    slpm = htmlText.split("SLpM:")
    slpmfirstsplit = slpm[1].split("</i>\n\n          ")[1]
    slpmSecondSplit = slpmfirstsplit.split("\n\n")[0]
    slpmSecondSplit.strip()
    print(slpmSecondSplit.strip())

    # Scraping for the Strike Accuracy of the fighter
    strAcc = htmlText.split("Str. Acc.:")
    strAccfirstsplit = strAcc[1].split("</i>")[1]
    strAccSecondSplit = strAccfirstsplit.split("</li>")[0]
    strAccSecondSplit.strip()
    print(strAccSecondSplit.strip())

    # Scraping for the Strikes Absorbed per  minute
    sapm = htmlText.split("SApM:")
    sapmfirstsplit = sapm[1].split("</i>")[1]
    sapmSecondSplit = sapmfirstsplit.split("</li>")[0]
    sapmSecondSplit.strip()
    print(sapmSecondSplit.strip())

    # Scraping for the percentage of strikes defended
    strDef = htmlText.split("Str. Def:")
    strDefFirstsplit = strDef[1].split("</i>")[1]
    strDefSecondSplit = strDefFirstsplit.split("</li>")[0]
    strDefSecondSplit.strip()
    print(strDefSecondSplit.strip())

    # Web Scraping for collum 2 of the career stats

    # Scraping for the Strikes Landed Per Minute
    tdAvg = htmlText.split("TD Avg.:")
    tdAvgfirstsplit = tdAvg[1].split("</i>")[1]
    tdAvgSecondSplit = tdAvgfirstsplit.split("</li>")[0]
    tdAvgSecondSplit.strip()
    print(tdAvgSecondSplit.strip())

    # Scraping for the Strikes Landed Per Minute
    tdAcc = htmlText.split("TD Acc.:")
    tdAccfirstsplit = tdAcc[1].split("</i>")[1]
    tdAccSecondSplit = tdAccfirstsplit.split("</li>")[0]
    tdAccSecondSplit.strip()
    print(tdAccSecondSplit.strip())

    # Scraping for the Strikes Landed Per Minute
    tdDef = htmlText.split("TD Def.:")
    tdDeffirstsplit = tdDef[1].split("</i>")[1]
    tdDefSecondSplit = tdDeffirstsplit.split("</li>")[0]
    tdDefSecondSplit.strip()
    print(tdDefSecondSplit.strip())

    # Scraping for the Strikes Landed Per Minute
    subAvg = htmlText.split("Sub. Avg.:")
    subAvgfirstsplit = subAvg[1].split("</i>")[1]
    subAvgSecondSplit = subAvgfirstsplit.split("</li>")[0]
    subAvgSecondSplit.strip()
    print(subAvgSecondSplit.strip())

    soup = BeautifulSoup(htmlText, "html.parser")

    for link in soup.find_all('a', href=re.compile("http://ufcstats.com/fighter-details/" + str(i))):
        noFights.append(link)

    fightno = (len(noFights))

    fighterDic.append({'Fighter Name': str(nameSecondSplit.strip().strip('\n')), 'fightno': float(fightno), 'slpmSecondSplit': float(slpmSecondSplit),
                       'strAccSecondSplit': float(strAccSecondSplit.strip().strip('%')),
                       'sapmSecondSplit': float(sapmSecondSplit),
                       'strDefSecondSplit': float(strDefSecondSplit.strip().strip('%')), 'tdAvgSecondSplit': float(tdAvgSecondSplit),
                       'tdAccSecondSplit': float(tdAccSecondSplit.strip().strip('%')), 'tdDefSecondSplit': float(tdDefSecondSplit.strip().strip('%')),
                       'subAvgSecondSplit': float(subAvgSecondSplit)})

df = pd.DataFrame(fighterDic)
df.to_csv(r'FighterData.csv',
          encoding='utf-8', index=False)
print(df)
