import os
import shutil

dir_path = input(r'Enter path of the folder: ').replace('"', '')
# dir_path = 'C:\\Users\\se_ba\\Downloads\\Nigh - Copy'

# Create an output folder where all non directory files will land
if 'OutputFolder' not in os.listdir(dir_path):
    os.mkdir(os.path.join(dir_path, 'OutputFolder')) 

# Location where all items will be moved to
target_dir = dir_path + '\OutputFolder'
# target_dir_duplicates = dir_path + '\OutputFolder_Duplicates'

# Variables
initialFolders = []

def start():
    print('Original list: ' + str(os.listdir(dir_path)))
    # Create initial list of only folders in main file
    for name in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, name)) and name != 'OutputFolder':
            initialFolders.append(os.path.join(dir_path, name))
            print(len(os.path.join(dir_path, name)))

    print('initialFolders')
    print(initialFolders)
    # Iterate through the intial list of folders
    for path in initialFolders:
        enter_folder(path)

def win32_fix_long_path(path):
    return  r'\\?\\' + os.path.realpath(path)

def enter_folder(path):
    files = os.listdir(path)
    # Iterate through the items in recently entered folder
    for name in files:
            # If item is not a folder, move the item to the OutputFolder
            if not os.path.isdir(os.path.join(path, name)):
                # If this name is already in output folder, compare file sizes to validate if different
                if name in os.listdir(target_dir):
                    src_size = os.stat(os.path.join(path, name)).st_size
                    trgt_size = os.stat(os.path.join(target_dir, name)).st_size
                    if src_size == trgt_size:
                         os.remove(os.path.join(path, name))
                         continue
                realPath = win32_fix_long_path(os.path.join(path, name))
                dup = 0
                while True:
                    dst_path = os.path.join(target_dir,name)
                    print(path)
                    if name not in os.listdir(target_dir):
                        break
                    dup += 1
                    base, ext = os.path.splitext(name)
                    name = f'{base}_{dup}{ext}'
                    
                os.rename(realPath, dst_path)

    # If items is a folder, enter the folder
    for name in files:
            if os.path.isdir(os.path.join(path, name)):
                 enter_folder(os.path.join(path, name))
    os.rmdir(path)

start()