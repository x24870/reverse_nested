import unittest

from main import reverse_nested

class Test(unittest.TestCase):
    def test_reverse_nested(self):
        input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        self.assertTrue(
            reverse_nested(input_value) == {'I': {'deserve': {'to': {'be': 'hired'}}}}
        )

if __name__ == '__main__':
    unittest.main()