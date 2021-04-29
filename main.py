import os

from characters_map import characters_map_dict
from utils import read_file, create_row_string, write_data_to_file, repair_rows_if_wrong_length


def parse_file_into_entries(raw_text):
    """
    Parse '_' and '|' signs from multiple rows into characters.
    :param raw_text: List of Strings
    :return: List of String Lists
    """
    width_of_char = 3  # todo: remove
    number_of_characters_per_row = 9  # todo: remove
    row_len = 27  # todo: remove

    i = 0
    entries = []

    for row in raw_text:
        row = repair_rows_if_wrong_length(row, row_len)

        # if first row, create empty elements into the list
        if i == 0:
            characters = ['' for x in range(number_of_characters_per_row)]

        if i == 3:
            # save entry
            entries.append(characters)

            i = 0
            characters = []
        else:
            # build characters from row text
            num_of_char = 0
            for part_of_character_end in range(3, (len(row) + 1), width_of_char):
                part_of_char = row[
                               (part_of_character_end - width_of_char):part_of_character_end
                               ]

                characters[num_of_char] += part_of_char
                num_of_char += 1

            i += 1

    return entries


def parse_entries_into_data(entries):
    """
    Parse '_' amd '|' characters into int
    :param entries: List of Strings
    :return: List of Int Lists
    """
    entries_parsed = []

    for entry in entries:

        characters_parsed = []

        for character in entry:
            if len(character) < 9:
                print('bad: ', character)
            else:
                # digit = [elem for elem in characters_map_dict.keys() if character == characters_map_dict[elem]]

                digit = None
                for elem in characters_map_dict.keys():
                    if character == characters_map_dict[elem]:
                        digit = elem

                characters_parsed.append(digit)

        entries_parsed.append(characters_parsed)

    return entries_parsed


def validate_account_numbers_checksum(data):
    """
    Calculate checksum, and print the validation: Invalid, Valid or Wrong character.
    :param data: List of Int Lists
    """
    for row in data:
        wrong_flag = False
        check_summary = 0

        for i in range(len(row)):
            row_string = create_row_string(row)

            if row[i] is None:
                print('Wrong character: ', row_string)
                wrong_flag = True
                continue
            check_summary += (len(row) - i) * row[i]

        if not wrong_flag:
            checksum = check_summary % 11
            if checksum == 0:
                print('Valid: ', row_string)
            else:
                print('Invalid: ', row_string)


def main(test_mode_file_name=False):
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
    data = parse_entries_into_data(entries)

    # validate account numbers
    validated_data = validate_account_numbers_checksum(data)

    if_success = write_data_to_file(data, output_file_with_path)
    print(if_success)


if __name__ == '__main__':
    test_mode_file_name = 'use_case_4_in.txt'
    main(test_mode_file_name)
