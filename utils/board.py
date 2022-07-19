from audioop import cross


ROWS = COLS = 0

class Board:
    def __init__(self, cells) -> None:
        self.cells = cells


    def printBoard(self) -> None:
        for r in range(9):
            if r % 3 == 0:
                print("-"*31)
            for c in range(9):
                sep = ""
                cell = self.cells[r*9 + c] if self.cells[r*9 + c] != "" else "-"
                if c % 3 == 0:
                    sep = "|"
                print(f"{sep} {cell} ", end="")
            print("|")
        print("-"*31)
            


    def checkCrossElements(self, point) -> list: # возвращать строку + столбец
        h_elements = []
        v_elements = []
        x = point[0]
        y = point[1]
        pointX = x
        pointY = -1
        while pointX < 72:
            pointX += 9
            if pointX != x and self.cells[pointX] != "":
                v_elements.append(self.cells[pointX])
        while pointY < 9:
            item = y * COLS + pointY
            if item != y and self.cells[item] != "":
                h_elements.append(self.cells[item])
            pointY += 1
        return v_elements, h_elements
