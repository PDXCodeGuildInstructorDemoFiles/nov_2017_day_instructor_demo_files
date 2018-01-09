import random


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{}{}'.format(self.rank[0], self.suit[0])


class Deck:
    def __init__(self):
        self.deck = self.generate_deck()

    def generate_deck(self, deck_size=6):
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
        return [Card(s, rank, value) for s in suits for rank, value in card_values.items() for x in range(deck_size)]


if __name__ == "__main__":
    deck = Deck()
    print(deck.deck)

    # deck = []
    #
    # for s in suits:
    #     for rank, value in card_values.items():
    #         deck.append(Card(s, rank, value))
    # random.shuffle(deck)
    # print(deck)
    # print(deck.pop())
