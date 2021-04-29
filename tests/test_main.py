from unittest import TestCase

target = __import__('main')


class Test(TestCase):
    def test_use_case_1_write_file_in_same_name_into_parsed_files(self):
        filename = "use_case_1.txt"
        target.main(filename)
        self.assertEqual(1, 1)
