# def get_tens_digit(num):
#     """
#     Returns the tens digit of a number.
#
#     >>> get_tens_digit(98)
#     8
#     >>> get_tens_digit(11)
#     1
#     >>> get_tens_digit(22)
#     2
#     """
#     return num // 10
#
# # print(get_tens_digit(98))
"""
>>> link('Chuck', 'Norris')
'Chuck-Norris'
>>> link("hello", 1)
'hello-1'
>>> link(40, 2)
'40-2'
"""

def link(st1, st2):
    return '-'.join([str(st1), str(st2)])
