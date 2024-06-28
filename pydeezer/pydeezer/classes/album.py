from dataclasses import dataclass
from typing import List
from datetime import datetime

from pydeezer.classes.model import Model
from pydeezer.classes.artist import Artist
from pydeezer.classes.track import Track
from pydeezer.classes.genre import Genre
from pydeezer.utils import read_datetime,explicitness_from_index

@dataclass(eq=False)
class Album(Model):
    __generic_name__ = "album"

    title: str = None
    upc : str = None
    link: str = None
    cover: str = None
    genres : List[Genre] = None
    nb_tracks : int = None
    duration : int = None
    fans : int = None
    release_date : datetime = None
    record_type : str = None
    available : bool = None
    tracklist : str = None
    explicit_lyrics : bool = None
    explicit_content_lyrics : int = None
    explicit_content_cover : int = None
    contributors : List = None
    artist : Artist = None
    tracks : List[Track] = None

    @property
    def mean_duration(self):
        return self.duration / self.nb_tracks

    @property
    def explicit(self):
        return {"lyrics" : explicitness_from_index(self.explicit_content_lyrics),"cover" : explicitness_from_index(self.explicit_content_cover)}

    def __post_init__(self):
        self.release_date = (
            read_datetime(self.release_date) if self.release_date is not None else None
        )
        self.artist = Artist.from_dict(self.artist)
        self.artist._is_complete = False

        tracks = []
        for json_obj in self.tracks.get("data"):
            obj = Track.from_dict(json_obj)
            obj._is_complete = False
            tracks.append(obj)
        self.tracks = tracks


        contributors = []
        for json_obj in self.contributors:
            obj = Artist.from_dict(json_obj)
            obj._is_complete = False
            contributors.append(obj)
        self.contributors = contributors


        self.genres = [Genre.from_dict(genre_obj) for genre_obj in self.genres.get("data")]


