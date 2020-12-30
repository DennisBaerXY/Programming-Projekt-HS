"""
Dennis Bär
Programmierprojekt chiffren
Main.py
"""

# Import der Chiffren aus der anderern Datei
from chiffren import *

alphabet = list(map(chr, range(65, 91)))

print( f"Geben sie nur Zeichen enthalten im Alphabet: {''.join(alphabet)} ein. Sonderzeichen und leertasten werden einfach ignoriert und nicht verschluesselt")

myText = input("Text der vesrschluesselt werden soll: ")
shifts = int(input("Wie viele shifts?:"))

# Key is not checked,yet , if only char's
key = "StandardKey"

encryptedText = ceasarChiffre(myText, shifts)
print(f"Ceasar encrypted: {encryptedText} with {shifts} shifts")
decryptedText, guessedShifts = decryptCeasar(encryptedText)
print("Caesar Decrypted: ")
print(f"Guessed shifts: {guessedShifts}, guessed Text: {decryptedText}")

print(f"Vigenere Chiffre encrypted: {vigenereChiffre(myText, key)}")
