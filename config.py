import configparser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
config_file_name = 'config.ini'
config_file_path = os.path.join(dir_path, config_file_name)

config = configparser.ConfigParser()
config.read(config_file_path)

WIDTH_OF_CHAR = int(config['settings']['width_of_char'])
NUMBER_OF_CHARACTERS_PER_ROW = int(config['settings']['number_of_characters_per_row'])
ROW_LEN = int(config['settings']['row_len'])

ERROR_PREFIX = config['text']['error_prefix']
FEEDBACK_PREFIX = config['text']['feedback_prefix']
BAD_CHARACTER_SIGN = config['text']['bad_character_sign']
ERR_SUFFIX = config['text']['err_suffix']
ILL_SUFFIX = config['text']['ill_suffix']
AMB_SUFFIX = config['text']['amb_suffix']

# to check:
# [print(i) for i in settings]
