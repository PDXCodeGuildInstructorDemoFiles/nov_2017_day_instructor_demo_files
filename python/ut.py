import unittest

from python.card_dexk_example import Card, Deck


class TestCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.ace_of_hearts = Card('Hearts', 'Ace', 1)

    def test_card_value(self):
        self.assertEqual(self.deck.deck[0].value, self.ace_of_hearts.value)
