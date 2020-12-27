import os
import re



def initFileModule():
    if not os.path.exists("./Decrypted"):
        os.makedirs("Decrypted")
    if not os.path.exists("./Encrypted"):
        os.makedirs("Encrypted")
    if not os.path.exists("./Encrypt"):
        os.makedirs("Encrypt")
    if not os.path.exists("./Decrypt"):
        os.makedirs("Decrypt")

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


def listAllTextFiles(pathOfDir="./"):
    files = []
    for f in os.listdir(pathOfDir):
        if os.path.isfile(f):
            print(f)
            if (re.search(r"\.txt$", f)):
                files.append(f)
    return files


def createTextFile(filename="Decrypted.txt", location="./Decrypted/", content="This is the default Text for the File",
                   overwrite=False):
    filename = checkIfFilenameTypeIsText(filename)
    print(filename)
    if overwrite:
        if os.path.exists(location + filename):
            filenameSlice = filename.split(".")

            i = 1
            while True:
                filename = f"{filenameSlice[0]}{i}.{filenameSlice[1]}"
                if not os.path.exists(location + filename):
                    break
                i = i + 1

    file = open(location + filename, 'w')
    file.write(content)
    file.close()


def createDecryptFile(filename="ThisIsMyFile.txt", content=" ", overwrite=True):
    createTextFile(filename = filename, location = "./Decrypted/", content = content, overwrite = overwrite)


initFileModule()


createDecryptFile("DennisIstMegacool", content = "Welt wie geht es dir denn heute?")
