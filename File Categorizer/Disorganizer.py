"""
    name='Disorganizer.py',
    project='File Sorter'
    date='12/22/2019',
    author='Oshodi Kolapo',
"""
import os
import glob
import shutil
import sys
import time

print("\nHello there! ")
print("Enter the full path/directory/folder without '' or "" ")
example = 'C:\ Users\Leo\Documents'.replace(" ", "")
print("Example - C:/Users/Leo/Documents or " + example)
user_address = str(input(">> "))  # get directory path from user
if not os.path.exists(user_address):
    print("Path or directory doesn't seem to exist \nSorry! try again later")
    sys.exit()
else:
    pass

print("Working on " + user_address)
time.sleep(1.0)


def start_app(address: str):
    os.chdir(address)  # Change working directory to the provided directory
    count = 0
    folders = [folder for folder in glob.iglob('**', recursive=True) if
               not os.path.isfile(folder)]  # get names of all folders in the directory and subdirectories

    #  get all files recursively in directories and subdirectories
    for file in glob.iglob('**', recursive=True):
        if os.path.isfile(file):  # check if its a file and not a folder
            count += 1
            try:
                shutil.move(file, address)  # move file to provided directory
                print(f"{file} moved to {address}")
            except Exception:
                pass

    for fol in folders:
        print(f"{fol} deleted")
        os.rmdir(fol)  # delete all empty folders

    print("\n---------------------END------------------------------")
    print("Success")
    print(f"Total files extracted: {count}")
    print(f"Total directory found: {len(folders)}")
    print(f"Folders: {folders} deleted")


start_app(user_address)  # method call
