import day_06


def test_build_grid():
    sizes = [2, 5, 10]
    for size in sizes:
        test_grid = day_06.build_grid(size, size)
        assert len(test_grid) == size
        for row in test_grid:
            assert len(row) == size


def test_light_count():
    test_grid = day_06.build_grid(5, 5)
    count = day_06.light_count(test_grid)
    assert count == 0

    test_grid = day_06.build_grid(5, 5, 1)
    count = day_06.light_count(test_grid)
    assert count == 5 * 5


def test_activate():
    test_size = 5
    test_grid = day_06.build_grid(test_size, test_size)

    activated_grid = day_06.activate("1,1", "2,2", test_grid)
    truth_table = {1: [(1, 1), (1, 2), (2, 1), (2, 2)],
                   0: [(0, 0), (0, 1), (0, 2),  (0, 3), (0, 4),
                       (1, 0), (1, 3), (1, 4),
                       (2, 0), (2, 3), (2, 4),
                       (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                       (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]}

    for z, loc in truth_table.items():
        for y in range(5):
            for x in range(5):
                test_loc = activated_grid[y][x]
                assert (y, x) in truth_table[test_loc]


def test_deactivate():
    test_size = 5
    test_grid_changes = day_06.build_grid(test_size, test_size, 1)
    test_grid_nochanges = day_06.build_grid(test_size, test_size, 0)

    deactivated_grid = day_06.deactivate("1,1", "2,2", test_grid_changes)
    deactivated_grid_nochanges = day_06.deactivate(
        "1,1", "2,2", test_grid_nochanges)

    truth_table = {0: [(1, 1), (1, 2), (2, 1), (2, 2)],
                   1: [(0, 0), (0, 1), (0, 2),  (0, 3), (0, 4),
                       (1, 0), (1, 3), (1, 4),
                       (2, 0), (2, 3), (2, 4),
                       (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                       (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]}

    for z, loc in truth_table.items():
        for y in range(5):
            for x in range(5):
                test_loc_changed = deactivated_grid[y][x]

                assert deactivated_grid_nochanges[y][x] == 0
                assert (y, x) in truth_table[test_loc_changed]


def test_light_count():
    test_size = 5
    test_grid_0 = day_06.build_grid(
        test_size, test_size, 0)  # 25 cells all equal to 0
    test_grid_1 = day_06.build_grid(
        test_size, test_size, 1)  # 25 cells all equal to 1

    assert day_06.light_count(test_grid_0) == 0
    assert day_06.light_count(test_grid_1) == test_size * test_size


def test_toggle():
    test_size = 5

    # default grid 5x5 all defaulted to off
    test_grid = day_06.build_grid(test_size, test_size)

    # make sure the target locs are off
    # for y in [2, 3]:
    #     for x in [2, 3]:
    #         assert test_grid[y][x] == 0

    # only works if light_count passed too
    assert day_06.light_count(test_grid) == 0

    toggled_grid = day_06.toggle("2,2", "3,3", test_grid)

    # now assert the target locs have been activated

    # general test only works if light_count passed too
    assert day_06.light_count(toggled_grid) == 4

    # for specifics test each targeted cell
    for y in [2, 3]:
        for x in [2, 3]:
            assert toggled_grid[y][x] == 1

    toggled_grid_2 = day_06.toggle("0,2", "2,2", test_grid)

    # manual truth table for what's on and what's off
    lights = {1: [(2, 3), (3, 2), (0, 2), (3, 3), (1, 2)],
              0: [(0, 0), (1, 0), (2, 2), (2, 0), (3, 0),
                  (4, 0), (0, 1), (1, 1), (2, 1), (3, 1),
                  (4, 1), (4, 2), (0, 3), (1, 3), (4, 3),
                  (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]}

    for z, loc in lights.items():
        for y in range(5):
            for x in range(5):
                test_loc = toggled_grid_2[y][x]
                assert (y, x) in lights[test_loc]


def test_instructions():
    test_raw_instructions = list(open("input.txt").readlines())
    day_06.instructions(test_raw_instructions)
    for cmd, start_pos, end_pos in day_06.instructions(test_raw_instructions):
        assert cmd in ["off", "on", "toggle"]
        sx, sy = start_pos.split(",")
        ex, ey = end_pos.split(",")
        assert str(sx).isnumeric() and str(sy).isnumeric()
        assert str(ex).isnumeric() and str(ey).isnumeric()
