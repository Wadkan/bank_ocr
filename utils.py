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
        print(f'Error during reading the file: {e}')
    else:
        print(f'File successfuly read into memory: {filename}')


def write_data_to_file(data, output_file_with_path):
    """
    Write data list into a file, every element into separate a row.
    :param data: list of Strings
    :param output_file_with_path: Path
    :return:
    """
    try:
        with open(output_file_with_path, "w") as output_file:
            for row in data:
                # row_string = ''.join(map(str, row))   # the easiest solution
                row_string = create_row_string(row)
                row_string += '\n'
                output_file.write(row_string)
    except Exception as e:
        return f'Error during writing: {e}'
    else:
        return f'Data parsed and saved into: {output_file_with_path}'


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
            elem = '_'
        row_string += str(elem)
    return row_string
