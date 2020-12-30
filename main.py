"""
Dennis Bär
Programmierprojekt chiffren
"""

#Import der Chiffren aus der anderern Datei
from chiffren import *

alphabet = list(map(chr, range(65, 91)))

print(f"Geben sie nur Zeichen enthalten im Alphabet: {''.join(alphabet)} ein. Sonderzeichen und leertasten werden einfach ignoriert und nicht verschluesselt")

myText = input("Text der vesrschluesselt werden soll: ")
shifts = int(input("How many shifts?:"))

encryptedText = ceasarChiffre(myText, shifts)
print(f"Ceasar encrypted: {encryptedText} with {shifts} shifts")

decryptedText, guessedShifts = decryptCeasar(encryptedText)
print(f"Guessed shifts: {guessedShifts}, guessed Text: {decryptedText}")


