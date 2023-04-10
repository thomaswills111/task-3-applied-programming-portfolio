from __future__ import annotations
from classes.encryption import Encryption


class Letter:
    def __init__(self, writer: "Person", recipient: "Person", message: str) -> None:
        self.writer: "Person" = writer
        self.recipient: "Person" = recipient
        self.message: str = message
        self._has_been_read: bool = False
        self.encrypted_message = Encryption(self.message)

    def __repr__(self) -> str:
        return repr(f"{self.recipient}'s letter")

    def see_read_status(self) -> bool:
        return self._has_been_read

    def change_read_status(self) -> None:
        self._has_been_read = True

    def reader_validation(self, reader_name: str) -> str:
        if reader_name == self.recipient.name:
            return self.encrypted_message.decrypt()
        return self.encrypted_message._encrypted_text
