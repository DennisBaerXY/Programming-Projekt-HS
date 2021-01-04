from random import randint


def random_chiffren_key_generator(keyLength):
    key = ""
    for i in range(keyLength):
        random = randint(65, 90)
        zeichen = chr(random)
        key = key + zeichen
    return key


def random_shifts():
    return randint(1, 25)
