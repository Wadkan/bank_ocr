import os
import time

from characters_map import character_map
from config import ERROR_PREFIX, BAD_CHARACTER_SIGN, FEEDBACK_PREFIX
from os.path import dirname, abspath


def check_and_create_folders():
    """
    Check whether required folders exist.
    If not, create them and print.
    :rtype: void
    """
    path = dirname(abspath(__file__))

    required_folders_list = [
        'parsed_files',
        'raw_files',
        'correct_parsed_files'
    ]
    for folder in required_folders_list:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            print(f'{ERROR_PREFIX} folder: <{folder}> does not exist.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print(f'{FEEDBACK_PREFIX} folder: <{folder}> is created.')
            time.sleep(2)
            os.mkdir(folder_path)


def read_file(filename):
    """
    Read file and print errors.
    :param filename:
    :return: List of strings
    """
    try:
        with open(filename, "r") as raw_text:
            return raw_text.read().splitlines()
    except Exception as e:
        print(f'{ERROR_PREFIX} Error during reading the file: {e}')
    else:
        print(f'{ERROR_PREFIX} File successfuly read into memory: {filename}')


def write_data_to_file(data, output_file_with_path, mode):
    """
    Write data list into a file, every element into separate a row.
    :param data: list of Strings
    :param output_file_with_path: Path
    :param mode: 'string': rows as strings, 'int': rows as List of ints
    :return: void
    """
    output_file_with_path += f'_{mode}_out'

    try:
        with open(output_file_with_path, "w") as output_file:
            for row in data:
                if mode == 'int':
                    row_string = create_row_string(row)
                elif mode == 'string':
                    row_string = row

                row_string += '\n'

                output_file.write(row_string)
    except Exception as e:
        feedback = f'Error during writing: {e}'
    else:
        feedback = f'Data parsed and saved into: {output_file_with_path}'

    print(FEEDBACK_PREFIX, feedback)


def create_row_string(row):
    """
    Convert list to string, if wrong character, sign it with '_'
    :param row:
    :return: String
    """
    row_string = ''
    for elem in row:
        if elem is None:
            row_string += BAD_CHARACTER_SIGN
        elif elem > 9:
            # in case of hex
            row_string += str(hex(10))[2:].upper()
        else:
            # in case of int
            row_string += str(elem)

    return row_string


def repair_rows_if_wrong_length(row, row_len):
    """
    Check the length of the rows and add extra String ' ' if shorter, or cut the end if longer.
    :param row: String
    :param row_len: required length
    :return:
    """
    if len(row) < row_len:
        plus_spaces = ''.join([' ' for p in range(row_len - (len(row)))])
        row += plus_spaces
    elif len(row) > row_len:
        row = row[:row_len]
    return row


def get_corrections(char_to_correct):
    """

    :param char_to_correct: one character string representation
    :return: available correction List of Strings
    """
    # 8 is the digit, that uses all parts
    FULL_DIGIT = character_map[8]

    def change_one_part(char, elem_num, new_part):
        char_list = list(char)
        char_list[elem_num] = new_part
        return "".join(char_list)

    # char_to_correct = character_map[digit_char]

    corrections = []
    for i in range(len(char_to_correct)):
        char_part = char_to_correct[i]
        char_part_if_full = FULL_DIGIT[i]

        # part is empty, but could be full
        if char_part == ' ' and char_part_if_full != ' ':
            correction = change_one_part(char_to_correct, i, char_part_if_full)
            corrections.append(correction)

        # part is not empty, correct to empty
        if char_part != ' ':
            correction = change_one_part(char_to_correct, i, ' ')
            corrections.append(correction)

    return corrections


def get_digit_from_string(character):
    digit = None
    for elem in character_map.keys():
        if character == character_map[elem]:
            digit = elem
    return digit
