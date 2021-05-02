import os

from characters_map import character_map
from utils import read_file, create_row_string, write_data_to_file, repair_rows_if_wrong_length, check_and_create_folders, get_corrections, get_digit_from_string
from config import WIDTH_OF_CHAR, NUMBER_OF_CHARACTERS_PER_ROW, ROW_LEN, FEEDBACK_PREFIX, ILL_SUFFIX, ERR_SUFFIX, AMB_SUFFIX


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
    If checksum is valid, Suffix -> None
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


def validation_and_correction(characters_parsed, data_string, characters_parsed_with_more_solutions):
    valid_solutions = []

    row_string, suffix = validate_a_row(characters_parsed)
    orig_solution = row_string, suffix

    if len(characters_parsed_with_more_solutions) > 0:

        for characters_parsed_this in characters_parsed_with_more_solutions:
            row_string, suffix = validate_a_row(characters_parsed_this)
            if suffix is None:
                valid_solution = row_string, suffix
                valid_solutions.append(valid_solution)

        if 1 < len(valid_solutions) or len(valid_solutions) < 1:
            row_string, suffix = orig_solution[0], AMB_SUFFIX
        else:
            row_string, suffix = valid_solutions[0][0]

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
        characters_parsed_with_more_solutions = []

        solutions_number = 1
        for character in entry:
            if_more_digits = False
            if len(character) < 9:
                print(f'{FEEDBACK_PREFIX} bad: ', character)
            else:
                digit = get_digit_from_string(character)

                if digit is None:
                    corrected_digit_list = []

                    # get possible corrections
                    corrections = get_corrections(character)

                    # try to convert correction into int
                    for correction in corrections:
                        one_digit = get_digit_from_string(correction)
                        if one_digit is not None:
                            corrected_digit_list.append(digit)
                            if_more_digits = True
                            solutions_number += 1

                # create new list if there are many solutions
                if if_more_digits:
                    for one_digit in corrected_digit_list:
                        orig_list_copy = characters_parsed.copy()
                        orig_list_copy.append(one_digit)
                        characters_parsed_with_more_solutions.append(orig_list_copy)

                # append original list and multiple lists with original digit
                characters_parsed.append(digit)

                if characters_parsed_with_more_solutions:
                    for one_list in characters_parsed_with_more_solutions:
                        if not corrected_digit_list:
                            one_list.append(digit)
                        else:
                            for one_digit in corrected_digit_list:
                                one_list.append(one_digit)

        data_ints.append(characters_parsed)

        # DO VALIDATION
        validation_and_correction(characters_parsed, data_string, characters_parsed_with_more_solutions)

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
    test_mode_file_name = 'use_case_a.txt'  # comment it out to use CLI
    main(test_mode_file_name)
