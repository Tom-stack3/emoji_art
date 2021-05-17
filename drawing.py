# to copy the drawing to the clipboard.
import pyperclip


class Drawing:
    def __init__(self):
        self.row_length = 10
        self.emojis = []

    def add_row(self, row):
        row = [str(e) for e in row]
        self.emojis.append(row)

    def get_drawing(self):
        string = '\n'.join([''.join(row) for row in self.emojis]) + '\n'
        pyperclip.copy(string)
        return string

    def __repr__(self):
        return self.get_drawing()
