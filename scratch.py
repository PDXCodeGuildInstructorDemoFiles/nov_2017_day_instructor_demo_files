user_in = input("What time is it?:\n")
if 'am' in user_in.lower():
	meridiem = 'am'
elif 'pm' in user_in.lower():
	meridiem = 'pm'
else:
	meridiem = input("Is that am or pm?:\n")

if meridiem == 'am':
    if int(user_in[0]) in (range(1,2)) and user_in2[0] == "p":
        print("Its Lunch Time!")
    elif int(user_in[0]) in (range(7,9)) and user_in2[0] == "a":
        print("Its Breakfast Time!")
    elif int(user_in[0]) in (range(7,9)) and user_in2[0] == "p":
        print("Its Dinner Time!")
    elif int(user_in[0]) in (range(10,12)) and user_in2[0] == "p":
        print("You shouldn't be eating now!")
    elif int(user_in[0]) in (range(5,6)) and user_in2[0] == "a":
        print("You shouldn't be eating now!")
    elif int(user_in[0]) in (range(3,6)) and user_in2[0] == "p":
        print("You shouldn't be eating now!")
    else:
        print("its HAMMER TIME!! CANT TOUCH THIS!")
else:
