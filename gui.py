import tkinter as tk
from tkinter import filedialog

from chiffren import *
from utils import *


def openFile(text_box):
    print(text_box)
    # Returns a file that is open
    file = filedialog.askopenfile(initialdir = "./", mode = "r", filetypes = [("Text Files", '*.txt')])

    if file is not None:
        chars = file.read()
        print(chars)
        text_box.delete("1.0", "end")
        text_box.insert("1.0", chars)


def saveToFile(box):
    content = box.get("1.0", "end")
    if content != None:
        extensions = [('Text Document', '*.txt'), ('All Files', '*.*')]
        file = filedialog.asksaveasfile(mode = "w", filetypes = extensions, defaultextension = extensions)
        if file is None:
            return
        file.write(content)
        file.close()


def encryptInputText(InputBox, OutputBox):
    content = InputBox.get("1.0", "end")
    choice = v.get()
    choice = int(choice)

    key_content = keyEntry.get()
    shift_content = shiftsEntry.get()

    key_content.strip()
    key_content.replace(" ", "")

    shift_content.strip()
    shift_content.replace(" ", "")

    if not key_content.isalpha():
        key_content = random_chiffren_key_generator(12)
    if not shift_content.isnumeric():
        shift_content = random_shifts()

    shift_content = int(shift_content)

    chiffre_text = ""
    if choice == 0:
        chiffre_text = ceasarChiffre(content, shift_content)

    if choice == 1:

        chiffre_text = vigenereChiffre(content, key_content)

    OutputBox.delete("1.0", "end")
    OutputBox.insert("1.0", chiffre_text)


window = tk.Tk()

window.title("Chiffren by Baer")

frame = tk.Frame(window)
mainmenu = tk.Menu(frame)
mainmenu.add_command(label = "Exit", command = window.quit)
mainmenu.add_command(label = "Options", )
mainmenu.add_command(label = "Save")
mainmenu.add_command(label = "Load")

window.config(menu = mainmenu)

# Header
Header = tk.Label(text = "Chiffren by Baer", height = 3, font = 10, foreground = 'black')
Header.grid(row = 0, column = 2)

# Left Site

LabelEntry = tk.Label(text = "Input Text", width = 25, height = 1, font = 6)
LabelEntry.grid(column = 0, row = 1)

LeftBox = tk.Text(height = 3, width = 20)
LeftBox.grid(column = 0, row = 2)

Button = tk.Button(text = "Load from file ", command = lambda: openFile(LeftBox))
Button.grid(column = 0, row = 3)

optionsFrame = tk.Frame(window)
optionsFrame.grid(row = 4)

LabelOptions = tk.Label(optionsFrame, text = "Options", font = 10, height = 2)
LabelOptions.pack()

shiftsLabel = tk.Label(optionsFrame, text = "Shifts:", font = 4)
shiftsLabel.pack()

shiftsEntry = tk.Entry(optionsFrame, text = "12")
shiftsEntry.pack()

keyLabel = tk.Label(optionsFrame, text = "Key:", font = 4)
keyLabel.pack()

keyEntry = tk.Entry(optionsFrame, text = "EncryptionKey")
keyEntry.pack()

# Midlle


# Encrypt Button
EnryptCeasarButton = tk.Button(text = "Encrypt!", width = 15, font = 8, foreground = "white", bg = "red",
                               command = lambda: encryptInputText(LeftBox, RightBox))
EnryptCeasarButton.grid(column = 2, row = 2)


def decryptInputText(LeftBox, RightBox):
    content = LeftBox.get("1.0", "end")
    choice = v.get()
    choice = int(choice)

    chiffre_text = ""
    if choice == 0:
        chiffre_text, shifts = decryptCeasar(content)

    # if choice == 1:

    # Decrypt Viegenere Chiffre return

    RightBox.delete("1.0", "end")
    RightBox.insert("1.0", chiffre_text)


DecrypTionButton = tk.Button(text = "Decrypt!!", width = 15, font = 8, foreground = "white", bg = "green",
                             command = lambda: decryptInputText(LeftBox, RightBox))
DecrypTionButton.grid(column = 2, row = 3)

# Choose encryption


newFrame = tk.Frame(window)
newFrame.grid(column = 2, row = 4)

v = tk.StringVar(newFrame, 0)

r1 = tk.Radiobutton(newFrame, text = "Caesar-Chiffre", value = 0, variable = v, font = 7)
r1.pack()

r2 = tk.Radiobutton(newFrame, text = "Vigenere-Chiffre", value = 1, variable = v, font = 7)
r2.pack()

# Right side

LabelEntry = tk.Label(text = "Output", width = 25, height = 1, font = 6)
LabelEntry.grid(column = 4, row = 1)

RightBox = tk.Text(height = 3, width = 20)
RightBox.grid(column = 4, row = 2)

Button = tk.Button(text = "Save to file ", command = lambda: saveToFile(RightBox))
Button.grid(column = 4, row = 3)
window.mainloop()
