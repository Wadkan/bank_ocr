import configparser

config_file_name = 'config.ini'

config = configparser.ConfigParser()
config.read(config_file_name)

WIDTH_OF_CHAR = int(config['settings']['width_of_char'])
WIDTH_OF_CHAR = int(config['settings']['width_of_char'])
NUMBER_OF_CHARACTERS_PER_ROW = int(config['settings']['number_of_characters_per_row'])
ROW_LEN = int(config['settings']['row_len'])

ERROR_PREFIX = config['text']['error_prefix']
FEEDBACK_PREFIX = config['text']['feedback_prefix']

# to check:
# [print(i) for i in settings]
