import pydeezer

from pprint import pprint
from dataclasses import asdict


def test():
    tracks = pydeezer.Track.search("Highway to Hell")
    track = tracks[0]

    acdc = track.artist
    print(acdc)
    acdc = acdc.complete()
    print(acdc)


if __name__ == "__main__":
    test()
