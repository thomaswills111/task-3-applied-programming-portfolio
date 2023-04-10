from __future__ import annotations
from classes.person import Person
from classes.post_office import PostOffice


class MailMan(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.stored_letters: list["Letter"] = list()

    def __repr__(self) -> str:
        return f"{self.name}: Mail Man"

    def collect_mail(self, post_office: PostOffice) -> None:
        for letter in post_office.stored_letters:
            self.stored_letters.append(letter)
            post_office.stored_letters.remove(letter)

    def deliver_to_lb(self) -> None:
        for letter in self.stored_letters:
            letter.recipient.letter_box.stored_letters.append(letter)
            letter.recipient.letter_box.letter_flag_raised = True


if __name__ == '__main__':
    alice = Person('Alice')
    bob = Person('Bob')
    charlie = MailMan("Charlie")
    post_office = PostOffice()

    alices_letter = alice.write(bob, "Dear Bob...")
    charlie.collect_mail(post_office)
    charlie.deliver_mail()

    print(alices_letter)
    print(bob)

    charlie.read(alices_letter)
    bob.read(alices_letter)
