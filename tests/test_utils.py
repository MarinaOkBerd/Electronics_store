import pytest

from utils import Item, Phone

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    assert item1.apply_discount() == None


def test_test_number_of_sim():
    assert phone1.number_of_sim == 2
    phone1.test_number_of_sim = 0
    assert phone1.test_number_of_sim == 0


def test_add():
    assert phone1 + item1 == 25

