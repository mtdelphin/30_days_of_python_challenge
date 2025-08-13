"""Day19 30 days of Python Programming"""

import re


#4
def extract_incoming_emails():
    with open("./data/email_exchanges_big.txt") as f:
        content=f.read()
        incoming_lines=re.findall(r"^From ([\w\.-]+@[\w\.-]+\.\w{2,4})", content, re.MULTILINE)
        emails=set(incoming_lines)
        return list(emails)

print(extract_incoming_emails())

#5
def find_most_common_words(filename, limit):
    with open(filename) as f:
        content=f.read()
        words=re.findall(r"\w+", content, re.MULTILINE)
        words_unique=set(words)
        appearences=[(words.count(word), word) for word in words_unique]
        return sorted(appearences, key=lambda w: w[0], reverse=True)[:limit]
    
print(find_most_common_words('./files/reading_file_example.txt', 4))