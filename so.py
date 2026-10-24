import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

rows = []

for book in soup.select("article.product_pod"):
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text
    stars = book.select_one("p.star-rating ")['class'][1]
    rows.append({"title": title, "price": price, 'star':stars})

table = pd.DataFrame(rows)
table.to_excel("books.xlsx", index=False)

print("finish", len(rows), "bok")

print(rows)