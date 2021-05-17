str_colors = {"red": "❤️", "orange": "🧡", "yellow": "💛", "green": "💚", "blue": "💙", "purple": "💜",
              "black": "🖤", "white": "🤍"}


class Heart:
    def __init__(self, color):
        self.str = str_colors[color]

    def __repr__(self):
        return self.str

    @staticmethod
    def get_working_colors():
        return str_colors.keys()
