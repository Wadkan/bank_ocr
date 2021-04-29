import os
from unittest import TestCase
from os.path import dirname, abspath
import filecmp

target = __import__('main')
parent_path = dirname(dirname(abspath(__file__)))


class Test(TestCase):
    def test_new_file_created(self):
        filename = "use_case_1.txt"
        target.main(filename)

        output_file_with_path = os.path.join(parent_path, "parsed_files", filename)

        self.assertTrue(os.path.isfile(output_file_with_path))

    def test_use_case_1_create_correct_file(self):
        filename = "use_case_1.txt"
        target.main(filename)

        output_file_with_path = os.path.join(parent_path, "parsed_files", filename)
        correct_file_with_path = os.path.join(parent_path, "correct_parsed_files", filename)

        self.assertTrue(filecmp.cmp(output_file_with_path, correct_file_with_path, shallow=False))
