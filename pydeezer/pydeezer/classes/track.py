from dataclasses import dataclass
from typing import List,Self
from datetime import datetime

from urllib.parse import quote

from pydeezer.classes.model import Model
from pydeezer.ordering import ordering_type
from pydeezer.request import get
from pydeezer.utils import read_datetime

@dataclass
class Track(Model):
    __generic_name__ = "track"

    title: str
    link: str
    title_short : str
    duration : int
    track_position : int
    rank : int
    explicit_lyrics : bool
    release_date : datetime
    available_countries : list
    preview : str
    isrc : str
    bpm : float
    gain : float 
    contributors : list

    def __post_init__(self):
        self.release_date = read_datetime(self.release_date)

    @classmethod
    def search(cls,query: str, ordering : ordering_type = None) -> List[Self]:
        endpoint = f"search?q={quote(query)}{f'&order={ordering.lower()}' if ordering else ''}"
        json = get(endpoint)
        tracks = []
        for track in json.get("data"):
            tracks.append(Track.from_dict(track))

        return tracks