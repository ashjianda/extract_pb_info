import pandas as pd
from bs4 import BeautifulSoup

file = "book.html"

with open(file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

hyperlinks = [(a.get_text(strip=True), a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]

data = {
    "link_text": [text for text, href in hyperlinks],
    "hyperlink": [href for text, href in hyperlinks]
}

df = pd.DataFrame(data)

df.to_csv("hyperlinks.csv", index=False)