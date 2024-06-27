from dataclasses import dataclass
from typing import List, Self
from datetime import datetime
from pprint import pprint

from urllib.parse import quote

from pydeezer.classes.model import Model
from pydeezer.ordering import ordering_type
from pydeezer.request import get
from pydeezer.utils import read_datetime
from pydeezer.classes.artist import Artist


@dataclass
class Track(Model):
    __generic_name__ = "track"

    title: str = None
    artist: Artist = None
    link: str = None
    title_short: str = None
    duration: int = None
    rank: int = None
    explicit_lyrics: bool = None
    preview: str = None
    track_position: int = None
    release_date: datetime = None
    available_countries: list = None
    isrc: str = None
    bpm: float = None
    gain: float = None
    contributors: list = None

    def __post_init__(self):
        self.release_date = (
            read_datetime(self.release_date) if self.release_date is not None else None
        )
        self.artist = Artist.from_dict(self.artist)
        self.artist._is_complete = False

    @classmethod
    def search(cls, query: str, ordering: ordering_type = None) -> List[Self]:
        endpoint = (
            f"search?q={quote(query)}{f'&order={ordering.lower()}' if ordering else ''}"
        )
        json = get(endpoint)
        # pprint(json)
        tracks = [Track.from_dict(d) for d in json.get("data")]
        return tracks
