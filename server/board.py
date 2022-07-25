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
            


    def checkCrossElements(self, point) -> list: # Возвращать ещё local 3x3 grid
        x = point[1]
        y = point[0]
        h_elements = [self.cells[x+COLS*y]] if self.cells[x+COLS*y] != "" else []
        v_elements = [self.cells[x+COLS*y]] if self.cells[x+COLS*y] != "" else []
        pointX = x
        pointY = 0
        while pointX < 72:
            pointX += 9
            if pointX != y*COLS+x and self.cells[pointX] != "":
                v_elements.append(self.cells[pointX])
        while pointY < 9:
            item = y * COLS + pointY
            if item != y*COLS+x and self.cells[item] != "":
                h_elements.append(self.cells[item])
            pointY += 1
        elements = [h_elements, v_elements]
        if len(set(v_elements)) == len(v_elements) and \
            len(set(h_elements)) == len(h_elements):
            return True, elements
        return False, elements