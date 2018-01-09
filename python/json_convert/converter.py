import json
import random
file_to_convert = input("What is the filename you wish to convert?: ")
new_file_name = input("What do you want to call the new file?: ")

with open('trivia_json/{}'.format(file_to_convert), 'r+') as f:
    data = json.loads(f.read())

new_dict_list = []

for i in data['results']:
    options = i['incorrect_answers']
    options.append(i['correct_answer'])
    random.shuffle(options)
    answer_index = options.index(i['correct_answer'])
    new_dict_list.append({
        'question': i['question'],
        'answer': answer_index,
        'options': options
    })

with open('trivia_json/{}'.format(new_file_name), 'w') as wf:
    wf.write(json.dumps(new_dict_list))
