from dataclasses import dataclass

from pydeezer.classes.model import Model


@dataclass
class Album(Model):
    __generic_name__ = "album"

    title: str
    link: str
    cover: str
    

