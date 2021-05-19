import numpy as np
from scipy.spatial import KDTree


class Heart:
    def __init__(self, color):
        self.str_colors = {"red": "❤️", "orange": "🧡", "yellow": "💛", "green": "💚", "blue": "💙", "purple": "💜",
                           "black": "🖤", "white": "🤍", "brown": "🤎", "pink": "💗"}
        self.main_colors = [(249, 91, 90),
                            (255, 161, 46),
                            (255, 217, 51),
                            (64, 203, 3),
                            (41, 163, 229),
                            (157, 108, 229),
                            (25, 25, 25),
                            (240, 240, 240),
                            (167, 98, 76),
                            (255, 122, 168)
                            ]
        self.str = self.__translate_rgb_to_color(color)

    def __repr__(self):
        return self.str

    def get_working_colors(self):
        return self.str_colors.keys()

    @staticmethod
    def __eu_dist(p1, p2):
        return np.linalg.norm(p1 - p2)

    def __find_nearest_color(self, rgb):
        closest_color = self.main_colors[0]
        min_dist = self.__eu_dist(self.main_colors[0], rgb)
        for main_color in self.main_colors[1:]:
            dist = self.__eu_dist(main_color, rgb)
            if dist < min_dist:
                min_dist = dist
                closest_color = main_color
        return closest_color

    def __translate_rgb_to_color(self, rgb):
        if isinstance(rgb, str):
            return self.str_colors[rgb]

        color_dict = dict(zip(self.main_colors, list(self.str_colors.keys())))
        # {self.main_colors[i]: self.str_colors.keys()[i] for i in range(len(self.main_colors))}

        closest_color = self.__find_nearest_color(rgb)
        current_color = color_dict[closest_color]
        return self.str_colors[current_color]
