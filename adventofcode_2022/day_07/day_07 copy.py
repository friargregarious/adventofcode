import sys

if "test" in sys.argv:
    data_file = "sample.txt"
else:
    data_file = "input.txt"

verbose = False
if "verbal" in sys.argv:
    verbose = True


class File:
    def __init__(self, name, size=0, parent=None):
        self.parent = parent
        self.name = name
        self.size = size

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.size


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.folders = {}

    @property
    def size(self):
        # I thought this was a clever way of hiding a recursion
        s = 0
        for item in self.contents.values():
            s += item.size
        return s

    def new_thing(self, thing, target):
        target[thing.name] = thing

        if verbose:
            print(f"\tadded {thing.name} to {self.name}")

    def new_file(thing):
        self.new_thing(thing, self.files)

    def new_folder(thing):
        self.new_thing(thing, self.folders)



    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


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


def show_dir(dir):
    c = " ".join( list(dir.files.keys()) + list(dir.folders.keys()))
    print(f"\tSHOWING: {dir}: {c}")


if __name__ == "__main__":

    data = list(open(data_file).readlines())
    current_dir = Path()
    all_dirs = {
        current_dir.path: Dir(name=current_dir.path, parent=None)
    }

    for index, command in enumerate(data):
        print(f"Command line {index + 1}: {command}", end="")
        if verbose:
            show_dir(all_dirs[current_dir.path])


        if command == "$ ls":
            if verbose:
                print(f"\tListing contents of {current_dir.path}")
            continue  # we don't need to test these lines

        # change current directory to new folder
        if command.startswith("$ cd"):

            current_dir.chdir(new_dir=str(command.strip().split(" ")[-1]))

            if verbose:
                show_dir(all_dirs[current_dir.path])
            continue

        # this means we found a directory, add it to the tree
        if command.startswith("dir"):

            new_path = str(current_dir.join(command.strip().split(' ')[-1]))
            print("newpath", new_path)

            temp_folder = Dir(new_path, parent=current_dir.path)
 
            all_dirs[new_path] = temp_folder
            all_dirs[current_dir.path].new_folder(temp_folder)

            if verbose:
                show_dir(all_dirs[current_dir.path])

            continue

        # this means we found a file, add it to the tree
        if command[0].isnumeric():
            f_size, f_name = command.strip().split(" ")

            # make a file
            temp_file = File(name=f_name, size=int(
                f_size), parent=current_dir.path)

            # put it in the directory contents
            all_dirs[current_dir.path].new_file(temp_file)

            if verbose:
                show_dir(all_dirs[current_dir.path])

    # Find all of the directories with a total size of at most 100000.
    # What is the sum of the total sizes of those directories?

    with open("output.file", "w") as outfile:
        total = 0
        for k, v in all_dirs.items():
            smaller = v.size <= 100000
            if smaller:
                print(
                    f"{k.ljust(15, ' ')}\t{v.size}\t<= 100000 {smaller}", file=outfile)
                total += v.size
            else:
                print(f"{k.ljust(15, ' ')}\t{v.size}", file=outfile)
        print(
            f"\nTotal size of dirs smaller than 100000: {total}", file=outfile)
