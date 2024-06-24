from dataclasses import dataclass
from typing import List,Self

from urllib.parse import quote

from pydeezer.classes.model import Model
from pydeezer.ordering import ordering_type
from pydeezer.request import get

@dataclass
class Artist(Model):
    __generic_name__ = "artist"

    name : str
    link: str
    nb_fan : int
    tracklist : str
    nb_album : int
    picture : str