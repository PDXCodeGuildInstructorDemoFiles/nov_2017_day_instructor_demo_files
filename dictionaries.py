# dict()
# value2 = 'value2'
# dct = {(0, 1): 'Large Dark Room'}
# player_loc = (0, 0)
#
# def move_right(loc):
#     return (loc[0], loc[1] + 1)
#
# print(dct[move_right(player_loc)])

# dct = {
#     'fruit': ['apple', ['banana', 'bananb'], 'grape'],
#     'people': {'names': ['Chris', 'Katie', 'Chelsea']}
#     }
# dct['fruit'][1] = 'GrapeFruit'

# print(dct['fruit'][1][0])
# print(len(dct['people']['names']))#['names'][0])
# print(dct['people']['names'])
# dct['people']['names'].append('Sheri')
# print(dct['people']['names'])
# dct['animals'] = ['Rex', 'TigerNice', 'phteven']
# print(dct)
# del dct['people']
# print(dct)

phonebook = {
    'jones': {'first_name': 'Chris', 'last_name': 'Jones', 'phone': '5032779710'},
    'dover': {'first_name': 'Sheri', 'last_name': 'Dover', 'phone': '5551212122'},
}

def search(query):

    old_fname = phonebook[query]['first_name'][:]
    phonebook[query]['first_name'] = 'blah'
    print(old_fname)
    print()
    print(phonebook[query]['first_name'])
    # try:
    #     print('Full Name: {} {}'.format(phonebook[query]['first_name'], phonebook[query]['last_name']))
    #     print('Phone: {}'.format(phonebook[query]['phone']))
    # except KeyError:
    #     print('That is not a valid entry.')

q = input("who are you looking for?: ").lower()
search(q)
