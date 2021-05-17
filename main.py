from drawing import Drawing
from heart import Heart


def main():
    d = Drawing()
    print(d)
    d.translate_image("flags_try/lgbtq.png")
    print(d)


if __name__ == '__main__':
    main()
