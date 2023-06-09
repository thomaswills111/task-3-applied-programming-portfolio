from __future__ import annotations
from classes.letter import Letter


class PostOffice:
    def __init__(self, address: str = "default") -> None:
        self.address: str = address
        self.stored_letters: list["Letter"] = list()

    def __repr__(self):
        return f"Post Office located at: {self.address}"
