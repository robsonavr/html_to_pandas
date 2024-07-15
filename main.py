import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://www.dicionariopopular.com/adedonha-temas-respostas-stop/'
r = requests.get(url)

df = pd.concat([x.set_index('LETRA').T for x in pd.read_html(r.content) if len(x) == 26], ignore_index=True)

soup  = BeautifulSoup(r.content, 'lxml')

df.index = [x.text for x in soup.find_all('h2') if '. ' in str(x)]

print(df.head())

df.to_excel('data.xlsx')

