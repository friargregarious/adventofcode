import sys

VERBOSE = "verbose" in sys.argv
sample = list(open("sample.txt").readlines())

def instructions(source:list):
    for row in source:
        row = str(row).strip()
        if row.startswith("$ ls"):
            continue 

        elif row.startswith("dir"):
            a, b = row.split(" ")
            yield a, b, None

        elif row.startswith("$ cd"):
            yield "cd", row.split(" ")[-1], None

        elif row.split(" ")[0].isnumeric():
            f_size, f_name = row.split(" ")
            yield "file", f_name, int(f_size)

class File:
    def __init__(self, size):
        self.size = size


class Folder:
    def __init__(self, size):
        self.contents = []
        self.size = sum(self.contents)

def current_location(p:list):
    return "/".join(p) + "/"

def add_dir(t:dict,p:list, target:str):
    this_level = t
    for level in p[:-1]:
        this_level = t[level]
        
    dict  this_level

path = ["."]
tree = {"." : {}}
for cmd, target, size in iter(instructions(sample)):
    
    print(cmd, target, size, path, current_location(path))

    if cmd == "cd":
        if target == "..":
            path.pop()
        elif target == "/":
            path = ["."]
        else:
            path.append(target)



