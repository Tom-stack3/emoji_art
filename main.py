from drawing import Drawing


def main():
    d = Drawing()
    d.translate_image("flags_try/github.png")
    #d.add_text("We want to sleep in the Uni", "brown")
    #d.draw_amogus("brown", "black")
    print(d)


if __name__ == '__main__':
    main()
