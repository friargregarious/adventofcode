import sys, math

if "test" in sys.argv:
    datafile = "sample.txt"
else:
    datafile = "input.txt"

FORREST = []
TOTAL_TREES = 0
MAX_ROW_INDEX = int()

for row in open(datafile).readlines():
    FORREST_row = row.strip()
    TOTAL_TREES += len(FORREST_row)
    FORREST.append(FORREST_row)
    if len(FORREST_row) > MAX_ROW_INDEX:
        MAX_ROW_INDEX = len(FORREST_row)

MAX_COL_INDEX = len(FORREST)
MAX_COL_INDEX -= 1  # MAX Y index (N TO S)
MAX_ROW_INDEX -= 1  # MAX X index (W TO E)

(N, E, S, W, OUT) = ("N", "E", "S", "W", "Out")  # [x for x in range(4)]


class Tree(dict):
    """ A Tree object has an Row and Column coordinate (row, col)
        it has 4 directions it might be seen from (N, E, S, W)
    """

    def __init__(self, row, col):
        self._row = row  # Which Row am I in?
        self._col = col  # Which Column am I in?
        self._view_quality = []

    def is_visible(self):
        return True in self.values()

    def view_quality(self):
        return math.prod(self._view_quality)

    def how_far_do_I_see(self):
        THIS_ROW = [int(i) for i in FORREST[self._row]]
        THIS_COL = [int(row[self._col]) for row in FORREST]
        MY_HEIGHT = int(FORREST[self._row][self._col])

        # Looking NORTH
        view_count = 0
        view = list(THIS_COL[:self._row])
        view.reverse()
        for target_height in view:
            view_count += 1
            if target_height >= MY_HEIGHT:
                break
        self._view_quality.append(view_count)

        # Looking SOUTH
        view_count = 0
        view = list(THIS_COL[self._row + 1:])
        for target_height in view:
            view_count += 1
            if target_height >= MY_HEIGHT:
                break
        self._view_quality.append(view_count)

        # Looking EAST
        view_count = 0
        view = list(THIS_ROW[self._col + 1:])
        for target_height in view:
            view_count += 1
            if target_height >= MY_HEIGHT:
                break
        self._view_quality.append(view_count)

        # Looking WEST
        view_count = 0
        view = list(THIS_ROW[:self._col])
        view.reverse()
        for target_height in view:
            view_count += 1
            if target_height >= MY_HEIGHT:
                break
        self._view_quality.append(view_count)

        # return math.prod(self._view_quality)

    def can_I_be_seen(self):  # store TRUTH and return it

        # outside ring of trees test
        if self._row in [0, len(FORREST)-1] or self._col in [0, len(FORREST[self._row])-1]:
            self[OUT] = True

        # Inside the forrest we need to check for heights of all trees inline
        else:
            THIS_ROW = [int(i) for i in FORREST[self._row]]
            THIS_COL = [int(row[self._col]) for row in FORREST]
            MY_HEIGHT = int(FORREST[self._row][self._col])

            # N S
            self[N] = MY_HEIGHT > max(list(THIS_COL[:self._row]))
            self[S] = MY_HEIGHT > max(list(THIS_COL[self._row + 1:]))
            # E W
            self[W] = MY_HEIGHT > max(list(THIS_ROW[:self._col]))
            self[E] = MY_HEIGHT > max(list(THIS_ROW[self._col + 1:]))

        self.how_far_do_I_see()
        return self.is_visible()

    @property
    def loc(self):
        return (self._row, self._col, )


# Truth table, stores only True and false values
working = {True: [], False: []}
best_loc = 0


for ROW_INDEX_Y, row in enumerate(FORREST):
    for COL_INDEX_X, tree in enumerate(row):
        this_tree = Tree(ROW_INDEX_Y, COL_INDEX_X)
        this_tree.can_I_be_seen()

        if best_loc < this_tree.view_quality() :
            best_loc = this_tree.view_quality()

        working[this_tree.is_visible()].append(this_tree.loc)

        print(this_tree.loc, this_tree.is_visible(), [
              f"{k}, {v}".rjust(10) for k, v in sorted(this_tree.items())])


print("Total Trees seen:", len(working[True]), "of", TOTAL_TREES)
print("Best view is", best_loc)