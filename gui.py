import tkinter as tk
from tkinter import filedialog


def openFile(TextBox):
    print(TextBox)
    file = filedialog.askopenfile(initialdir = "./", mode = "r", filetypes = [("Text Files", '*.txt')])

    if file is not None:
        chars = file.read()
        print(chars)
        TextBox.delete("1.0", "end")
        TextBox.insert("1.0", chars)


window = tk.Tk()

window.title("Chiffren by Baer")


# Header
Header = tk.Label(text = "Chiffren by Baer", height = 3, font = 10, foreground = 'black')
Header.grid(row = 0, column = 2)

# Left Site

LabelEntry = tk.Label(text = "Input Text", width = 25, height = 1,font=6)
LabelEntry.grid(column = 0, row = 1)

LeftBox = tk.Text(height = 3, width = 20)
LeftBox.grid(column = 0, row = 2)

Button = tk.Button(text = "Load from file ", command = lambda: openFile(LeftBox))
Button.grid(column = 0, row = 3)




#Midlle

EnryptCeasarButton = tk.Button(text="Encrypt!",width = 15,font = 8,foreground="red",bg="black")
EnryptCeasarButton.grid(column = 2,row = 2)

# Right side

LabelEntry = tk.Label(text = "Output", width = 25, height = 1,font=6)
LabelEntry.grid(column = 4, row = 1)

RightBox = tk.Text(height = 3, width = 20)
RightBox.grid(column = 4, row = 2)

Button = tk.Button(text = "Load from file ", command =  lambda: openFile(RightBox))
Button.grid(column = 4, row = 3)
window.mainloop()
