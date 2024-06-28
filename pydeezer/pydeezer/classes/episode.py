from dataclasses import dataclass
from datetime import datetime

from pydeezer.classes.model import Model
from pydeezer.classes.podcast import Podcast
from pydeezer.utils import read_datetime

@dataclass(eq=False)
class Episode(Model):
    __generic_name__ = "episode"
  

    title : str = None
    description : str = None
    available : bool = None
    release_date : datetime = None
    duration : int = None
    link : str = None
    picture : str = None
    podcast : Podcast = None

    def __post_init__(self):
        self.release_date = (
            read_datetime(self.release_date) if self.release_date is not None else None
        )
        self.podcast = Podcast.from_dict(self.podcast)
        self.podcast._is_complete = False



