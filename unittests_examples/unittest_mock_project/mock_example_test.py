import unittest
from mock import Mock


class TestMockExample(unittest.TestCase):

    def test_mock_method_returns(self):
        # Create a mock object
        myMock = Mock()

        # Define the behavior of the mock object
        myMock.my_method.return_value = 'hello world'

        # Call the method and assert the return value
        self.assertEqual('hello world', myMock.my_method())


if __name__ == '__main__':
    unittest.main()