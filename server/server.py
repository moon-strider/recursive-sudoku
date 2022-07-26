import requests
from flask import Flask, request
from flask_cors import CORS
from lxml import html
from bs4 import BeautifulSoup
from board import Board

app = Flask(__name__)
CORS(app)

@app.route("/getpuzzle")
def getpuzzle():
    DIFFICULTY = 1                                  #1..4
    url = f"https://nine.websudoku.com/?level={DIFFICULTY}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    board = []
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
    return {
        "board": board
    }


@app.route("/solvepuzzle", methods=['POST'])
def solvepuzzle():
    board = request.get_json()["board"]

    board[0] = "10"

    return {
        "board": board
    }


if __name__ == '__main__':
    app.run(debug=True)