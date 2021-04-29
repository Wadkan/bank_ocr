import os

from characters_map import characters_map_dict


def read_file(filename):
    try:
        with open(filename, "r") as raw_text:
            return raw_text.read().splitlines()
    except Exception as e:
        print(f'Error during reading the file: {e}')
    else:
        print(f'File successfuly read into memory: {filename}')


def parse_file_into_entries(raw_text):
    width_of_char = 3  # todo: remove
    number_of_characters_per_row = 9  # todo: remove
    row_len = 27  # todo: remove

    i = 0
    entries = []

    for row in raw_text:
        if len(row) < row_len:
            plus_spaces = ''.join([' ' for p in range(row_len - (len(row)))])
            row += plus_spaces
        elif len(row) > row_len:
            row = row[:row_len]

        # if first row, create the elements of the list
        if i == 0:
            characters = ['' for elem in range(number_of_characters_per_row)]

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


def write_data_to_file(data, output_file_with_path):
    try:
        with open(output_file_with_path, "w") as output_file:
            for row in data:
                row_string = ''.join(map(str, row))
                row_string += '\n'
                output_file.write(row_string)
    except Exception as e:
        return f'Error during writing: {e}'
    else:
        return f'Data parsed and saved into: {output_file_with_path}'


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
    if_success = write_data_to_file(data, output_file_with_path)
    print(if_success)


if __name__ == '__main__':
    test_mode_file_name = 'use_case_1.txt'
    main(test_mode_file_name)
