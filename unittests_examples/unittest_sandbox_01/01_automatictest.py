"""

python 01_automatictest.py

python 01_automatictest.py -v

"""

import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

class MySecondTestCase(unittest.TestCase):
    def test_two(self):
        pass

    def test_three(self):
        pass


if __name__ == '__main__':
    unittest.main()