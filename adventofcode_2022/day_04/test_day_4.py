import day_4


def test_cleanup():

    test_data = [
        "8-17,16-49",
        "17-38,18-36",
        "17-43,43-43",
        "86-94,7-87",
        "23-97,22-85",
    ]

    for i in test_data:
        assert "\n" not in day_4.cleanup(i)


test_data_ranges = [
    "8-17",
    "16-49",
    "17-38",
    "18-36",
    "17-43",
    "43-43",
    "86-94",
    "7-87",
    "23-97",
    "22-85",
]

def test_work_range():
    for data in test_data_ranges:
        test_elf = day_4.Elf(data)
        assert test_elf.min <= test_elf.max

        if test_elf.min == test_elf.max:
            assert int(test_elf.work_range) == test_elf.max




