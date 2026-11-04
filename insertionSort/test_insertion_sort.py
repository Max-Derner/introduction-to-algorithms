import unittest

from insertion_sort import sort


class TestSort(unittest.TestCase):
    def test_sort(self):
        unsorted_nums = [3, 7, 6, 4, 8, 2, 9, 1, 10, 5]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        result = sort(unsorted_nums)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
