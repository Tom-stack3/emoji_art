import numpy as np
from PIL import Image
from heart import Heart
# to copy the drawing to the clipboard.
import pyperclip

TRANSPARENT_BACKGROUND_COLOR = "white"
DEFAULT_BACKGROUND_COLOR = "white"
DEFAULT_TEXT_COLOR = "blue"
DEFAULT_AMOGUS_COLOR = "red"


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

    def __add_space_row(self, background_color=DEFAULT_BACKGROUND_COLOR):
        self.add_row([Heart(background_color) for _ in range(10)])

    def add_text(self, text, color=DEFAULT_TEXT_COLOR, background_color=DEFAULT_BACKGROUND_COLOR):
        for char in text:
            self.__add_space_row(background_color)
            self.add_row(str(Letter(char, color, background_color)))
        self.__add_space_row(background_color)

    def draw_amogus(self, color=DEFAULT_AMOGUS_COLOR, background_color=DEFAULT_BACKGROUND_COLOR):
        self.add_rows(str(Amogus(color, background_color)))

    def get_drawing(self):
        string = '\n'.join([''.join(row) for row in self.emojis]) + '\n'
        # copy the drawing to the clipboard.
        pyperclip.copy(string)
        return string

    def translate_image(self, img_path, use_nearest_filter=True):
        img = Image.open(img_path)

        # Create a white rgba background
        new_image = Image.new("RGBA", img.size, TRANSPARENT_BACKGROUND_COLOR)
        # Paste the image on the background.
        new_image.paste(img, (0, 0), img.convert('RGBA'))

        img = new_image.convert('RGB')
        # we resize the image but keep the aspect ratio. this tuple is the maximum width and maximum height of the img.
        if use_nearest_filter:
            # we use the NEAREST filter to keep the sharpness of the edges.
            img.thumbnail((10, 500), Image.NEAREST)
        else:
            img.thumbnail((10, 500))

        img_pixels = np.array(img)

        # if you want to see the resized photo
        # img.show()

        new_img_pixels = img_pixels
        for row in new_img_pixels:
            new_row = []
            for pixel in row:
                new_row.append(Heart(pixel))
            self.add_row(new_row)

    def __repr__(self):
        return self.get_drawing()

    # not used, because doesn't resize and keeps the proportion.
    @staticmethod
    def __old_method(img_pixels):
        # uint8 -> 0 to 255
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

        return np.array(new_img_pixels, dtype=np.uint8)


class Amogus:
    text_representation = "----------\n----rrrr--\n---rrrrrr-\n---rreeee-\n-rrrreeee-\n-rrrreeee-\n-rrrrrrrr-\n" \
                          "-rrrrrrrr-\n-rrrrrrrr-\n---rrrrrr-\n---rr-rr--\n---rr-rr--\n----------"

    def __init__(self, color=DEFAULT_AMOGUS_COLOR, background_color=DEFAULT_BACKGROUND_COLOR):

        self.representation = self.text_representation.replace("r", str(Heart(color))).replace("-", str(
            Heart(background_color)))
        if color == "blue":
            self.representation = self.representation.replace("e", "🌐")
        else:
            self.representation = self.representation.replace("e", "💙")

    def __repr__(self):
        return self.representation


