"""
A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

Implement the Spreadsheet class:

Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
void resetCell(String cell) Resets the specified cell to 0.
int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
"""
class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.sheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.sheet: del self.sheet[cell]

    def getValue(self, formula: str) -> int:
        segments = formula.replace("=", "").split("+")
        res = 0
        for segment in segments:
            if segment.isnumeric(): res += int(segment)
            else: res += self.sheet[segment]
        return res