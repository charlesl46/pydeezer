from dataclasses import dataclass, fields, asdict
from typing import Self, List
import asyncio

from pydeezer.request import get, get_async


@dataclass(eq=False)
class Model:
    id: int
    _json: dict = None
    _is_complete: bool = (
        True  # this boolean tells if an object contains all info available on deezer.com, for example, if it was recovered following a indirect request, there can be missing info
    )

    def __eq__(self, value: Self) -> bool:
        return self.id == value.id

    def complete(self):
        if not self._is_complete:
            comp = self.by_id(str(self.id))
            comp._is_complete = True
            return comp
        else:
            return self

    @classmethod
    def from_dict(cls, dico: dict):
        _fields = fields(cls)
        fields_names = [f.name for f in _fields]
        cleaned_dico = {
            key: value for key, value in dico.items() if key in fields_names
        }
        obj = cls(**cleaned_dico)
        obj._json = dico
        return obj

    @classmethod
    def by_id(cls, id: str | List) -> Self | List[Self]:
        if type(id) == list:
            endpoints = ["/".join([cls.__generic_name__, _id]) for _id in id]
            responses = asyncio.run(get_async(urls=endpoints))
            return [cls.from_dict(response) for response in responses]
        else:
            endpoint = "/".join([cls.__generic_name__, id])
            json = get(endpoint)
            return cls.from_dict(json)
        
    @property
    def missing_fields(self):
        return [key for key,value in asdict(self).items() if value is None]
