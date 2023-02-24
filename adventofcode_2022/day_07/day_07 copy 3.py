import sys
import sqlite3

if "test" in sys.argv:
    data_file = "sample.txt"
else:
    data_file = "input.txt"

verbose = False
if "verbal" in sys.argv:
    verbose = True


class Path:
    def __init__(self):
        self.root = "."
        self._path = [self.root]

    @property
    def path(self):
        if len(self._path) == 0:
            return "./"
        else:
            return "/".join(self._path) + "/"

    def __repr__(self):
        return self.path

    def __str__(self):
        return self.path

    def join(self, new_dir):
        # this does not add the new_dir to the path,
        # it just returns what it would look like.
        return self.path + new_dir + "/"

    def chdir(self, new_dir=".."):
        prev_dir = str(self.path)

        if new_dir == "/":
            self._path = [self.root]

        elif new_dir.isalpha():
            self._path.append(new_dir)

        else:
            self._path = self._path[:-1]

        if verbose:
            print(f"\tchange dir from {prev_dir} to {self.path}")


class Folder(dict):
    def __add__(self, x):
        print("My Sum =", sum(self.values()))
        return x + sum(self.values())

    def get_folder(self, location):
        this_folder = self

        # location ex ./a/b/c/d/
        path = [f"{x}/" for x in location[:-1].strip().split("/")]
        print("path example",path)
        target_folder = path[-1]
        for level in path:
            if level == target_folder:
                return this_folder[level]
            this_folder = this_folder[level]

    def get_size(self, location):
        return sum(self.get_folder(location))

    def new_file(self, name, size, location):
        path = [f"{x}/" for x in location[:-1].strip().split("/")]
        target_folder = path[-1]
        this_folder = self

        for level in path:
            if level == target_folder:
                this_folder[level][name] = size
            this_folder = this_folder[level]

    def new_folder(self, location):
        path = [f"{x}/" for x in location[:-1].strip().split("/")]
        if len(path) == 1 and len(self) == 0:
            self["./"] = Folder()
        else:
            target_folder = path[-1]
            this_folder = self
            for folder in path:
                if folder == target_folder:
                    this_folder[folder] = Folder()
                else:
                    this_folder = this_folder[folder]


if __name__ == "__main__":
    data = list(open(data_file).readlines())
    current_dir = Path()
    Directory = Folder()
    Directory.new_folder(current_dir.path)

    for index, command in enumerate(data):
        print(f"Command line {index + 1}: {command}", end="")
        if command == "$ ls":
            continue  # we don't need to test these lines

        # change current directory to new folder
        if command.startswith("$ cd"):
            current_dir.chdir(new_dir=str(command.strip().split(" ")[-1]))
            print(Directory.get_folder(current_dir.path))

        # this means we found a directory, add it to the tree
        if command.startswith("dir"):
            new_path = current_dir.join(command.strip().split(' ')[-1])
            Directory.new_folder(new_path)

        # this means we found a file, add it to the tree
        if command[0].isnumeric():
            f_size, f_name = command.strip().split(" ")
            Directory.new_file(f_name, f_size, current_dir.path)

    print("\n\n\n",Directory)
    print("sum of directory tree:", sum(Directory.values()))

# Find all of the directories with a total size <= 100,000
# What is the sum of the total sizes of those directories?
