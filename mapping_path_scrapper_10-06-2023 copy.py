import os
import shutil

dir_path = input(r'Enter path of the folder: ').replace('"', '')

# Create an output folder where all non directory files will land
if 'OutputFolder' not in os.listdir(dir_path):
    os.mkdir(os.path.join(dir_path, 'OutputFolder')) 

# Location where all items will be moved to
target_dir = dir_path + '\OutputFolder'

# Variables
initialFolders = []

def start():
    print('Original list: ' + str(os.listdir(dir_path)))
    # Creat initial list of only folders in main file
    for name in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, name)) and name != 'OutputFolder':
            initialFolders.append(os.path.join(dir_path, name))

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
                print(path)
                realPath = win32_fix_long_path(os.path.join(path, name))
                if name not in os.listdir(target_dir):
                    shutil.move(realPath, target_dir)
    # If items is a folder, enter the folder
    for name in files:
            if os.path.isdir(os.path.join(path, name)):
                 enter_folder(os.path.join(path, name))

start()