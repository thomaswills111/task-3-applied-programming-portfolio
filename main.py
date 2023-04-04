from classes.post_office import PostOffice
from classes.mail_man import MailMan
from classes.person import Person
import threading
import time

alice = Person('Alice')
bob = Person('Bob')
charlie = MailMan('Charlie')
post_office = PostOffice()


def alices_day():
    while True:
        alices_letter = alice.write(bob, "Dear Bob...")
        alice.deliver(post_office, alices_letter)
        alice.check_letter_box()
        time.sleep(3)


def bobs_day():
    while True:
        bob.check_letter_box()
        time.sleep(3)
        bobs_letter = bob.write(alice, "Dear Alice...")
        bob.deliver(post_office, bobs_letter)



def charlies_day():
    while True:
        charlie.collect_mail(post_office)
        charlie.read(charlie.stored_letters[-1])
        charlie.deliver_mail()
        time.sleep(3)


threading.Thread(target=bobs_day).start()

threading.Thread(target=alices_day).start()

threading.Thread(target=charlies_day).start()
