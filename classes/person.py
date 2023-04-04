from __future__ import annotations
from classes.letter_box import LetterBox
from classes.letter import Letter
from classes.post_office import PostOffice


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.letter_box: LetterBox = LetterBox(self)

    def __repr__(self):
        return f"{self.name}"

    def write(self, recipient: Person, contents) -> Letter:
        new_letter = Letter(recipient, contents)
        return new_letter

    def read(self, letter: Letter) -> None:
        print(letter.reader_validation(self.name))
        letter.change_read_status()

    def check_letter_box(self):
        if self.letter_box.letter_flag_raised == True:
            self.read(self.letter_box.stored_letters[-1])

    def deliver(self, post_office: PostOffice, letter: Letter):
        post_office.stored_letters.append(letter)
