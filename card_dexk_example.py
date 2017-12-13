import random

card_values = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'King': 10,
    'Queen': 10
}

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{}{}'.format(self.rank[0], self.suit[0])


deck = []

for s in suits:
    for rank, value in card_values.items():
        deck.append(Card(s, rank, value))
random.shuffle(deck)
print(deck)
print(deck.pop())