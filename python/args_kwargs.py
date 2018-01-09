# def add_nums(x, y=10, z=None):
#     if z:
#         return x + y + z
#     return x + y
#
#
# print(add_nums(10))
# print(add_nums(10, 22))
# print(add_nums(y=321, z=22, x=10))

def add_nums(*args, **kwargs):
    '''
    sums all numbers passed
    '''
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))
    total = 0
    for i in args:
        total += i
    return total

x = 'hi'

print(add_nums(1, 4, 56, 35123, 2, 0, word=x, newthing='oldthing'))
