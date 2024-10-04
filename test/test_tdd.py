import unittest
from tdd import sum_of_even , calculate_median, find_missing_number, remove_duplicates, first_non_repeating_char


class TestTdd(unittest.TestCase):
    def test_sum_of_even(self):
        self.assertEqual(sum_of_even([2, 4, 6]), 12)

    def test_calculate_median(self):
        self.assertEqual(calculate_median([1, 3, 5]), 3)

    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([1, 2, 4]), 3)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates("hello"), "helo")

    def test_first_non_repeating_char(self):
        self.assertEqual(first_non_repeating_char("pineapple"), "i")


if __name__ == "__main__":
    unittest.main()
    

"""I am getting an error when I run these testcases:

wtc@pop-os:~/tdd-prac$ python3 -m unittest test_tdd.py
E
======================================================================
ERROR: test_tdd (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_tdd
Traceback (most recent call last):
  File "/usr/lib/python3.10/unittest/loader.py", line 154, in loadTestsFromName
    module = __import__(module_name)
ModuleNotFoundError: No module named 'test_tdd'


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)"""