import os


def read_file(filename):
    with open(filename, "r") as raw_text:
        return raw_text.readlines()


def parse_file_into_data(raw_text):
    width_of_char = 3  # todo: replace
    number_of_characters_per_row = 9  # todo: replace

    i = 0
    entries = []

    for row in raw_text:
        # if first row, create the elements of the list
        if i == 0:
            characters = ['' for elem in range(number_of_characters_per_row)]

        elif i == 4:
            # parse characters
            entry = characters

            # save entry
            entries.append(entry)

            i = 0
            characters = []
            continue    # leave incrementation and start from the next entry

        else:
            # build characters from row text
            num_of_char = 0
            for part_of_character_end in range(3, len(row), width_of_char):
                part_of_char = row[
                               (part_of_character_end - width_of_char):part_of_character_end
                               ]

                characters[num_of_char] += part_of_char
                num_of_char += 1
            print(characters)

        i += 1


def main():
    # print("Welcome!")
    # filename = input("Please type filename from raw_files folder and hit enter: ")
    filename = "file1.txt"
    file_with_path = os.path.join("raw_files", filename)
    raw_text = read_file(file_with_path)
    data = parse_file_into_data(raw_text)
    print(data)


if __name__ == '__main__':
    main()
