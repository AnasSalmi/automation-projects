import hashlib
from pathlib import Path

def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()
    


folder = Path(r"C:\Users\DELL\Desktop\automation\week1\test2")

result={}
for file in folder.iterdir():
    if file.is_file():
        h=get_hash(file)
        if h in result:
            result[h].append(file.name)
        else:
            result[h]=[file.name]
    


for hash, files in result.items():
    if len(files) > 1:
        print(f"duplicates found: {files}")