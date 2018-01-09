import datetime

name = input('What is your name?: ')
year = int(input('What year were you born in?(YYYY): '))
age = datetime.datetime.now().year - year
greet = 'Hello {n},\nI\'m glad to meet you! You are {cat} {cat} {n}.'.format(n=name, cat=age)
print(greet)
