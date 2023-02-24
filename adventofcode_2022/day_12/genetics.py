from random import randint, choice


def score(given_route, multiplier=100000, shortest_distance=10):
    # route = {rating: [steps...]}
    # rating = (length, score)
    for rating, route in given_route.items():
        length, score = rating
        if length != len(route):
            length = len(route)
        score = int((1 / (length-shortest_distance)) * multiplier)
        return {(length, score): route}


def is_valid_route(this_route, the_map):

    # loc = (row, col)
    # step = {loc: height}
    # steps = {step, step, step...}

    # length = len(steps)
    # score = score(route)

    # rating = (length, score)
    # route = {rating: steps}

    return True


def get_routes(seg_pop):

    for s, s_steps in seg_pop.start.items():
        for f, f_steps in seg_pop.finish.items():
            this_route = s_steps + f_steps
            if is_valid_route(this_route):
                # take completed routes and put them
                # in RoutePopulation for scoring and selection
                return i + h


# THE ROUTESEGMENT is an incomplete route that must be anchored
# by either a starting point or the finishing point.
# The idea is to work on the problem from both directions.


def available_steps(from_point, the_map, max_map_size=(25, 25)):
    fr, fc = from_point  # row/col
    mr, mc = max_map_size  # row/col

    # 1 step up, or down, or left, or right
    gens = [(fr+1, fc), (fr-1, fc), (fr, fc+1), (fr, fc-1)]
    possible = []
    for x, y in gens:
        if not (x == mr or x == -1) and not (x == mc or x == -1):
            possible.append((x, y))

    map_portion = {loc: the_map[loc] for loc in possible}

    return map_portion


def gen_random_segment(anchor, anchor_type, target_len=10):
    this_seg_len = randint(5, target_len)

    if anchor_type == "START":
        direction = 1
    else:
        direction = -1

    new_seg = [anchor]

    last_step = anchor
    for i in range(this_seg_len):
        if anchor_type == "START":
            this_step = None
        else:
            direction = -1

        possible_steps = available_steps(this_step)

        new_seg = [anchor] + new_seg

        new_seg = new_seg + [anchor]

    return new_seg


# Population

class RouteSegmentPopulation:
    def __init__(self, max_pop=50, cutoff=0.5):
        self.start = {}  # population of starting segments
        self.finish = {} # population of finishing segments
        self.max_pop = max_pop # largest qty of members in each population
        self.selection_cutoff = cutoff # percentage of total population


    def add(self, element, gender):
        if gender == "START":
            self.start.add(element)
        else:
            self.finish.add(element)

    def selection(self):
        cutoff = int(self.selection_cutoff * self.max_pop)

        working_pop = list(self.start.keys())
        working_pop.sort(reverse=True) ## highest scores first
        not_selected = working_pop[cutoff:]
        for i in not_selected:
            if i in self.start:
                del self.start[i]
        
        working_pop = list(self.finish.keys())
        working_pop.sort(reverse=True)  # highest scores first
        not_selected = working_pop[cutoff:]
        for i in not_selected:
            if i in self.finish:
                del self.finish[i]







class RouteSegment:
    def __init__(self, route, gender):
        self.route = route
        self._score = int()
        # genders are START or FINISH. can't merge two starting points
        self.gender = gender


# once a route has been determined by the segment generator
# it gets placed here for scoring,
class RoutePopulation:
    def __init__(self):
        self.group = set()

    def add(self, element):
        self.group.add(element)


class Route:
    def __init__(self, route, gender):
        self.route = route
        self._score = int()


# inheritance
def mate(element_1, element_2):
    len1 = len(element_1)
    len2 = len(element_2)
    shorter = min([len1, len2])
    split = shorter // 2 + \
        (randint(1, min([len1, len2]) // 4) * choice([-1, 1]))
    return element_1[:split] + element_2[split:]


# mutation
def mutation(element):
    max_index = len(element)
    mutate_index = randint(0, max_index)
    old_loc_x, old_loc_y = element[mutate_index]
    mutate_choice = choice(["x", "y"])
    if mutate_choice == "x":
        old_loc_x = old_loc_x + choice([-1, 1])
    else:
        old_loc_y = old_loc_y + choice([-1, 1])

    return element[:mutate_index] + new_loc + element[mutate_index + 1:]


if __name__ == "__main__":

    # loc = (row, col)
    # step = {loc: height}
    # steps = {step, step, step...}

    # length = len(steps)
    # score = score(route)

    # rating = (length, score)
    # route = {rating: steps}

    SHORT = 40
    test_route = {}
    test_route[(0, 0)] = {(x, x+50): int(randint(1, 10)) for x in range(40)}

    for y in range(SHORT):
        result = score(test_route, multiplier=100000,
                       shortest_distance=y)
        test_route.update(result)
        print("\n")
        for key in test_route:
            print(key)
