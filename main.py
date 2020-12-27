"""
Dennis Bär
Programmierprojekt chiffren
"""


# Die funktion nimmt einen Text in der variable text und einen shift amount in amount. Amounts default wert ist 10
def ceasarChiffre(text, amount=10):
    # String wird in liste umgewandelt da das zuweisen an eine stelle im string bsp text[0] nicht funktioniert
    text = text.upper()
    charArray = list(text)

    # Jeder buchstabe wird geshifted
    for i in range(len(text)):
        if (charArray[i] != ' '):
            charArray[i] = shiftChar(charArray[i], amount)

    # Fügt die lsite wieder zusammen in ein String. Hier werden einfach ein leerer String und die liste kombiniert um so
    # einen string wieder aus der Liste zu bekommen

    text = "".join(charArray)

    # Versschlüsselter Text wir wieder returned
    return text


# Einzelner Buchstabe ( c ) wird um amount geändert.
# Bsp c = 'a' und amount = 4        -> b -> c -> d -> e
# dann ist return 'e'
def shiftChar(c, amount=10, asciiLast=90):
    number = ord(c)
    if (number >= 65 and number <= 90):
        number += amount

        while number > asciiLast:
            number = number - 26
        while number < 65:
            number = number + 26

        c = chr(number)

        return c

    return c


def vigenereChiffre(text="Default", key="Default"):
    multiCeasarChiffre = []

    alphabet = list(map(chr, range(65, 91)))

    for i in range(len(text)):
        row = []
        for j in range(26):
            row.append(ceasarChiffre(alphabet[j], i))
        multiCeasarChiffre.append(row)
        print("".join(row))

    text = text.upper()
    key = key.upper()
    keydata = key

    while len(text) > len(key):
        key = key + keydata

    keyList = list(key)
    textList = list(text)
    encryptList = []

    # Encryotion Process mit der vigenere "Tabelle"
    for i in range(len(text)):
        # -65 um die Großbuchstaben in indexe umzuwanden bps A = 65  ->  A - 65 = 0
        # ord um die Ascii werte zu bekommen in Decimal
        indexText = ord(textList[i]) - 65
        indexKey = ord(keyList[i]) - 65

        encryptList.append(multiCeasarChiffre[indexText][indexKey])

    # Zusammen fügen der Liste als Text
    encryptText = "".join(encryptList)
    print("ViginerChifre: ", encryptText)


# vigenereChiffre("Wassr","IchBinDennisBaer")


# Funktion um die häufigkeit der einzelnen Buchstaben zu finden
def countChars(text):
    text = text.upper()
    counting = []
    total = 0

    for i in range(26):
        counting.append(0)
    # Ignoriert leertasten und addiert die zahl an der Index stelle des Buchstabens
    for z in text:
        #Zählt die sonderzeichen nicht mit sondern nur die buchstaben die eingegeben Wurden
        if (ord(z) >= 65 and ord(z) <= 90):
            index = ord(z) - 65
            counting[index] += 1
            total += 1

    # Returned eine Liste mit der häufigkeit der jeweiligen Buchstaben und die komplette anzahl der Buchstaben
    return counting, total


def decryptCeasar(text):
    # Häufigkeit der einzelnen buchstaben in reihenfolge a,b,c .....
    weightOfChar = [6.51, 1.89, 3.06, 5.08, 17.40, 1.66, 3.01, 4.76, 7.55, 0.27, 1.21, 3.44, 2.53, 9.78, 2.51, 0.79,
                    0.02, 7.0, 7.27, 6.15, 4.35, 0.67, 1.89, 0.03, 0.04, 1.13]

    # Wird am ende die Maximale punktzahl des besten Satzes haben
    maxPoints = 0
    # Wird am ende die shifts haben um den text zurück zu entschlüsseln
    result = 0

    for i in range(26):
        # Shiftet den text immer neu also beim ersten mal mit 0 garnicht und danach immer weiter um jede shifts zu bekommen
        msg = ceasarChiffre(text, i)

        # in count steht die jeweilige anzahl der Buchstaben des Satzes drin
        count, total = countChars(msg)

        points = 0.0

        # Berechnet die Punkte für jeden satz mit der anzahl der jeweiligen Buchstaben und der wichtung der Buchstagebn
        for p in range(26):
            points += count[p] * weightOfChar[p]

        # Falls der Satz mehr wert wie der Maximale ist wird result auf diesen shift gesezt und die maxpoints auf die aktuellen
        if (points > maxPoints):
            result = i
            maxPoints = points

    # Ergebnis gibt die shifts die man zurück gehen müsste um den Original text zu bekommen.
    result = 26 - result % 26

    # Returned wird der Original text der druch das chiffrieren in die andere richtung generiert wird und wie viele shifts es gewesen sind
    return ceasarChiffre(text, result * -1), result


alphabet = list(map(chr, range(65, 91)))

print(f"Geben sie nur Zeichen enthalten im Alphabet: {''.join(alphabet)} ein. Sonderzeichen und leertasten werden einfach ignoriert und nicht verschluesselt")

myText = input("Text der vesrschluesselt werden soll: ")
shifts = int(input("How many shifts?:"))

encryptedText = ceasarChiffre(myText, shifts)
print(f"Ceasar encrypted: {encryptedText} with {shifts} shifts")

decryptedText, guessedShifts = decryptCeasar(encryptedText)
print(f"Guessed shifts: {guessedShifts}, guessed Text: {decryptedText}")


