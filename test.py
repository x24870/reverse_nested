import unittest

from main import reverse_nested

class Test(unittest.TestCase):
    def test_reverse_nested(self):
        input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        self.assertTrue(
            reverse_nested(input_value) == {'I': {'deserve': {'to': {'be': 'hired'}}}}
        )

        self.assertTrue(
            reverse_nested({1: {2: 3}}) == {3: {2: 1}}
        )

        self.assertTrue(
            reverse_nested({}) == {}
        )

if __name__ == '__main__':
    unittest.main()