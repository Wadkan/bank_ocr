import os

from characters_map import characters_map_dict
from utils import read_file, create_row_string, write_data_to_file, repair_rows_if_wrong_length, check_and_create_folders
from config import WIDTH_OF_CHAR, NUMBER_OF_CHARACTERS_PER_ROW, ROW_LEN, ERROR_PREFIX, FEEDBACK_PREFIX, ILL_SUFFIX, ERR_SUFFIX


def parse_file_into_entries(raw_text):
    """
    Parse '_' and '|' signs from multiple rows into characters.
    :param raw_text: List of Strings
    :return: List of String Lists
    """

    i = 0
    entries = []

    for row in raw_text:
        row = repair_rows_if_wrong_length(row, ROW_LEN)

        # if first row, create empty elements into the list
        if i == 0:
            characters = ['' for x in range(NUMBER_OF_CHARACTERS_PER_ROW)]

        if i == 3:
            # save entry
            entries.append(characters)

            i = 0
            characters = []
        else:
            # build characters from row text
            num_of_char = 0
            for part_of_character_end in range(3, (len(row) + 1), WIDTH_OF_CHAR):
                part_of_char = row[
                               (part_of_character_end - WIDTH_OF_CHAR):part_of_character_end
                               ]

                characters[num_of_char] += part_of_char
                num_of_char += 1

            i += 1

    return entries


def validate_a_row(row):
    """
    Calculate checksum, and print the validation using the proper SUFFIX.
    :param row: List of ints
    :return: Data (String), Suffix (String)
    """
    wrong_flag = False
    check_summary = 0
    for i in range(len(row)):
        row_string = create_row_string(row)

        if row[i] is None:
            wrong_flag = True
            continue
        check_summary += (len(row) - i) * row[i]
    if not wrong_flag:
        checksum = check_summary % 11
        if checksum == 0:
            row_final = row_string, None
        else:
            row_final = row_string, ERR_SUFFIX
    else:
        row_final = row_string, ILL_SUFFIX
    return row_final


def validation_and_correction(characters_parsed, data_string):
    row_string, suffix = validate_a_row(characters_parsed)
    characters_parsed_string = f'{row_string} {suffix}'
    data_string.append(characters_parsed_string)
    print(characters_parsed_string)


def parse_entries_into_data(entries):
    """
    Parse '_' amd '|' characters into int
    :param entries: List of Strings
    :return: List of Int Lists
    """
    data_ints = []
    data_string = []

    for entry in entries:

        characters_parsed = []

        for character in entry:
            if len(character) < 9:
                print(f'{FEEDBACK_PREFIX} bad: ', character)
            else:
                # digit = [elem for elem in characters_map_dict.keys() if character == characters_map_dict[elem]]

                digit = None
                for elem in characters_map_dict.keys():
                    if character == characters_map_dict[elem]:
                        digit = elem

                characters_parsed.append(digit)

        data_ints.append(characters_parsed)

        # DO VALIDATION
        validation_and_correction(characters_parsed, data_string)

    return data_ints, data_string


def main(test_mode_file_name=False):
    check_and_create_folders()

    if not test_mode_file_name:
        print("Welcome!")
        filename = input("Please type input_filename from raw_files folder and hit enter: ")
    else:
        filename = test_mode_file_name

    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_file_with_path = os.path.join(dir_path, "raw_files", filename)
    output_file_with_path = os.path.join(dir_path, "parsed_files", filename)

    raw_text = read_file(input_file_with_path)
    entries = parse_file_into_entries(raw_text)
    data_ints, data_string = parse_entries_into_data(entries)

    write_data_to_file(data_ints, output_file_with_path, 'int')
    write_data_to_file(data_string, output_file_with_path, 'string')


if __name__ == '__main__':
    test_mode_file_name = 'use_case_4_in.txt'  # comment it out to use CLI
    main(test_mode_file_name)
