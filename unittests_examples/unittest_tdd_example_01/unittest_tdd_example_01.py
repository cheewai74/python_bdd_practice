import unittest

class AdditionalTestCase(unittest.TestCase):
    def test_main(self):
        # Arrange Phase

        # Act Phase
        result = additional(1, 2)

        # Assert Phase
        assert result == 3

    def test_threeargs(self):
        # Arrange Phase
        # Act Phase
        result = additional(1, 2, 3)
        # Assert Phase
        assert result == 6

    def test_fourargs(self):
        # Arrange Phase
        # Act Phase
        result = additional()
        # Assert Phase
        assert result == 0


def additional(*args):
    total = 0
    for i in args:
        total += i
    return total
    

if __name__ == '__main__':
    unittest.main()