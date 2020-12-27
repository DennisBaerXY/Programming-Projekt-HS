import re
import os

if (os.path.exists("./decrypted") != True):
    os.makedirs("decrypted")


def checkIfFilenameTypeIsText(filename):
    fileSplit = filename.split(".")
    if (len(fileSplit) > 2):
        print("Wrong File name format. Using default file name \" I_didnt_name_my_file_right\" ")
        filename = "I_didnt_name_my_file_right.txt"
    if (len(fileSplit) == 1):
        filename = fileSplit[0] + ".txt"

    if (len(fileSplit) == 2):
        if (fileSplit[1] != "txt"):
            filename = filename = fileSplit[0] + ".txt"

    return filename


def listAllTextFiles():
    files = []
    for f in os.listdir():
        if os.path.isfile(f):
            print(f)
            if (re.search(r"\.txt$", f)):
                files.append(f)
    return files


def createDecryptedFile(filename="Decrypted.txt", content="This is the default Text for the File",overwrite = False):
    filename = checkIfFilenameTypeIsText(filename)
    print(filename)
    if overwrite:
        if (os.path.exists(f"./decrypted/{filename}")):
            filenameSlice = filename.split(".")

            i = 1
            while True:
                filename = f"{filenameSlice[0]}{i}.{filenameSlice[1]}"
                if not os.path.exists(f"./decrypted/{filename}"):
                    break
                i = i+1

    file = open(f'./decrypted/{filename}','w')
    file.write(content)
    file.close()


createDecryptedFile("DennisIstMegacool",content="Welt wie geht es dir denn heute?")
