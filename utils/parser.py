import requests
from lxml import html
from bs4 import BeautifulSoup
from board import Board

DIFFICULTY = 1                                  #1..4
url = f"https://nine.websudoku.com/?level={DIFFICULTY}"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

board = []
# 9r9c row-first
for r in range(9):
    for c in range(9):
        container = soup.find(id=f"c{r}{c}")
        try:
            newval = container.findChild("input")['value']
            if (newval == "c"):
                continue
        except:
            newval = ''
        board.append(newval)

#print(board)

# TEST

sudoku = Board(board)
sudoku.printBoard()

# TEST