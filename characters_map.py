int_map_dict = {
    0:
        " _ " +
        "| |" +
        "|_|",
    1:
        "   "
        "  |"
        "  |",
    2:
        " _ " +
        " _|" +
        "|_ ",
    3:
        " _ " +
        " _|" +
        " _|",
    4:
        "   " +
        "|_|" +
        "  |",
    5:
        " _ " +
        "|_ " +
        " _|",
    6:
        " _ " +
        "|_ " +
        "|_|",
    7:
        " _ " +
        "  |" +
        "  |",
    8:
        " _ " +
        "|_|" +
        "|_|",
    9:
        " _ " +
        "|_|" +
        " _|"
}

int_part_map_for_existing = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 4, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6, ],
}

all_part = list(range(0, 7))


for chars in int_part_map_for_existing.values():
    print('existing: ', chars)
    diff = list(set(all_part) - set(chars))
    print('diff: ', diff)
