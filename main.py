from drawing import Drawing
from heart import Heart


def main():
    d = Drawing()
    d.add_row([Heart("red"), Heart("red"), Heart("red"), Heart("red")])
    d.add_row([Heart("blue"), Heart("blue"), Heart("green"), Heart("green")])
    print(d)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
