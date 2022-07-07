import requests
from lxml import html
from bs4 import BeautifulSoup

DIFFICULTY = 1                                  #1..4
url = f"https://nine.websudoku.com/?level={DIFFICULTY}"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

board = []
# 9r9c row-first
for r in range(9):
    board.append([])
    for c in range(9):
        container = soup.find(id=f"c{r}{c}")
        try:
            newval = container.findChild("input")['value']
        except:
            newval = ''
        board.append(newval)
        
print(board)