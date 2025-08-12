"""Day18 30 days of Python Programming"""

import re

def clean_text(sentence):
    pattern=r"[^a-zA-Z.? ]*"
    return re.sub(pattern, '', sentence)


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s 
mo@tivate yo@u to be a tea@cher!?'''

cleaned_text=clean_text(sentence)
# print(clean_text(sentence))

def most_frequent_words(sentence):
    words = re.findall(r"\w+", cleaned_text)
    words_unique=set(words)
    frequence=list(map(lambda word: (words.count(word), word), words_unique))
    frequence=sorted(frequence, key=lambda item: item[0], reverse=True)
    return frequence[:3]

print(most_frequent_words(cleaned_text))