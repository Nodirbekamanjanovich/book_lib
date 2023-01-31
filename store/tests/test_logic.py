from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_minus(self):
        result = operations(8, 15, '-')
        self.assertEqual(-7, result)

    def test_plus(self):
        result = operations(8, 15, "+")
        self.assertEqual(23, result)

    def test_multiply(self):
        result = operations(8, 15, "*")
        self.assertEqual(120, result)
