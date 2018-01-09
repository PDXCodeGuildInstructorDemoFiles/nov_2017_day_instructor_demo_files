name = input('What is your name?: ')
greeting = 'Yo, {}. You are awesome!'
if name.lower() == 'chris':
    print('Hi, Chris! I\'m happy to see you!')
    print('HAHAHA YOU look funny!')
elif name.lower() == 'katie':
    print('i said "{}"'.format(greeting.format(name)))
else:
    print(f'Hi {name}')
