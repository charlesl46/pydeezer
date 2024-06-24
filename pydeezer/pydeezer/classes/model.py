from dataclasses import dataclass, fields
from typing import Self

from pydeezer.request import get


@dataclass
class Model:
    id: str

    @classmethod
    def from_dict(cls, dico: dict):
        _fields = fields(cls)
        fields_names = [f.name for f in _fields]
        cleaned_dico = {
            key: value for key, value in dico.items() if key in fields_names
        }
        return cls(**cleaned_dico)

    @classmethod
    def by_id(cls, id: str) -> Self:
        endpoint = "/".join([cls.__generic_name__, id])
        json = get(endpoint)
        return cls.from_dict(json)
