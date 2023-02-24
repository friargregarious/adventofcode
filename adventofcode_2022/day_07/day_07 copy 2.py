import sys, sqlite3

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


if __name__ == "__main__":

    CONN = sqlite3.connect("working.db3")
    curs = CONN.cursor()

    drop_files = "DROP TABLE IF EXISTS Files;"
    drop_folders = "DROP TABLE IF EXISTS Folders;"

    Build_Folders_table = """CREATE TABLE "Folders" (
                                "id"	INTEGER NOT NULL UNIQUE,
                                "FolderName"	TEXT,
                                "Parent"	TEXT,
                            PRIMARY KEY("id" AUTOINCREMENT) ) """

    Build_Files_Table = """CREATE TABLE "Files" (
	                            "id"	INTEGER NOT NULL UNIQUE,
                                "Parent"	INTEGER,
                                "FileName"	TEXT,
                                "size"	INTEGER,
                            PRIMARY KEY("id" AUTOINCREMENT),
                            FOREIGN KEY("Parent") REFERENCES "Folders"("id") )"""

    init_folders = "INSERT INTO Folders (FolderName, Parent) VALUES ('./', './');"


    data = list(open(data_file).readlines())
    current_dir = Path()

    for SQL in [drop_files, drop_folders, Build_Folders_table, Build_Files_Table, init_folders]:
        curs.execute(SQL)
        CONN.commit()

    for index, command in enumerate(data):
        print(f"Command line {index + 1}: {command}", end="")
        if command == "$ ls":
            continue  # we don't need to test these lines

        # change current directory to new folder
        if command.startswith("$ cd"):
            current_dir.chdir(new_dir=str(command.strip().split(" ")[-1]))

        # this means we found a directory, add it to the tree
        if command.startswith("dir"):
            new_path = str(current_dir.join(command.strip().split(' ')[-1]))

            # INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
            # VALUES('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

            SQL = f"INSERT INTO Folders (FolderName, Parent) VALUES ('{new_path}', '{current_dir.path}');"

            print(SQL)
            curs.execute(SQL)
            CONN.commit()

        # this means we found a file, add it to the tree
        if command[0].isnumeric():
            f_size, f_name = command.strip().split(" ")

            SQL = f"INSERT INTO Files (FileName, Parent, size) VALUES ('{f_name}', '{current_dir.path}', {int(f_size)});"

            print(SQL)
            curs.execute(SQL)
            CONN.commit()

    SQL = """SELECT Folders.FolderName, sum(Files.size) as size
                FROM Folders
                LEFT JOIN Files
                ON Folders.id = Files.Parent
                GROUP by FolderName"""
    
    results = curs.execute(SQL).fetchall()

    for row in results:
        print(row)


# Find all of the directories with a total size of at most 100000.
# What is the sum of the total sizes of those directories?
