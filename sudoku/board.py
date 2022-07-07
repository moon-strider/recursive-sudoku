from audioop import cross


ROWS = COLS = 0

class Board:
    def __init__(self, cells) -> None:
        self.cells = cells


    def checkCrossElements(self):
        cross_elements = []
        for i in range(ROWS*COLS):
            while indexV := -1 < 81:
                indexV += 9
                if indexV != i:
                    cross_elements.append(self.cells[indexV])
            while indexH := -1 < 9:
                row = int(i / ROWS)
                if item := row * COLS + indexH != i:
                    cross_elements.append(self.cells[item])
        return cross_elements
