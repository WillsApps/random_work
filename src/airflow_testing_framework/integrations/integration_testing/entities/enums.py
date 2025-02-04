from enum import Enum, auto

try:
    from enum import StrEnum
except ImportError:
    from integrations.entities.classes import StrEnum


class TestId(Enum):
    PLATFORM_DELETES_REFINEMENTS = "platform_deletes"


class DataEnvironment(StrEnum):
    DBX = auto()
    RDS = auto()
    S3 = auto()
