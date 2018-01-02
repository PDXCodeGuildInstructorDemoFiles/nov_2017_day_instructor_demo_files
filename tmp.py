import random

card_values = {
    'Ace': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6,
    '07': 7, '08': 8, '09': 9, '10': 10, 'Jack': 10, 'King': 10,
    'Queen': 10
}

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    # def __str__(self):
    #     return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{} of {}'.format(self.rank[0:], self.suit[0])

class Deck:
    def __init__(self):
        self.deck = []

        for s in suits:
            for rank, value in card_values.items():
                self.deck.append(Card(s, rank, value))
        # print (self.deck)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def cut_deck(self):
        i = random.randrange(len(self.deck))
        cut1 = self.deck[:i]
        cut2 = self.deck[i:]
        cut_deck = cut2 + cut1
        self.deck = cut_deck

    def dealer_hand(self):
        card_dealt = self.deck.pop()
        return card_dealt
        # print (cut_deck)
        # player = [cut_deck.pop() for _ in range (2)]
        # print (player)

class Hand:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0

    def hand_hit(self, deck_in_play):
        card_dealt = deck_in_play.dealer_hand()
        self.hand.append(card_dealt)
        return self.hand

    def score_hand(self):
        self.value = 0
        for card in self.hand:
            self.value += card.value

    def __str__(self):
        return '{}'.format(self.hand)

    def __repr__(self):
        return self.__str__()

class Game:
    pass

my_deck = Deck()
my_deck.shuffle_deck()
my_deck.cut_deck()

card = my_deck.dealer_hand() #just serves to remove a single card
# print (card)

player_hand = Hand("Player")
cpu_hand = Hand("Dealer")

def initial_hand(who):
    who.hand_hit(my_deck)
    who.hand_hit(my_deck)
    print("{} Hand: {}".format(who.name, who.hand))
    who.score_hand()
    print (who.value)


initial_hand(player_hand)
initial_hand(cpu_hand)

def stay_hit(who, option):
    if option == "hit":
        who.hand_hit(my_deck)
        who.score_hand()
        print("Player Hand: ", who.hand) #maybe need to wrap'
        print (who.value)

    elif option == "stay":
        who.score_hand()
        print("Player Hand: ", who.hand)
        print (who.value)

    else:
        print ("Player Error")

def cpu_stay_hit(who, option):
    if option == "hit":
        who.hand_hit(my_deck)
        who.score_hand()
        print("Dealer Hand: ", who.hand)

    elif option == "stay":
        who.score_hand()
        print("Dealer Hand: ", who.hand)

    else:
        print ("Dealer Error")


def check_game(player_hand, dealer_hand):
    if player_hand.value > dealer_hand.value:
        print("Player Wins!")
    if dealer_hand.value > player_hand.value:
        print("Dealer Wins!")
    else:
        print("Draw Game!")

player = 1
cpu = 1
game = True
# cpu_total = 21


while True:
# while player_game == True:
    if player_hand.value > 21:
        print ("Bust!")
        break
    elif player_hand.value == 21:
        print ("Winner!")
        break
    elif player_hand.value <21:
        query = input("Would you like to stay or hit?:\n")
        stay_hit(player_hand, query)
        if query == "stay":
            break

while True:
    if cpu_hand.value > 21:
        print ("Dealer Bust! You Win!")
        break
    elif cpu_hand.value == 21:
        print ("Dealer Wins! You Lose!")
        break
    elif cpu_hand.value < 15:
        cpu_stay_hit(cpu_hand, "hit")
    elif cpu_hand.value >= 15:
        cpu_stay_hit(cpu_hand, "stay")
        break


check_game(player_hand, cpu_hand)
#CPU