import pydeezer

from pprint import pprint


def test():
    g = pydeezer.Genre.by_id("0")
    print(g)


if __name__ == "__main__":
    test()
