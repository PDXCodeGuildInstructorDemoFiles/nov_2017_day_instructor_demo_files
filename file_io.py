# f = open("text_file.txt", 'r')
# content = f.read()
# new_content = content.replace('l', '1')
# f.close()
#
# wf = open("text_file.txt", 'w')
# wf.write(new_content)
# wf.close()

# with open("text_file.txt", 'r') as f:
#     content = f.read().replace('l', '1')
#
# with open("text_file.txt", 'w') as wf:
#     wf.write(content)
#
#     set things up
#     try:
#         do something
#     finally:
#         f.close()

# with open('text_file.txt', 'r+') as f:
#     lines = [i.replace('\n', '') for i in f.readlines()]
#     # for i in f.readlines():
#     #     lines.append(i.replace('\n', ''))
#
# print(lines)
# for l in lines:
#     print(l)
import json

with open('json_files/data_example.json', 'r') as f:
    data = json.loads(f.read())

for i in range(len(data)):
    data[i]['glossary']['title'] = 'A new Title for this thing x {}'.format('*'*(i+1))

with open('json_files/data_example.json', 'w') as f:
    f.write(json.dumps(data))

with open('json_files/data_example.json', 'r') as f:
    data = json.loads(f.read())

for i in range(len(data)):
    print(data[i]['glossary']['title'])
