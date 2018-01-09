
def validate_age(age):
    if age < 13:
        raise ValueError('impossible age, too young!: {!r}'.format(age))


def make_validate_age(verb_func):
    def main_func(age):
        validate_age(age)
        print(verb_func(age))

    return main_func


@make_validate_age
def say_happy_birthday(age):
    return "You're {} years old!".format(age)



# validate_and_say_happy_birthday = make_validate_age(say_happy_birthday)

# validate_and_say_happy_birthday(12)

say_happy_birthday(34)