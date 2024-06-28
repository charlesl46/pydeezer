from dataclasses import dataclass
from typing import List

from pydeezer.classes.model import Model
from pydeezer.classes.track import Track
from pydeezer.request import get

@dataclass(eq=False)
class Radio(Model):
    __generic_name__ = "radio"

    title : str = None
    description : str = None
    picture : str = None 
    tracklist : str = None

    def get_tracks(self) -> List[Track] | None:
        if self.tracklist is not None:
            tracks = []
            json = get(self.tracklist)
            for track_json in json.get("data"):
                track = Track.from_dict(track_json)
                track._is_complete = False
                tracks.append(track)
            return tracks
        else:
            return None
