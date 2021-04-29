import configparser

config_file_name = 'config.ini'

config = configparser.ConfigParser()
config.read(config_file_name)


try:
    ERROR_PREFIX = config['text']['error_prefix']
    WIDTH_OF_CHAR = int(config['settings']['width_of_char'])
    WIDTH_OF_CHAR = int(config['settings']['width_of_char'])
    NUMBER_OF_CHARACTERS_PER_ROW = int(config['settings']['number_of_characters_per_row'])
    ROW_LEN = int(config['settings']['row_len'])
except Exception as e:
    print(f'{ERROR_PREFIX} Probem in loading configs: {e}')


# to check:
# [print(i) for i in settings]
