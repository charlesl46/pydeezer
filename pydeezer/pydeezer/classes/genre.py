from dataclasses import dataclass

from pydeezer.classes.model import Model

@dataclass
class Genre(Model):
    __generic_name__ = "genre"

    name : str
    picture : str