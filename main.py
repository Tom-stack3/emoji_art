from drawing import Drawing


def main():
    d = Drawing()
    d.translate_image("flags_try/guinea.png", True)
    # d.add_text("Hi", "brown")
    #d.draw_amogus("pink")
    print(d)


if __name__ == '__main__':
    main()
