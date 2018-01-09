def gen_odd_num(less_than):
    for i in range(less_than):
        if i % 2 == 1:
            yield i


print(gen_odd_num(100))