class Letter:
    letters_dict = {
        ' ': "----------",
        'A': "-----r----\n-----r----\n----r-r---\n----r-r---\n---r---r--\n---rrrrr--\n--r-----r-\n--r-----r-",
        'a': "---rrrr---\n-------r--\n----rrrr--\n---r---r--\n---r---r--\n----rrrr--",
        'B': "---rrr----\n---r--r---\n---r--r---\n---rrrr---\n---r---r--\n---r---r--\n---r---r--\n---rrrr---",
        'b': "---r------\n---r------\n---r------\n---rrrr---\n---r---r--\n---r---r--\n---r---r--\n---r---r--\n---rrrr---",
        'C': "----rrr---\n---r---r--\n--r-------\n--r-------\n--r-------\n--r-------\n---r---r--\n----rrr---",
        'c': "----rrr---\n---r------\n---r------\n---r------\n---r------\n----rrr---",
        'D': "---rrrr---\n---r---r--\n---r----r-\n---r----r-\n---r----r-\n---r----r-\n---r---r--\n---rrrr---",
        'd': "-------r--\n-------r--\n-------r--\n----rrrr--\n---r---r--\n---r---r--\n---r---r--\n---r---r--\n----rrrr--",
        'E': "---rrrr---\n---r------\n---r------\n---rrrr---\n---r------\n---r------\n---r------\n---rrrr---",
        'e': "----rr----\n---r--r---\n---rrrr---\n---r------\n---r------\n----rrr---",
        'F': "---rrrr---\n---r------\n---r------\n---rrrr---\n---r------\n---r------\n---r------\n---r------",
        'f': "-----rr---\n----r-----\n----r-----\n---rrrr---\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----",
        'G': "----rrr---\n---r---r--\n--r-------\n--r-------\n--r--rrr--\n--r----r--\n---r---r--\n----rrr---",
        'g': "----rrrr--\n---r--r---\n---r--r---\n----rr----\n---r------\n----rrr---\n---r---r--\n---rrrr---",
        'H': "--r----r--\n--r----r--\n--r----r--\n--rrrrrr--\n--r----r--\n--r----r--\n--r----r--\n--r----r--",
        'h': "---r------\n---r------\n---r------\n---r-rr---\n---rr--r--\n---r---r--\n---r---r--\n---r---r--\n---r---r--",
        'I': "----r-----\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----",
        'i': "----r-----\n----------\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----",
        'J': "-----r----\n-----r----\n-----r----\n-----r----\n-----r----\n-----r----\n-----r----\n---rr-----",
        'j': "-----r----\n----------\n-----r----\n-----r----\n-----r----\n-----r----\n-----r----\n-----r----\n---rr-----",
        'K': "---r---r--\n---r--r---\n---r-r----\n---rr-----\n---r-r----\n---r--r---\n---r--r---\n---r---r--",
        'k': "---r------\n---r------\n---r--r---\n---r-r----\n---rr-----\n---r-r----\n---r-r----\n---r--r---",
        'L': "---r------\n---r------\n---r------\n---r------\n---r------\n---r------\n---r------\n---rrrr---",
        'l': "---r------\n---r------\n---r------\n---r------\n---r------\n---r------\n---r------\n---r------\n---r------",
        'M': "-rr----rr-\n-rr----rr-\n-r-r--r-r-\n-r-r--r-r-\n-r-r--r-r-\n-r-r--r-r-\n-r--rr--r-\n-r--rr--r-",
        'm': "-r-rr-rr--\n-rr--r--r-\n-r---r--r-\n-r---r--r-\n-r---r--r-\n-r---r--r-",
        'N': "---rr---r-\n---rr---r-\n---r-r--r-\n---r-r--r-\n---r--r-r-\n---r--r-r-\n---r---rr-\n---r---rr-",
        'n': "---r-rr---\n---rr--r--\n---r---r--\n---r---r--\n---r---r--\n---r---r--",
        'O': "----rrr---\n---r---r--\n--r-----r-\n--r-----r-\n--r-----r-\n--r-----r-\n---r---r--\n----rrr---",
        'o': "----rrr---\n---r---r--\n---r---r--\n---r---r--\n---r---r--\n----rrr---",
        'P': "---rrrr---\n---r---r--\n---r---r--\n---r---r--\n---rrrr---\n---r------\n---r------\n---r------",
        'p': "---rrrr---\n---r---r--\n---r---r--\n---r---r--\n---r---r--\n---rrrr---\n---r------\n---r------",
        'Q': "----rrr---\n---r---r--\n--r-----r-\n--r-----r-\n--r-----r-\n--r-----r-\n---r---r--\n----rrrr--\n--------rr",
        'q': "----rrrr--\n---r---r--\n---r---r--\n---r---r--\n---r---r--\n----rrrr--\n-------r--\n-------r--",
        'R': "---rrrr---\n---r---r--\n---r---r--\n---r---r--\n---rrrr---\n---r--r---\n---r---r--\n---r---r--",
        'r': "---r-rr---\n---rr-----\n---r------\n---r------\n---r------\n---r------",
        'S': "----rr----\n---r--r---\n---r------\n----r-----\n-----r----\n------r---\n---r--r---\n----rr----",
        's': "----rrr---\n---r------\n---rr-----\n-----rr---\n------r---\n---rrr----",
        'T': "--rrrrr---\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----\n----r-----",
        't': "----r-----\n----r-----\n---rrrr---\n----r-----\n----r-----\n----r-----\n----r-----\n-----rr---",
        'U': "---r----r-\n---r----r-\n---r----r-\n---r----r-\n---r----r-\n---r----r-\n---r----r-\n----rrrr--",
        'u': "---r---r--\n---r---r--\n---r---r--\n---r---r--\n---r--rr--\n----rr-r--",
        'V': "--r-----r-\n--r-----r-\n---r---r--\n---r---r--\n----r-r---\n----r-r---\n-----r----\n-----r----",
        'v': "---r---r--\n---r---r--\n----r-r---\n----r-r---\n-----r----\n-----r----",
        'W': "-rr--rr--r\n--r--rr--r\n--r-rrr--r\n--r-r-r-r-\n---r---r--\n---r---r--\n---r---r--",
        'w': "-r---r---r\n-r---r---r\n--r-r-r-r-\n--r-r-r-r-\n---r---r--\n---r---r--",
        'X': "--r-----r-\n---r---r--\n----r-r---\n-----r----\n-----r----\n----r-r---\n---r---r--\n--r-----r-",
        'x': "---r---r--\n----r-r---\n-----r----\n-----r----\n----r-r---\n---r---r--",
        'Y': "---r---r--\n---r---r--\n----r-r---\n----r-r---\n-----r----\n-----r----\n-----r----\n-----r----",
        'y': "---r---r--\n---r---r--\n----r-r---\n----r-r---\n-----r----\n-----r----\n----r-----\n----r-----",
        'Z': "---rrrrrr-\n--------r-\n-------r--\n------r---\n-----r----\n----r-----\n---r------\n---rrrrrr-",
        'z': "---rrr----\n-----r----\n----r-----\n----r-----\n---r------\n---rrr----",
    }

    def __init__(self, char, color=DEFAULT_TEXT_COLOR, background_color=DEFAULT_BACKGROUND_COLOR):
        self.representation = self.letters_dict[char].replace("r", str(Heart(color))).replace("-", str(
            Heart(background_color)))

    def __repr__(self):
        return self.representation
