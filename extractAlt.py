from bs4 import BeautifulSoup
import pandas as pd

file = "book.html"

with open(file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

alts = [(img['title'], img['src'], img['alt']) for img in soup.find_all('img')]

df = pd.DataFrame(alts, columns=["title", "src", "alt"])

df.to_csv("alts.csv", index=False)