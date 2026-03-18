import os
from pathlib import Path
from datetime import date

today= date.today()

date_string_ymd = today.strftime("%Y-%m-%d")

folder = Path(r"C:\Users\DELL\Desktop\automation\week1\test2")

for index, file in enumerate(folder.iterdir()):
    if file.is_file():
        new_name = f"{date_string_ymd}_{file.name}"
        new_path = folder / new_name
        file.rename(new_path)
        print(f"{file.name} → {new_name}")