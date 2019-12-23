"""
    name='Sort-by-Extension',
    project='File Sorter'
    date='12/22/2019',
    author='Oshodi Kolapo'
"""

import shutil
import os
import sys
from pathlib import Path
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
    # method to get extension from a file
    def extension_catcher(name: str):
        return name.split('.')[-1]  # get string that succeeds the last '.'

    os.chdir(address)  # Change working directory to the provided directory
    path = Path(address)  # make directory a Path object
    files = path.iterdir()  # iterate through all the files in the path
    files_extension = set()  # a set to filter and get unique extensions
    count = 0

    for filename in files:
        filename = str(filename)
        if Path(filename).is_file():  # check if its a file and not a folder
            count += 1
            files_extension.add(extension_catcher(filename))  # add extensions to the set
            for extension in files_extension:
                try:
                    os.mkdir(extension.upper() + "-files")  # create a folder for each extensions
                    print(f"'{extension.upper()}' folder created")
                except FileExistsError:
                    pass

                if filename.endswith(extension):  # checks for files ending with extension
                    try:
                        shutil.move(filename,
                                    extension.upper() + '-files')  # move files to folders wrt their extensions
                        print(f"'{filename}' moved to {extension.upper() + '-files'}")
                    except Exception:
                        pass

    print("\n---------------------END------------------------------")
    print(f"Total file extensions: {len(files_extension)}")
    print(f"Extensions: {files_extension}")
    print(f"Total files categorized: {count}")
    print("Congratulations, all files have been sorted")


start_app(user_address)  # method call
