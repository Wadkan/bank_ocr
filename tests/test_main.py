import os
from unittest import TestCase
from os.path import dirname, abspath

target = __import__('main')
parent_path = dirname(dirname(abspath(__file__)))


class Test(TestCase):
    def test_new_file_created(self):
        filename = "use_case_1.txt"
        target.main(filename)
        out_filename1 = 'use_case_1.txt_int_out'
        out_filename2 = 'use_case_1.txt_string_out'

        output_file_with_path1 = os.path.join(parent_path, "parsed_files", out_filename1)
        output_file_with_path2 = os.path.join(parent_path, "parsed_files", out_filename2)

        self.assertTrue(os.path.isfile(output_file_with_path1) and os.path.isfile(output_file_with_path2))


# There was not enough time to write more tests.