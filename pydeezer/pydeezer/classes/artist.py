from dataclasses import dataclass
from typing import List, Self

from urllib.parse import quote

from pydeezer.classes.model import Model
from pydeezer.ordering import ordering_type
from pydeezer.request import get


@dataclass
class Artist(Model):
    __generic_name__ = "artist"

    name: str = None
    link: str = None
    nb_fan: int = None
    tracklist: str = None
    nb_album: int = None
    picture: str = None
