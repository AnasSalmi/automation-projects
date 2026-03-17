import os
import shutil
from pathlib import Path

folder = Path(r"C:\Users\DELL\Desktop\automation\week1\test")

destinations = {
    ".txt": "Text",
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "PDFs",
    ".mp3": "Music",
}

for file in folder.iterdir():
    if file.is_file():  # skip folders
        if file.suffix in destinations:
            dest_folder = folder / destinations[file.suffix]
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(dest_folder))
            print(f"moved {file.name} → {destinations[file.suffix]}/")
        else:
            print(f"{file.name} → unknown, skipping")