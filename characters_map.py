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

# todo: use only modification if it will produce a valid int !
int_part_map_for_existing = {
    0: {
        'missing': [3],
        'existing': [0, 1, 2, 4, 5, 6]
    },
    1: {
        'missing': [0, 1, 3, 4, 6],
        'existing': [2, 5]
    },
    2: {
        'missing': [1, 5],
        'existing': [0, 2, 3, 4, 6]
    },
    3: {
        'missing': [1, 4],
        'existing': [0, 2, 3, 4, 6]
    },
    4: {
        'missing': [0, 4],
        'existing': [1, 2, 3, 5]
    },
    5: {
        'missing': [2, 4],
        'existing': [0, 1, 3, 5, 6]
    },
    6: {
        'missing': [2],
        'existing': [0, 1, 3, 4, 5, 6]
    },
    7: {
        'missing': [1, 3, 4, 6],
        'existing': [0, 2, 5]
    },
    8: {
        'missing': [],
        'existing': [0, 1, 2, 3, 4, 5, 6]
    },
    9: {
        'missing': [4],
        'existing': [0, 1, 2, 3, 5, 6, ]
    },
}
