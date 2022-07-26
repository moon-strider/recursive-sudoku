import sys
import requests
from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
from lxml import html
from bs4 import BeautifulSoup

sys.setrecursionlimit(100000)

app = Flask(__name__, static_folder='client/build', static_url_path='')
CORS(app)

board = []
ret_board = []

solve_attempts = 0

def possible(y, x, n):
    global board
    for i in range(9):
        if board[y*9 + i] == n:
            return False

    for i in range(9):
        if board[i*9 + x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[(y0 + i)*9 + x0 + j] == n:
                return False

    return True


def solve():
    global solve_attempts
    global board
    global ret_board
    solve_attempts += 1
    #print(solve_attempts)

    for y in range(9):
        for x in range(9):
            if board[y*9 + x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        board[y*9 + x] = n
                        if 0 not in board:
                            ret_board = board[::]
                        solve()
                        board[y*9 + x] = 0
                return
    return
        

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/getpuzzle")
@cross_origin()
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
                newval = int(container.findChild("input")['value'])
                if (newval == "c"):
                    continue
            except:
                newval = 0
            board.append(newval)
    return {
        "board": board
    }


@app.route("/solvepuzzle", methods=['POST'])
@cross_origin(origin='*')
def solvepuzzle():
    global board
    global ret_board
    board = request.get_json()["board"]

    print("initial board", board)

    solve()
    print("solved!")
    print(ret_board)

    return {
        "board": ret_board
    }


if __name__ == '__main__':
    app.run(debug=True)