#!/usr/bin/env python3
from drawing import Drawing


def main():
    d = Drawing()
    d.translate_image("./examples/tanzania.png", True)
    d.add_text("Hi there", "green")
    d.draw_amogus("pink", "green")
    print(d)


if __name__ == '__main__':
    main()
