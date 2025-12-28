import abc

from beartype.typing import Mapping
from dataclasses_json import DataClassJsonMixin


class ScriptableDataClass(DataClassJsonMixin, Mapping, abc.ABC):
    def __len__(self):
        return len(self.to_dict())

    def __iter__(self):
        return iter(self.to_dict())

    def __getitem__(self, key, default=None):
        return self.to_dict().get(key, default)
