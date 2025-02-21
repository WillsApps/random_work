from enum import Enum


class StrEnum(Enum):
    @classmethod
    def from_str(cls, name: str):
        try:
            return cls[name.upper()]
        except KeyError:
            return cls[name.replace(f"{cls.__name__}.", "").upper()]
