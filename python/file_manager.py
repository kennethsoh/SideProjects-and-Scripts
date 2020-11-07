# This script runs a simple file manager on your system. It is optimised for Unix.

import os
import sys
import shutil
from os import listdir

# Create new empty file
def createFile():
    print("You have selected to create an empty file")
    path = input("file name ")
    open(path, "w+")

# Write to a file; creates if does not exist
def writeFile():
    print("You have selected to write to a file")
    path = input("File name: ")
    text = input("What do you want to write? ")
    File = open(path, "w")
    File.write(text)
    File.close()

# Read File
def readFile():
    print("You have selected to read a file")
    path = input("file name: ")
    File = open(path, "r")
    print(File.read())
    input("\nPress Enter to Close")
    File.close()

# Delete File
def deleteFile():
    print("You have selected the delete file option")
    path = input("file name: ")
    if os.path.exists(path):
        check = input("Confirmation: Press 'Enter' to delete " + str(path))
        File = os.remove(path)
    else:
        print("The file does not exist\n")

# Copy File
def copyFile():
    print("You have selected to copy a file")
    originalPath = input("Original File to copy: ")
    targetPath = input("New Copied File name & path: ")
    shutil.copy(originalPath, targetPath)

# Move File
def moveFile():
    print("You have selected to move/rename a file")
    originalFile = input("Original File to copy: ")
    originalPath = os.path.abspath(originalFile)
    targetPath = input("New File path: ")
    os.rename(originalPath, targetPath)

# Show Directory List
def ls():
    path = os.getcwd()
    arr = os.listdir(path)
    print(arr)

# MAIN
pwdpath = os.getcwd()
print("\nWelcome to Python File Mananger\n")
i = 0
while i != 1:
    print("Your current directory is " + str(pwdpath))
    print('''\nChoose an action option: 
    0. Exit the program
    1. View list of files in current directory
    2. Create new empty file
    3. Write to file
    4. Read a file
    5. Delete a file
    6. Copy a file
    7. Move/Rename a file
    ''')
    option = int(input("Your Selection number is: "))
    if option == 1:
        ls()
    elif option == 2:
        createFile()
    elif option == 3:
        writeFile()
    elif option == 4:
        readFile()
    elif option == 5:
        deleteFile()
    elif option == 6:
        copyFile()
    elif option == 7:
        moveFile()
    else:
        i = 1
        sys.exit()
