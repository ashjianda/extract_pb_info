import pandas as pd
from bs4 import BeautifulSoup

file = "book.html"

with open(file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

embeds = [a.get('data-url', '') for a in soup.find_all('a') if a.get('data-url') 
          and 'oembed' in a.get('data-url') and 'pressbooks.library.vcu.edu' in a.get('data-url')]

df = pd.DataFrame({"embedded videos": embeds})

df.to_csv("embedded.csv", index=False)