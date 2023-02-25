import unittest
from utils import Item


class Testutils(unittest.TestCase):
    def setUp(self):
        self.item = Item("Смартфон", 10000, 20)

    def test_calculate_total_price(self):
        self.assertEqual(self.item.calculate_total_price(), 200000)

    def test_apply_discount(self):
        self.assertEqual(self.item.apply_discount(), None)

