"""
How to use:
command line -> python analyze.py <desired_text_file> 
[WITHOUT THE .TXT EXTENSION]
"""

import sys
from collections import Counter

file = open(sys.argv[1] + ".txt", "r")
frequency_file = open(str(sys.argv[1]) + "_word_frequency.txt", "w")
punctuation = [',', '.', '.', '..', '...', ';', ':', '?', '\'', '(', ')', '!', '-', '*']
new_string = ""

for line in file:
    new_line = ''.join([i for i in line if not i.isdigit() and i not in punctuation])
    new_line = new_line.lower()
    new_string += new_line
    
word_frequency = Counter(new_string.split()).most_common()
frequency_file.write('UNIQUE WORD COUNT: ' + str(len(word_frequency)) + '\n')
for word in word_frequency:
    frequency_file.write(word[0] + '\t' + str(word[1]) + '\n')
