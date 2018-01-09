# def factorial(4):
#     print('factorial has been called with n = {}'.format(n))
#     # if 5 == 1:
#     #     return 1
#     # else:
#         res = 4 * factorial(4-1)
#         print('intermediate result for {} * factorial({}): {}'.format(n, n-1, res))
#         return res
#
# print(factorial(5))

import datetime

# def timer(function):
#     def timed(*args, **kwargs):
#         start = datetime.datetime.now()
#         result = function(*args, **kwargs)
#         end = datetime.datetime.now()
#         print(end - start)
#         return result
#     return timed
#
# @timer
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

def contains_factory(x):
    def contains(lst):
        return x in lst
    return contains

l = [1, 22, 15, 8, 7, 66]
contains_22 = contains_factory(22)
contains_55 = contains_factory(55)

print(contains_22(l))
print(contains_55(l))

# print(fib(5))
# start = datetime.datetime.now()
# print(fib(30))
# end = datetime.datetime.now()
# print(end - start)
