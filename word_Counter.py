# from collections import Counter

# text = "Python is a high-level, interpreted, and general-purpose programming language known for its simple, readable syntax that resembles English"
# # Split function turns the string into list of words.
# count = Counter(text.split())

# # Display the words in number it appeared in the paragraph.
# print("Total count words are \n", count)

# # len function display the total length of the paragraph including spaces
# print(len(text))

# # Display the most common words in the paragraph, the moct common words would be 10, 8, 4, 1, 2 etc
# print("Most commnon words are \n", count.most_common(4))


# ........................................................................................
import re
from collections import Counter

def analyze_paragraph(text):
    ''' pattern (r'[^\w\s]'):
    r: Stands for "Raw String." It tells Python, "Don't try to be clever with backslashes; just read this exactly as it's typed."
    [ ]: These brackets define a set. Everything inside is what we are looking for.
    ^: Inside a set, this means "NOT." It flips the logic. Instead of looking for these characters, we are looking for everything except these characters.
    \w: This represents any Alphanumeric character (letters, numbers, and underscores).
    \s: This represents Whitespace (spaces, tabs, and newlines).l '''
    clean_text = re.sub(r'[^\w\s]', '', text).lower()
    Words = clean_text.split()
    length = len(Words)
    Words_freq = Counter(Words)
    common_words = Words_freq.most_common(3)
    return  length, common_words



paragraph = """
Python is a great programming language. Python is popular because it is easy to learn 
and powerful to use. Many developers love Python for its simple syntax and vast 
library support.
"""

total_words, common_words =  analyze_paragraph(paragraph)
print("----Paragrapgh Analysis----")
print(f"Total words are: {total_words}")
print(f"\nMost common words are")
i = 0
for w, c in common_words:
    i += 1
    print(f" {i}- {w}: {c} times")