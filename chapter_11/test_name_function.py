import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like janis jackson work?"""

    def test_first_last_middle_name(self):
        """Do names like 'wag wig stallone' work?"""
        formatted_name=get_formatted_name('wag', 'stallone', 'wig')
        self.assertEqual(formatted_name, 'Wag Wig Stallone')


if __name__=='__main__':
    unittest.main()
