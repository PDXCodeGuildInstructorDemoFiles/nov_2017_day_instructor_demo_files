'''
Write a function that returns the meal for any given hour of the day or night
in respect to the following schedule:

```
Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM
```
'''

time = input('What time is it?(HH:MM:am/pm): ').lower()

hour, minute, merd = time.split(':')

if merd == 'am':
    # if hour == '07' or hour == '08' or hour == '09':
    if hour in ['07', '08', '09']:
        print('Breakfast')
    elif hour in ['12', '01', '02', '03', '04']:
        print('HammerTime!')
    else:
        print('GO TO SLEEP!')
else:
    if hour in ['12', '01', '02']:
        print('Lunch')
    elif hour in ['07', '08', '09']:
        print('Dinner')
    elif hour in ['10', '11', '12']:
        print('HammerTime!')
    else:
        print('Work Time!')
