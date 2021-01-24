"""
Dennis Bär
Programmierprojekt chiffren
chiffren.py
"""


# Die funktion nimmt einen Text in der variable text und einen shift amount in amount. Amounts default wert ist 10
def ceasarChiffre(text, amount=10):
    # String wird in liste umgewandelt da das zuweisen an eine stelle im string bsp text[0] nicht funktioniert

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


def rangeIt(number, amount, bottom=65, top=90):
    number += amount
    rangeOfSet = abs(top - bottom) + 1
    while number > top:
        number = number - rangeOfSet
    while number < bottom:
        number = number + rangeOfSet

    c = chr(number)
    return c


# Einzelner Buchstabe ( c ) wird um amount geändert.
# Bsp c = 'a' und amount = 4        -> b -> c -> d -> e
# dann ist return 'e'
def shiftChar(c, amount=10):
    number = ord(c)
    # GroßBuchstaben
    if (number >= 65 and number <= 90):
        return rangeIt(number, amount, 65, 90)
    # KleinBuchstaben
    elif (number >= 97 and number <= 122):
        return rangeIt(number, amount, 97, 122)

    # Returned zeichen wenn es kein Groß buchstabe ist
    return c


def generateMultiCaesarField(bottom=65, top=91):
    charSets = list(map(chr, range(bottom, top)))
    caesarField = []

    length = abs(top - bottom)
    # Generierung des um eine Zeile immer geschifftete Feld
    for i in range(length):
        row = []
        for j in range(length):
            row.append(ceasarChiffre(charSets[j], i))
        caesarField.append(row)
    return caesarField


def makeKeyCorrectLength(text, key):
    # Ursprungs key um das es erweitert werden kann
    keydata = key

    # Solange der text noch länger als der Key ist wird an key, key hinzugefügt ..bsp key: Abc Text: Dennis,  Key danach -> AbcAbc
    while len(text) > len(key):
        key = key + keydata
    return key


def IndexViginere(key, i):
    if key[i].isupper():
        indexKey = ord(key[i]) - 65
    elif key[i].islower():
        indexKey = ord(key[i]) - 97
    else:
        indexKey = None
    return indexKey




def vigenereChiffre(text="Default", key="Default"):
    # Generierung des um eine Zeile immer geschifftete Feld
    upperChiffre = generateMultiCaesarField(65, 91)
    lowerChiff = generateMultiCaesarField(97, 123)

    key = makeKeyCorrectLength(text, key)

    encryptList = []

    # Encryotion Process mit der vigenere "Tabelle"
    for i in range(len(text)):
        # -65 um die Großbuchstaben in indexe umzuwanden bps A = 65  ->  A - 65 = 0
        # ord um die Ascii werte zu bekommen in Decimal
        indexKey = IndexViginere(key, i)
        indexText = IndexViginere(text,i)

        if text[i].isupper():
            encryptList.append(upperChiffre[indexText][indexKey])
        elif text[i].islower():
            encryptList.append(lowerChiff[indexText][indexKey])
        else:
            encryptList.append(text[i])


    # Zusammen fügen der Liste als Text
    encryptText = "".join(encryptList)
    return encryptText


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
        # Zählt die sonderzeichen nicht mit sondern nur die buchstaben die eingegeben Wurden
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
    shifts = 26 - result % 26

    # Returned wird der Original text der druch das chiffrieren in die andere richtung generiert wird und wie viele shifts es gewesen sind
    return ceasarChiffre(text, shifts * -1), shifts
