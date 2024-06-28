from dataclasses import dataclass

from pydeezer.classes.model import Model

@dataclass(eq=False)
class Podcast(Model):
    __generic_name__ = "podcast"
  

    title : str = None
    description : str = None
    available : bool = None
    fans : int = None
    link : str = None
    picture : str = None

