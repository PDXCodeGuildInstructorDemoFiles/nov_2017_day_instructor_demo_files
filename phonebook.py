def pretty_print(num):
    return '({}) {}-{}'.format(num[:3], num[3:6], num[6:])

phone_dict = {
    'jones': {'f_name': 'Chris', 'l_name': 'Jones', 'phone': '5032779710', 'pretty': pretty_print},
    }


# Create New Contact
def create(f, ln, p):
    phone_dict[ln] = {'f_name': f.capitalize(), 'l_name': ln.capitalize(), 'phone': p, 'pretty': pretty_print}

# Retrieve Contact
def search(q):
    try:
        print(phone_dict[q]['f_name'])
        print(phone_dict[q]['l_name'])
        print(phone_dict[q]['pretty'](phone_dict[q]['phone']))
    except KeyError:
        print("That query does not match anything.")


# Update Existing Contact
def update(oln):
    new_f_name = input("new first name: ").lower()
    new_l_name = input("new last name: ").lower()
    new_phone = input("new phone: ").lower()
    remove(oln)
    create(new_f_name, new_l_name, new_phone)

    print("I'm update!")

# Delete Contact
def remove(ln):
    del phone_dict[ln]


if __name__ == '__main__':
    while True:
        print()
        print(phone_dict)
        print()
        q = input('(C)reate, (S)earch, (U)pdate, (R)emove (Exit): ').lower()
        if q == 'c':
            f_name = input("What is your first name?: ")
            l_name = input("What is your last name?: ")
            phone = input("What is your phone number?: ")
            create(f_name, l_name, phone)
        elif q == 's':
            query = input('What is the last name of the person you are looking for?: ')
            search(query)
        elif q == 'u':
            o_l_name = input("What is the last name of the person you wish to change?: ")
            try:
                phone_dict[o_l_name]
                update(o_l_name)
            except KeyError:
                print("That entry does not match our records.")
        elif q == 'r':
            ln = input('What is the last name of the person you would like to remove?: ')
            remove(ln)
        elif q == 'exit':
                quit()
        else:
            print("I don't understand what you are asking...")
