from string import punctuation
from operator import itemgetter
common_words = ['time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world', 'life', 'hand', 'part', 'child', 'eye',
                'woman', 'place', 'work', 'week', 'case', 'point', 'government', 'company', 'number', 'group',
                'problem', 'fact', 'be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come',
                'think', 'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'try', 'leave',
                'call', 'good', 'new', 'first', 'last', 'long', 'great', 'little', 'own', 'other', 'old', 'right',
                'big', 'high', 'different', 'small', 'large', 'next', 'early', 'young', 'important', 'few', 'public',
                'bad', 'same', 'able', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from', 'up', 'about', 'into',
                'over', 'after', 'the', 'and', 'a', 'that', 'i', 'it', 'not', 'he', 'as', 'you', 'this', 'but', 'his',
                'they', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'is', 'was',
                'said', 'mrs', 'had', 'mr', 'what', 'me']


def get_text(file_location):
    with open(file_location, 'r') as f:
        txt = f.read().lower()
    return txt


def clean_text(text):
    for i in punctuation:
        text = text.replace(i, '')
    txt_list = text.split()
    return [w for w in txt_list if w not in common_words]


def word_count(cleaned_txt_list):
    words = {}
    for w in cleaned_txt_list:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1
    return words


def find_top(word_dic, n=10):
    word_count_list = list(word_dic.items())
    return sorted(word_count_list, key=itemgetter(1), reverse=True)[:n]


if __name__ == '__main__':
    # txt = get_text('hex.txt')
    # clean = clean_text(txt)
    # words = word_count(clean)
    # print(find_top(words))
    print(find_top(word_count(clean_text(get_text('hex.txt')))))
