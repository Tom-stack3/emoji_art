from drawing import Drawing


def main():
    d = Drawing()
    print(d)
    d.translate_image("flags_try/2.png")
    print(d)


if __name__ == '__main__':
    main()
