def read_file(path):
    try:
        file=open(path, "r")
        content=file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("cannot find the file")