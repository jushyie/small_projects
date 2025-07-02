import shutil
import os

folder = "Downloads"

def organize_folder(folder):
    path = f"/Users/jushyie/{folder}"
    types = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".txt", ".zip"],
        "Installers": [".dmg"],
        "Books": [".epub"]
    }
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path): # if file is a folder
            continue
    
        _, ext = os.path.splitext(file)
        ext = ext.lower()
        for f, e in types.items():
            if ext in e:
                # create new folder
                folder_path = os.path.join(path, f)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved {file} to {f}.")

organize_folder(folder)