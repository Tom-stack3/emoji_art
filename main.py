from drawing import Drawing


def main():
    d = Drawing()
    d.translate_image("flags_try/letters.png")
    #d.add_text("SsUu", "brown")
    print(d)


if __name__ == '__main__':
    main()
