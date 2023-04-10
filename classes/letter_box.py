from __future__ import annotations
from classes.letter import Letter


class LetterBox:
    def __init__(self, owner: "Person") -> None:
        self.owner: "Person" = owner
        self.stored_letters: list["Letter"] = list()
        self.letter_flag_raised: bool = False

    def __repr__(self) -> str:
        return f"{self.owner}'s letterbox"


