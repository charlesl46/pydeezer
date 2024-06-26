from dataclasses import dataclass

from pydeezer.classes.model import Model


@dataclass(eq=False)
class Genre(Model):
    __generic_name__ = "genre"

    name: str = None
    picture: str = None
