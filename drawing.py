# to copy the drawing to the clipboard.
import numpy as np
from PIL import Image
import pyperclip
from heart import Heart


class Drawing:
    def __init__(self):
        self.row_length = 10
        self.emojis = []

    def add_row(self, row):
        row = [str(e) for e in row]
        self.emojis.append(row)

    def add_rows(self, rows):
        rows = rows.split('\n')
        self.emojis += rows

    def __add_space_row(self):
        self.add_row([Heart("white") for _ in range(10)])

    def add_text(self, text, color="blue", background_color="white"):
        for char in text:
            self.__add_space_row()
            self.add_row(str(Letter(char, color, background_color)))
        self.__add_space_row()

    def get_drawing(self):
        string = '\n'.join([''.join(row) for row in self.emojis]) + '\n'
        pyperclip.copy(string)
        return string

    def translate_image(self, img_path):
        img = Image.open(img_path).convert('RGB')
        # we resize the image but keep the aspect ratio. this tuple is the maximum width and maximum height of the img
        img.thumbnail((10, 500))

        # uint8 -> 0 to 255
        img_pixels = np.array(img)
        """
        new_img_pixels = []
        for row in img_pixels:
            new_row = []
            i = 0
            while i < len(row):
                new_pixel = np.array(
                    [sum(row[i:i + 10][:, 0]) / 10, sum(row[i:i + 10][:, 1]) / 10,
                     sum(row[i:i + 10][:, 2]) / 10],
                    dtype=np.uint8)
                new_row.append(new_pixel)
                i += 10
            new_row = np.array(new_row, dtype=np.uint8)
            new_img_pixels.append(new_row)
        
        new_img_pixels = np.array(new_img_pixels, dtype=np.uint8)
        """
        # new_img = Image.fromarray(np.array(new_img_pixels))
        # img.show()
        # new_img.show()
        new_img_pixels = img_pixels
        for row in new_img_pixels:
            new_row = []
            for pixel in row:
                new_row.append(Heart(pixel))
            self.add_row(new_row)

    def __repr__(self):
        return self.get_drawing()


class Letter:
    letters_dict = {
        'A': "-----r----\n-----r----\n----r-r---\n----r-r---\n---r---r--\n---rrrrr--\n--r-----r-\n--r-----r-",
        'a': "---rrrr---\n-------r--\n----rrrr--\n---r---r--\n---r---r--\n----rrrr--",
        'B': "---rrr----\n---r--r---\n---r--r---\n---rrrr---\n---r---r--\n---r---r--\n---r---r--\n---rrrr---",
        'b': "---r------\n---r------\n---r------\n---rrrr---\n---r---r--\n---r---r--\n---r---r--\n---r---r--\n---rrrr---",
        'C': "",
        'c': "",
        'D': "",
        'd': "",
        'E': "",
        'e': "",
        'F': "",
        'f': "",
        'S': "----rr----\n---r--r---\n---r------\n----r-----\n-----r----\n------r---\n---r--r---\n----rr----",
        's': "----rrr---\n---r------\n---rr-----\n-----rr---\n------r---\n---rrr----",
        'U': "---r----r-\n---r----r-\n---r----r-\n---r----r-\n---r----r-\n---r----r-\n---r----r-\n----rrrr--",
        'u': "---r---r--\n---r---r--\n---r---r--\n---r---r--\n---r--rr--\n----rr-r--",
        'Y': "---r---r--\n---r---r--\n----r-r---\n----r-r---\n-----r----\n-----r----\n-----r----\n-----r----",
        'y': "---r---r--\n---r---r--\n----r-r---\n----r-r---\n-----r----\n-----r----\n----r-----\n----r-----"
    }

    def __init__(self, char, color="blue", background_color="white"):
        self.representation = self.letters_dict[char].replace("r", str(Heart(color))).replace("-", str(
            Heart(background_color)))

    def __repr__(self):
        return self.representation
