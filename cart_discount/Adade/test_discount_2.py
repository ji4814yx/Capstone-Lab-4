import unittest
from unittest import TestCase
from price_discount_2 import discount


class TestDiscount(TestCase):

    # 3 items, discount
    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    # 2 items, discount wont apply
    def test_list_of_two_prices_no_discount(self):
        prices = [20, 1]  # arrange
        expected_discount = 0  # arrange
        actual_discount = discount(prices)  # action
        self.assertEqual(expected_discount, actual_discount)  # assert

    # Test with 1 item, then discount
    def test_returns_0_when_called_with_1_item(self):
        prices = [11]

        expected_discount = 0  # arrange

        actual_discount = discount(prices)
        self.assertEqual(expected_discount, actual_discount)

    # Test with 4 items
    def test_four_items(self):
        prices = [11, 4, 5, 7]

        expected_discount = 4

        self.assertEqual(expected_discount, discount(prices))

    # Test with more than 4 items
    def test_more_than_4_items_in_cart(self):
        self.assertEqual(discount([5, 10, 15, 20, 25]), 5)

    # Empty list
    def test_if_list_is_empty(self):
        prices = []

        expected_discount = 0

        self.assertEqual(expected_discount, discount(prices))

    # Same prices
    def test_if_same_prices(self):
        prices = [11, 11, 11]

        expected_discount = 11

        self.assertEqual(expected_discount, discount(prices))

    def test_if_price_is_float(self):
        prices = [23.50, 4.50, 0.50, 5.50]  # Arrange the scenario to set

        expected_discount = 0.50

        actual_discount = discount(prices)  # do the action to test, save the output from the method to test
        self.assertEqual(expected_discount, actual_discount)

    def test_if_price_list_of_string(self):
        prices = ["1", "2", "3"]

        expected_discount = "1"


if __name__ == '__main__':
    unittest.main()

    # Tests
    # Same prices, empty list, 4 items, more than 4 items, 1 tests, 2 items, 3 items

    # Other Tests That Are Not Written Yet
    # Strings
    # Negatives
    # Other iterative beside a lists
    # Emojis
    # Other type of characters
    # Floats
