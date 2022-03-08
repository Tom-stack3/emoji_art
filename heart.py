import numpy as np

class Heart:
    def __init__(self, color):
        self.str_colors = {"red": "❤️", "orange": "🧡", "yellow": "💛", "green": "💚", "blue": "💙", "purple": "💜",
                           "black": "🖤", "white": "🤍", "brown": "🤎", "pink": "💗"}

        # in RGB format
        self.main_colors = {
            (249, 91, 90): "red",
            (187, 0, 19): "red",
            (255, 161, 46): "orange",
            (255, 217, 51): "yellow",
            (64, 203, 3): "green",
            (0, 123, 58): "green",
            (41, 163, 229): "blue",
            (0, 30, 150): "blue",
            (157, 108, 229): "purple",
            (118, 1, 136): "purple",
            (25, 25, 25): "black",
            (240, 240, 240): "white",
            (167, 98, 76): "brown",
            (255, 122, 168): "pink"
        }
        self.str = self.__translate_rgb_to_color(color)

    def __repr__(self):
        return self.str

    def get_working_colors(self):
        return self.str_colors.keys()

    @staticmethod
    def __eu_dist(p1, p2):
        return np.linalg.norm(p1 - p2)

    def __find_nearest_color(self, rgb):
        closest_color = list(self.main_colors.keys())[0]
        min_dist = self.__eu_dist(closest_color, rgb)
        for main_color in list(self.main_colors.keys())[1:]:
            dist = self.__eu_dist(main_color, rgb)
            if dist < min_dist:
                min_dist = dist
                closest_color = main_color
        return closest_color

    def __translate_rgb_to_color(self, rgb):
        if isinstance(rgb, str):
            return self.str_colors[rgb]

        closest_color = self.__find_nearest_color(rgb)
        current_color = self.main_colors[closest_color]
        return self.str_colors[current_color]
