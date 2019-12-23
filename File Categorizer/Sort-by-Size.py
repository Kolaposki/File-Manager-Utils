"""
    name='Sort-by-Size',
    project='File Sorter'
    date='12/22/2019',
    author='Oshodi Kolapo',
"""
import glob
import os
import shutil

address = 'C:/Users/KOLAPO/Desktop/sample'
os.chdir(address)

folders = ['XXsmall', 'Xsmall', 'Small', 'Medium', 'Large', 'Xlarge', 'XXlarge']
xxsmall_counter, xsmall_counter, small_counter = 0, 0, 0
medium_counter, file_counter = 0, 0
large_counter, xlarge_counter, xxlarge_counter = 0, 0, 0


def bytes2kb(byte: float):
    return round(byte / 1024, 2)


for folder in folders:
    try:
        os.mkdir(folder)
        print(f"{folder} folder created succesfully")
    except FileExistsError:
        pass

#  search for files recursively in subdirectories
for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file):
        file_counter += 1
        size_of_file = bytes2kb(os.path.getsize(file))

        # XXsmall
        if 0 <= size_of_file <= 1024:  # 0kb --> 1mb
            xxsmall_counter += 1
            try:
                shutil.move(file, folders[0])
                print(f"{file} moved to {folders[0]}")
            except Exception:
                pass


        # Xsmall
        elif 1024 < size_of_file <= 25600:  # 1mb --> 25mb
            xsmall_counter += 1
            try:
                shutil.move(file, folders[1])
                print(f"{file} moved to {folders[1]}")
            except Exception:
                pass

        # Small
        elif 25600 < size_of_file <= 102400:  # 25mb --> 100mb
            small_counter += 1
            try:
                shutil.move(file, folders[2])
                print(f"{file} moved to {folders[2]}")
            except Exception:
                pass

        # Medium
        elif 102400 < size_of_file <= 512000:  # 100mb --> 500mb
            medium_counter += 1
            try:
                shutil.move(file, folders[3])
                print(f"{file} moved to {folders[3]}")
            except Exception:
                pass

        # Large
        elif 512000 < size_of_file <= 1048576:  # 500mb --> 1gb
            large_counter += 1
            try:
                shutil.move(file, folders[4])
                print(f"{file} moved to {folders[4]}")
            except Exception:
                pass

        # Xlarge
        elif 1048576 < size_of_file <= 52428800:  # 1gb --> 50gb
            xlarge_counter += 1
            try:
                shutil.move(file, folders[5])
                print(f"{file} moved to {folders[5]}")
            except Exception:
                pass

        # XXlarge
        elif size_of_file > 52428800:  # 50gb --> x
            xxlarge_counter += 1
            try:
                shutil.move(file, folders[6])
                print(f"{file} moved to {folders[6]}")
            except Exception:
                pass

print("--------------------------------------------------------------------------")
print(f"Total files sorted --> {file_counter}")
print(f"Total {folders[0]} files --> {xxsmall_counter}")
print(f"Total {folders[1]} files --> {xsmall_counter}")
print(f"Total {folders[2]} files --> {small_counter}")
print(f"Total {folders[3]} files --> {medium_counter}")
print(f"Total {folders[4]} files --> {large_counter}")
print(f"Total {folders[5]} files --> {xlarge_counter}")
print(f"Total {folders[6]} files --> {xxlarge_counter}")
