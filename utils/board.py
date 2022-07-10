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
            


    def checkCrossElements(self, point) -> list:
        cross_elements = []
        x = point[0]
        y = point[1]
        while pointX := x < 81:
            pointX += 9
            if pointX != x:
                cross_elements.append(self.cells[pointX])
        while pointY := -1 < 9:
            if item := y * COLS + pointY != y:
                cross_elements.append(self.cells[item])
        return cross_elements
