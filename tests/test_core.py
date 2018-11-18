import unittest
from src import core


class TestCore(unittest.TestCase):
    occr = ['A', 'B', 'C', 'A', 'B', 'B']

    def test_count(self):

        expected = {
            'A': 2,
            'B': 3,
            'C': 1
        }

        actual = core._count(self.occr)
        self.assertEqual(expected, actual)

    def test_sort_based_on_occurrence(self):
        expected =[['B', 3], ['A', 2], ['C', 1]]
        
        actual = core._sort_based_on_occurrence(self.occr)
        self.assertEqual(expected, actual)



