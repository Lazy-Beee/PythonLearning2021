import unittest
from name_function import get_formated_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formated_name('alien', 'white')
        self.assertEqual(formatted_name, 'Alien White')

    def test_first_last_middle_name(self):
        formatted_name = get_formated_name('alien', 'white', 'D.')
        self.assertEqual(formatted_name, 'Alien D. White')


if __name__ == '__main__':
    unittest.main()