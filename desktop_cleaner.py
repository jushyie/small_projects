import os
import shutil

path = "/Users/jushyie/Desktop"

print(os.listdir(path))

folders = {
    "Images": [".png", ".jpeg", ".jpg"],
    "Steam_Games": [".app"],
    "Website": [".webloc"]
}

for file in os.listdir(path):
    item_path = os.path.join(path, file)
    if os.path.isdir(item_path):
        continue
    

    _, extension = os.path.splitext(file)
    extension = extension.lower()
    for folder, ext in folders.items():
        if extension in ext:
            # folder directory
            folder_path = os.path.join(path, folder)
            # create the folder if does not yet exist
            os.makedirs(folder_path, exist_ok = True)
            # move the file to that folder
            shutil.move(item_path, os.path.join(folder_path, file))
            break
    
    
