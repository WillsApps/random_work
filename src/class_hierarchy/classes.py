from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def print_me(self, index: int):
        raise NotImplementedError()


class ChildOne(Base):
    def print_me(self, index: int):
        print(f"Child One, {index}")


class ChildTwo(Base):
    def print_me(self, index: int):
        print(f"Child Two, {index}")


CLASS_MAP = {"one": ChildOne(), "two": ChildTwo()}
# print_all(["one", "two", "two", "two","one"], Base.print_me)
