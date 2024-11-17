from bs4 import BeautifulSoup
import requests
import pandas as pd
# import csv


# Variables
url = "https://musicbrainz.org/artist/79491354-3d83-40e3-9d8e-7592d58d790a"
req = requests.get(url)


# To see if a website "allows" scraping run the following command (a <Response [200]> is OK):
# print(req)

soup = BeautifulSoup(req.text, "lxml")
table = soup.find("table", class_ = "tbl release-group-list")
headers = table.find_all("th")

header_names = []
for header in headers:
    header_name = header.text
    header_names.append(header_name)

df = pd.DataFrame(columns= header_names)

rows = table.find_all("tr")

for row in rows[1:]:
    row_data = row.find_all("td")
    row_value = [tr.text for tr in row_data]    
    length = len(df)
    df.loc[length] = row_value

print(df)

# df.to_csv("Queen_albums.csv")

# To print the row values:
#    print(row_value)

# To print the row_data:
#    print(row_data)


# To print the rows:
#print(rows)

# To print the dataframe:
# print(df)


# print(header_names)


# To print the headers use the following command:
# print(headers)


# To print the whole table ("unformated") use the following command: 
# print(table)


# for cell in ars:
#     print(cell.text)

# page_to_scrape = requests.get("https://musicbrainz.org/release-group/810068af-2b3c-3e9c-b2ab-68a3f3e3787d")
# soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# albums = soup.findAll("span", attrs={"class":"mp"})

# for mp in albums:
#     print(mp.bdi)





# page_to_scrape = requests.get("https://quotes.toscrape.com")
# soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# quotes = soup.findAll("span", attrs={"class":"text"})
# authors = soup.findAll("small", attrs={"class":"author"})

# file =open("scraped_quotes.csv", "w")
# writer = csv.writer(file)

# writer.writerow(["QUOTES","AUTHORS"])

# for quote, author in zip(quotes, authors):
#     print(quote.text + " - " + author.text)
#     writer.writerow([quote.text, author.text])
# file.close()



# for quote in quotes:
#     print(quote.text)
# for author in authors:
#     print(author.text)


# sources
# https://youtu.be/T1qv3ksMDq4
# https://youtu.be/aGCyqj8nPKw