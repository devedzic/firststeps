from pathlib import Path

def iter_child_filenames(dirpath):
    for child in dirpath.iterdir():
        if child.is_file():
            print(child)
            yield child.name


x = iter_child_filenames(r'K:\Vladan')
print(x)

