import unittest
from dataclasses import dataclass
from typing import List

class TestSum(unittest.TestCase):
    def test_sum(self):
        
        @dataclass
        class TestCase:
            name: str
            input: List[int]
            expected: int
        
        testcases = [
            TestCase(name="No nums to sum", input=[], expected=0),
            TestCase(name="Sum 1 + 2 equals 3", input=[1, 2], expected=3),
        ]

        for case in testcases:
            actual = sum(case.input)
            self.assertEqual(case.expected, actual, "Failed test {}. Expected {}, but actual was {}".format(case.name, case.expected, actual))        



if __name__ == "__main__":
    unittest.main()