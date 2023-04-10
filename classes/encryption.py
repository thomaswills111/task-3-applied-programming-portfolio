from __future__ import annotations
import random


class Encryption:
    def __init__(self, text) -> None:
        self._shift_key: int = random.randint(1, 20)
        self._encrypted_text: str = self.encrypt(text, self._shift_key)

    def __repr__(self) -> str:
        return f"Encrypted text: {self._encrypted_text}"

    def encrypt(self, text: str, shift_key: int) -> str:
        encrypted_text = ""
        s = shift_key
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encrypted_text += chr((ord(char) + s - 65) % 26 + 65)

                else:
                    encrypted_text += chr((ord(char) + s - 97) % 26 + 97)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self) -> str:
        encrypted_text = self._encrypted_text
        s = self._shift_key
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                if char.isupper():
                    decrypted_text += chr((ord(char) - s - 65) % 26 + 65)
                else:
                    decrypted_text += chr((ord(char) - s - 97) % 26 + 97)
            else:
                decrypted_text += char
        return decrypted_text


if __name__ == '__main__':
    test = Encryption("Hello World!")

    print(test.encrypted_text)

    print(test.decrypt())
