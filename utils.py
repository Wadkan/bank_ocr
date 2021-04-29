from config import ERROR_PREFIX, BAD_CHARACTER_SIGN, FEEDBACK_PREFIX


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
    output_file_with_path += f'{mode}_output_file_with_path'

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
    # row_string = ''.join(map(str, row))

    row_string = ''
    for elem in row:
        if elem is None:
            elem = BAD_CHARACTER_SIGN
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
