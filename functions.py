# # def greeting():
# #     if somebool:
# #         return 'Hey!'
# #     else:
# #         return 'How are you?'
# #
# # print(type(greeting()))
#
# # name = 'input('What is your name?: ')'
# #
# # def greeting(n):
# #     return 'Hey, {}!'.format(n)
# #
# # print(greeting(name))
#
#
# name = input('name: ')
# original_name = name[:]
#
# def rename_again():
#     global name
#     name = original_name
#
# def rename_name():
#     global name
#     rename_again()
#     name ='not what you entered.'
#
# print(name)
# rename_name()
# print(name)
#
#
# print(name)
# rename_again()
# print(name)
x = 0
x = 'sojtngashd;lf'

def add_two_nums(x, y):
    x += 1
    return x + y

x += 1

bad_var = 'gdfaskjhfgdaskjhgdfas'
num_total = add_two_nums(
    int(input('give me and int: ')),
    int(input('give me and int: '))
)

print(num_total)
