words  = {'the': 1}

text = ['the', 'the', 'blah', 'hi', 'hi', 'hi']

for i in text:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1
        

for k, v in words.items():
    print('{}:{} times.'.format(k, v))
