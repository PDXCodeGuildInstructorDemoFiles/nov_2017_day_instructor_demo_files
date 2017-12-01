lst = [1, 2, 3, 4, 5]
#
# lst2 = []
#
# for num in lst:
#     lst2.append(num + 33)
#
# print(lst2)
# num = 0
# while num < 10000:
#     num += 1
#     print(num)


# while True:
#     try:
#         num = int(input('Please enter a number: '))
#         break
#     # except ValueError:
#     #     print('That is not an int. Try again.')
#     #     continue
#     # except KeyError:
#     #     print('How did you even do that?')
#     #     continue
#
#     print('Your number is now {}!'.format(num ** 47))
#
# print('Your program has finished.')

# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1

# while True:
#     q = input('Press 1 to play, press 2 to quit: ').lower()
#     q2 = input('are you sure?: ').lower()
#     if q == '1' and q2 in ['yes', 'y']:
#         print('THis game is sooooo much fun.<PLACEHOLDER GAME>')
#     elif q == '2':
#         print('Thanks for playing!')
#         quit()
#     else:
#         print('Ummmm, come again?')
#
# print('this will not be seen')


# while True:
#     try:
#         q = int(input('please enter a number: '))
#         break
#     except ValueError:
#         print('I didn\'t understand that')
#
# print('your number is now {}'.format(q * 22))
# lst = [1, 2]
# lst2 = []
# for n in lst:
#     lst2.append(n + 22)
# print(lst2)

# for index in range(len(lst)):
#     lst.append(lst[index])
# print(lst)
# for num in lst:
#     lst.append(num)
#     print(lst)
#     time.sleep(1)

NAME_VALUE = {
        'Ace': 11,
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
        'Queen': 10,
        'King': 10
    }
SUIT = [
    "Diamonds",
    "Hearts",
    "Spades"
]


class Card:
    def __init__(self, rank, suit, value=0):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()

deck = []

for s in SUIT:
    for r, v in NAME_VALUE.items():
        deck.append(Card(r, s, v))

print(deck)
