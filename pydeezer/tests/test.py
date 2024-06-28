import pydeezer

from pprint import pprint
from dataclasses import asdict
from unittest import TestCase

import pydeezer.utils

ALBUM = pydeezer.Album.by_id("226069")
ARTIST = pydeezer.Artist.by_id("176")

class Tests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.album_title = "Dire Straits"
        self.first_song_title = "Down To The Waterline"
        self.release_date = pydeezer.utils.read_datetime("1983-02-15")

    def test_album(self):
        self.assertEqual(ALBUM.title,"Dire Straits")
        self.assertEqual(ALBUM.release_date,self.release_date)
        self.assertEqual(ALBUM.artist,ARTIST)
        
